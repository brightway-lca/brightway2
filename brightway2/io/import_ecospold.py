# -*- coding: utf-8 -*
from __future__ import division
from brightway2 import Database, mapping
from brightway2.logs import get_logger
from brightway2.errors import UnknownExchange
from lxml import objectify
import math
import os
import progressbar
from stats_toolkit.distributions import *

BIOSPHERE = ("air", "water", "soil", "resource")


class EcospoldImporter(object):
    def importer(self, path, name, depends=["biosphere", ]):
        data = []
        log = get_logger(name)
        log.critical(u"Starting import of %s (from %s)" % (name, path))
        if os.path.isdir(path):
            files = [os.path.join(path, filter(lambda x: x[-4:].lower(
                ) == ".xml", os.listdir(path)))]
        else:
            files = [path]

        widgets = ['Files: ', progressbar.Percentage(), ' ',
            progressbar.Bar(marker=progressbar.RotatingMarker()), ' ',
            progressbar.ETA()]
        pbar = progressbar.ProgressBar(widgets=widgets, maxval=len(files)
            ).start()

        for index, filename in enumerate(files):
            root = objectify.parse(open(filename)).getroot()

            if root.tag != '{http://www.EcoInvent.org/EcoSpold01}ecoSpold':
                # Unrecognized file type
                log.critical(u"skipping %s - no ecoSpold element" % filename)
                continue

            for dataset in root.iterchildren():
                data.append(self._process_dataset(dataset))

            pbar.update(index)

        # Hackish
        for o in data:
            try:
                o["code"] = int(o["code"])
            except:
                pass

        # Fix exchanges
        codes = set([o["code"] for o in data])
        for ds in data:
            for exc in ds["exchanges"]:
                code = exc["code"]
                # Hack - not work with others?
                try:
                    code = int(code)
                except:
                    pass
                if code in codes:
                    exc["input"] = (name, code)
                else:
                    exc["input"] = self._find_in_dependent_database(code,
                        exc, depends)
                exc["technosphere"] = exc["input"][0] != "biosphere"

        data = dict([((name, int(o["code"])), o) for o in data])

        manager = Database(name)
        manager.register("Ecospold 1", depends, len(data))
        manager.write(data)

        pbar.finish()

    def _find_in_dependent_database(self, code, exc, depends):
        for db in depends:
            if (db, code) in mapping:
                return (db, code)

        # Add new biosphere flow if needed
        if exc["_matching"].get("categories", [None, ])[0] in BIOSPHERE:
            data = exc["_matching"]

            # Emission or resource
            resource = data["categories"][0] == "resource"
            data["type"] = "resource" if resource else "emission"

            # Biosphere flows don't have locations or exchanges
            del data["location"]
            data["exchanges"] = []

            # Write modified biosphere database
            biosphere = Database("biosphere")
            bio_data = biosphere.load()
            bio_data[("biosphere", code)] = data
            biosphere.write(bio_data)
            return ("biosphere", code)
        raise UnknownExchange(("The exchange %s couldn't be " + \
            "matched to this or a depending database") % code)

    def _process_dataset(self, dataset):
        data = {}
        ref_func = dataset.metaInformation.processInformation.\
            referenceFunction

        data["name"] = ref_func.get("name")
        data["type"] = "process"  # True for all ecospold?
        data["categories"] = [ref_func.get("category"), ref_func.get(
            "subCategory")]
        # Convert ("foo", "unspecified") to ("foo",)
        while data["categories"][-1] == "unspecified":
            data["categories"] = data["categories"][:-1]
        data["location"] = dataset.metaInformation.processInformation.\
            geography.get("location")
        data["code"] = dataset.get("number")
        data["unit"] = ref_func.get("unit")
        data["exchanges"] = self._process_exchanges(dataset)
        return data

    def _process_exchanges(self, dataset):
        data = []
        # Skip definitional exchange - we assume this already
        for exc in dataset.flowData.iterchildren():
            if exc.get("name") == dataset.metaInformation.processInformation.\
                    referenceFunction.get("name") != None and float(
                    exc.get("meanValue", 0.)) == 1.0:
                continue

            this = {
                "code": int(exc.get("number")),
                "_matching": {
                    "categories": (exc.get("category"), exc.get("subCategory")),
                    "location": exc.get("location"),
                    "unit": exc.get("unit"),
                    "name": exc.get("name")
                    }
                }

            if exc.get("generalComment"):
                this["pedigree matrix"] = exc.get("generalComment")

            uncertainty = int(exc.get("uncertaintyType", 0))
            mean = exc.get("meanValue")
            min_ = exc.get("minValue")
            max_ = exc.get("maxValue")
            sigma = exc.get("standardDeviation95")

            if uncertainty == 1:
                # Lognormal
                this.update({
                    'uncertainty type': LognormalUncertainty.id,
                    'amount': float(mean),
                    'sigma': math.log(math.sqrt(float(sigma)))
                    })
                if this['sigma'] == 0:
                    # Bad ecoinvent data
                    this['uncertainty type'] = UndefinedUncertainty.id
                    del this["sigma"]
            elif uncertainty == 2:
                # Normal
                this.update({
                    'uncertainty type': NormalUncertainty.id,
                    'amount': float(mean),
                    'sigma': float(sigma) / 2
                    })
            elif uncertainty == 3:
                # Triangular
                this.update({
                    'uncertainty type': TriangularUncertainty.id,
                    'minimum': float(min_),
                    'maximum': float(max_)
                    })
                # Sometimes this isn't included (though it SHOULD BE)
                if exc.get("mostLikelyValue"):
                    this['amount'] = float(exc.get("mostLikelyValue"))
                else:
                    this['amount'] = float(mean)
            elif uncertainty == 4:
                # Uniform
                this.update({
                    'uncertainty type': UniformUncertainty.id,
                    'amount': float(mean),
                    'minimum': float(min_),
                    'maximum': float(max_)
                    })
            else:
                # None
                this.update({
                    'uncertainty type': UndefinedUncertainty.id,
                    'amount': float(mean)
                })

            data.append(this)

        return data
