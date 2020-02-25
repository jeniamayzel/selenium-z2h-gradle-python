from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    BASE_URL = "https://www.github.com/";
    WAIT_TIME = 60

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIME)

    def gotoUrl(self, uri):
        self.driver.get(self.BASE_URL + uri)

    #Base Functions
    def input_text(self, element, input = ""):
        element.clear()
        element.send_keys(input)
        return self

    def click(self, element):
        element.click()
        return self

    #Locators
    def find_by_id(self, value = ""):
        return self.driver.find_element(by=By.ID, value=value)

    def find_by_name(self, value = ""):
        return self.driver.find_element(by=By.NAME, value=value)

    def find_by_xpath(self, value = ""):
        return self.driver.find_element(by=By.XPATH, value=value)

    def find_by_link_text(self, value = ""):
        return self.driver.find_element(by=By.LINK_TEXT, value=value)

    def find_by_partial_link_text(self, value = ""):
        return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=value)

    def find_by_tag_name(self, value = ""):
        return self.driver.find_element(by=By.TAG_NAME, value=value)

    def find_by_class_name(self, value = ""):
        return self.driver.find_element(by=By.CLASS_NAME, value=value)

    def find_by_css(self, value = ""):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=value)
