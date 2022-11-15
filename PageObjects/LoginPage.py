from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    logIn_btn = (By.ID, "logIn")
    needHelp_link=(By.LINK_TEXT,"Need help?")

    def getEmailField(self):
        return self.driver.find_element(*LoginPage.email_field)

    def getPasswordField(self):
        return self.driver.find_element(*LoginPage.password_field)

    def clickLoginButton(self):
        return self.driver.find_element(*LoginPage.logIn_btn).click()

    def clickNeedHelpLink(self):
        return self.driver.find_element(*LoginPage.needHelp_link).click()
