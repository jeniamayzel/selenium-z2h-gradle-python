from ui_builder.pages.LoginPage import LoginPage


class LoginFlow:

    def __init__(self, driver):
        self.driver = driver

    def basic_login_flow(self, username, password):
        page = LoginPage(self.driver)
        page.go()
        page.input_username(username)
        page.input_password(password)
        page.click_login()

    def basic_login_fluent_flow(self, username, password):
        LoginPage(self.driver)\
            .go()\
            .input_username(username)\
            .input_password(password)\
            .click_login()
