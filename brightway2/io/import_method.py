# -*- coding: utf-8 -*
from brightway2 import Database, mapping, Method, methods
from lxml import objectify
import os
import progressbar
try:
    import cPickle as pickle
except:
    import pickle


class EcospoldImpactAssessmentImporter(object):
    """
Import impact assessment methods and weightings from ecospold XML format.
    """
    def importer(self, path):
        if os.path.isdir(path):
            files = [os.path.join(path, filter(lambda x: x[-4:].lower(
                ) == ".xml", os.listdir(path)))]
        else:
            files = [path]

        self.biosphere_data = Database("biosphere").load()
        if progressbar:
            widgets = ['Files: ', progressbar.Percentage(), ' ',
                progressbar.Bar(marker=progressbar.RotatingMarker()), ' ',
                progressbar.ETA()]
            pbar = progressbar.ProgressBar(widgets=widgets, maxval=len(files)
                ).start()

        for index, filepath in enumerate(files):
            # Note that this is only used for the first root method found in
            # the file
            root = objectify.parse(open(filepath)).getroot()
            for dataset in root.iterchildren():
                self.add_method(dataset)
            pbar.update(index)

        pbar.finish()

    def add_method(self, ds):
        ref_func = ds.metaInformation.processInformation.referenceFunction
        name = (ref_func.get("category"), ref_func.get("subCategory"),
            ref_func.get("name"))
        description = ref_func.get("generalComment") or ""
        unit = ref_func.get("unit") or ""
        data = {}
        for cf in ds.flowData.iterchildren():
            if ("biosphere", int(cf.get("number"))) not in mapping:
                # Add new biosphere flow
                code = int(cf.get("number"))
                new_flow = {
                    "name": cf.get("name"),
                    "categories": (cf.get("category"),
                        cf.get("subCategory") or "unspecified"),
                    "code": code,
                    "unit": cf.get("unit"),
                    "exchanges": []
                }

                # Convert ("foo", "unspecified") to ("foo",)
                while new_flow["categories"][-1] == "unspecified":
                    new_flow["categories"] = new_flow["categories"][:-1]

                # Emission or resource
                resource = new_flow["categories"][0] == "resource"
                new_flow["type"] = "resource" if resource else "emission"

                # Write modified biosphere database
                biosphere = Database("biosphere")
                bio_data = biosphere.load()
                bio_data[("biosphere", code)] = new_flow
                biosphere.write(bio_data)
                return ("biosphere", code)
            data[("biosphere", int(cf.get("number")))] = float(
                cf.get("meanValue"))
        assert name not in methods
        method = Method(name)
        method.register(unit, description, len(data))
        method.write(data)
        method.process()
