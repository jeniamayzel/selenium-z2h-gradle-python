from ui_builder.pages.BasePage import BasePage

class LoginPage(BasePage):

    LOGIN_URI = "login"
    USERNAME_ID = "login_field"
    PASSWORD_ID = "password"
    LOGIN_BTN_NAME = "commit"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def go(self):
        BasePage(self.driver).gotoUrl(self.LOGIN_URI)
        return self

    def input_username(self, input):
        element = self.find_by_id(self.USERNAME_ID)
        BasePage(self.driver).input_text(element, input)
        return self

    def input_password(self, input):
        element = self.find_by_id(self.PASSWORD_ID)
        BasePage(self.driver).input_text(element, input)
        return self

    def click_login(self):
        element = self.find_by_name(self.LOGIN_BTN_NAME)
        BasePage(self.driver).click(element)
        return self




