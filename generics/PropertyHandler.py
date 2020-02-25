from argparse import Namespace

import yaml
import json
from collections import namedtuple

from generics.PropsModel import PropsModel


class PropertyHandler:

    def __init__(self):
        pass

    def readYamlFile(self, filePath):
        allProps = []
        with open(filePath) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            for item in data.get("props"):
                parsedItem = PropsModel(**data.get("props")[0])
                allProps.append(parsedItem)

            # for prop in allProps:
            #     print(prop)
            return allProps