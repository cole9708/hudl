from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LoginHelpPage:

    def __init__(self, driver):
        self.driver = driver

    reset_email_field = (By.CSS_SELECTOR, "input[data-qa-id='password-reset-input']")
    password_field = (By.ID, "password")
    reset_btn = (By.CSS_SELECTOR, "button[data-qa-id='password-reset-submit-btn']")
    check_email_banner=(By.CSS_SELECTOR,"h3[class='uni-headline']")

    #class ="uni-form--large


    def getRestEmailFieldValue(self):
        return self.driver.find_element(*LoginHelpPage.reset_email_field).get_attribute('value')

    def clickResetButton(self):
        button =self.driver.find_element(*LoginHelpPage.reset_btn)
        return ActionChains(self.driver).move_to_element(button).click(button).perform()

    def getCheckEmailBanner(self):
        return self.driver.find_element(*LoginHelpPage.check_email_banner).text

