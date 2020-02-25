import unittest

from generics.PropertyHandler import PropertyHandler
import pathlib

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        modulePath = str(pathlib.Path(__file__).parent)
        envFile = modulePath + "\\resources\\myEnv.yaml"
        # print(envFile)
        self.myEnvProps = PropertyHandler().readYamlFile(envFile)
