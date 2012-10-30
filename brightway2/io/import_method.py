# -*- coding: utf-8 -*
from brightway2 import config, Manager, mapping, methods
from lxml import objectify
import os
import string
import random
try:
    import cPickle as pickle
except:
    import pickle


def abbreviate(names, length=8):
    abbrev = lambda x: x if x[0] in string.digits else x[0].lower()
    name = " ".join(names).split(" ")[0].lower() + \
        "".join([abbrev(x) for x in " ".join(names).split(" ")[1:]])
    random_string = ''.join(random.choice(string.letters + string.digits
        ) for i in xrange(length))
    return name + "-" + random_string


def import_ia_dir(dirpath):
    for filename in filter(lambda x: x.lower()[-4:] == ".xml",
            os.listdir(dirpath)):
        filepath = os.path.join(dirpath, filename)
        print "Working on %s" % filepath
        EcospoldImpactAssessmentImporter(filepath)


class EcospoldImpactAssessmentImporter(object):
    """
Import impact assessment methods and weightings from ecospold XML format.
    """
    def __init__(self, filename):
        self.filename = filename
        self.biosphere_data = Manager("biosphere").load()
        # Note that this is only used for the first root method found in
        # the file
        root = objectify.parse(open(self.filename)).getroot()
        for dataset in root.iterchildren():
            self.add_method(dataset)

    def add_method(self, ds):
        ref_func = ds.metaInformation.processInformation.referenceFunction
        name = (ref_func.get("category"), ref_func.get("subCategory"),
            ref_func.get("name"))
        abbreviation = abbreviate(name)
        print abbreviation, name
        filepath = os.path.join(config.dir, "ia", "%s.pickle" % abbreviation)
        description = ref_func.get("generalComment") or ""
        unit = ref_func.get("unit") or ""
        data = []
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
                biosphere = Manager("biosphere")
                bio_data = biosphere.load()
                bio_data[("biosphere", code)] = new_flow
                biosphere.write(bio_data)
                return ("biosphere", code)
            data.append((("biosphere", int(cf.get("number"))), float(cf.get(
                "meanValue"))))
        methods.add(name, {
            'abbreviation': abbreviation,
            'description': description,
            'unit': unit
            })
        pickle.dump(data, open(filepath, "wb"),
            protocol=pickle.HIGHEST_PROTOCOL)
        methods.process(name)
