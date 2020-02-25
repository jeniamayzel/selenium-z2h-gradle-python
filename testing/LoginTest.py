import unittest
import HtmlTestRunner

from testing.BaseTest import BaseTest

class LoginTest(BaseTest):

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    # #Before Method
    # def setUp(self):
    #     print("running : " + self.func_name())

    # @unittest.skip
    def test_neg(self):
        print(self.myEnvProps)
        self.assertEqual(self.myEnvProps[0].username, "myUsername", "failed on assertion")

    def test_pos(self):
        self.assertEqual(5, 5)

if __name__ == '__main__':
    # htmlRunner = HtmlTestRunner.HTMLTestRunner()
    # unittest.main(verbosity=0, failfast=False, testRunner=htmlRunner)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(LoginTest))
    runner = unittest.TextTestRunner(verbosity=3, failfast=False)
    result = runner.run(suite)
