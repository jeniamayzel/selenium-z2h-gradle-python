from selenium import webdriver
class SeleniumDriver:

    timeout_time = 60
    selenium_hub = 'http://127.0.0.1:4444/wd/hub'

    def __init__(self):
        pass

    def setTimeouts(self, driver):
        driver.set_page_load_timeout(self.timeout_time)
        driver.set_script_timeout(self.timeout_time)
        driver.implicitly_wait(self.timeout_time)
        return self.driver

    def setChromeOptions(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        return options

    def withChrome(self):
        self.driver = webdriver.Chrome(chrome_options=self.setChromeOptions())
        return self.setTimeouts(self.driver)

    # command_executor = 'http://127.0.0.1:4444/wd/hub',
    # desired_capabilities = None, browser_profile = None, proxy = None,
    # keep_alive = False, file_detector = None, options = None

    def withSeleniumHub(self, address):
        self.selenium_hub = 'http://%s:4444/wd/hub' % (str(address))
        return self

    def withChromeRemote(self):
        self.driver = webdriver.Remote(command_executor = self.selenium_hub, options=self.setChromeOptions())
        return self.setTimeouts(self.driver)