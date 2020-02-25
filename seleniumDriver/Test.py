import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# # options.binary_location = r'C:\work\selenium\drivers\chromedriver.exe'
# driver = webdriver.Chrome(chrome_options=options)
from seleniumDriver.SeleniumDriver import SeleniumDriver
from ui_builder.flows.LoginFlow import LoginFlow


driver = SeleniumDriver().withSeleniumHub("10.54.245.62").withChromeRemote()
# driver = SeleniumDriver().withChrome()

LoginFlow(driver).basic_login_flow("username", "pass")

driver.get('https://python.org')
driver.close()

# cdd = GeckoDriverManager()
# cdd.download_and_install()
# path = cdd.get_download_path()
# geckoFullPath = path + "\geckodriver-v0.26.0-win32\geckodriver.exe"
# print geckoFullPath
# binary = FirefoxBinary(geckoFullPath)
# os.environ["PATH"] += os.pathsep + r'C:\Users\mayzee\AppData\Local\salabs_\WebDriverManager\gecko\v0.26.0\geckodriver-v0.26.0-win32\geckodriver.exe';
# browser = webdriver.Firefox(firefox_binary=binary)
#
#
#
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = geckoFullPath
# capabilities = webdriver.DesiredCapabilities()
# driver = webdriver.Remote(desired_capabilities=capabilities.FIREFOX)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()