# -*- coding: utf-8 -*
from .. import config, Database
from lxml.builder import ElementMaker
from lxml.etree import tostring
import datetime
import itertools
import os
import progressbar


class DatabaseToGEXF(object):
    def __init__(self, database, include_descendants=False):
        self.database = database
        self.descendants = include_descendants
        if self.descendants:
            raise NotImplemented
        filename = database + ("_plus" if include_descendants else "")
        self.filepath = os.path.join(config.request_dir("output"),
            filename + ".gexf")
        self.data = Database(self.database).load()
        self.id_mapping = dict([(key, str(i)) for i, key in enumerate(
            self.data)])

    def export(self):
        E = ElementMaker(namespace="http://www.gexf.net/1.2draft",
            nsmap={None: "http://www.gexf.net/1.2draft"})
        meta = E.meta(E.creator("Brightway2"), E.description(self.database),
            lastmodified=datetime.date.today().strftime("%Y-%m-%d"))
        attributes = E.attributes(
            E.attribute(id="0", title="category", type="string"),
            **{"class": "node"}
        )
        nodes, edges = self.get_data(E)
        graph = E.graph(attributes, nodes, edges, mode="static",
            defaultedgetype="directed")
        with open(self.filepath, "w") as f:
            f.write(tostring(E.gexf(meta, graph, version="1.2"),
                xml_declaration=True, encoding="utf-8",
                pretty_print=True))

    def get_data(self, E):
        count = itertools.count()
        nodes = []
        edges = []

        widgets = ['Processes: ', progressbar.Percentage(), ' ',
            progressbar.Bar(marker=progressbar.RotatingMarker()), ' ',
            progressbar.ETA()]
        pbar = progressbar.ProgressBar(widgets=widgets, maxval=len(self.data)
            ).start()

        for i, (key, value) in enumerate(self.data.iteritems()):
            nodes.append(E.node(
                E.attvalues(
                    E.attvalue(
                        value="-".join(value["categories"]),
                        **{"for": "0"}
                    )
                ),
                id=self.id_mapping[key],
                label=value["name"]
            ))
            for exc in value["exchanges"]:
                if exc["input"] not in self.id_mapping:
                    continue
                else:
                    edges.append(E.edge(
                        id=str(count.next()),
                        source=self.id_mapping[exc["input"]],
                        target=self.id_mapping[key]
                    ))
            pbar.update(i)
        pbar.finish()

        return E.nodes(*nodes), E.edges(*edges)
