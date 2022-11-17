from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    logIn_btn = (By.ID, "logIn")
    needHelp_link=(By.LINK_TEXT,"Need help?")

    def get_email_field(self):
        return self.driver.find_element(*LoginPage.email_field)

    def get_password_field(self):
        return self.driver.find_element(*LoginPage.password_field)

    def click_login_button(self):
        return self.driver.find_element(*LoginPage.logIn_btn).click()

    def click_need_help_link(self):
        return self.driver.find_element(*LoginPage.needHelp_link).click()
