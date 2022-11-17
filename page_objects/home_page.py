import pytest
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    sign_in = (By.CSS_SELECTOR, "a[data-qa-id='login']")
    login_error_banner = (By.CSS_SELECTOR, "p[data-qa-id='error-display']")
    loggedIn_initials = (By.CSS_SELECTOR,"div[class='hui-globaluseritem__display-name']")

    def click_sign_in(self):
        self.driver.find_element(*HomePage.sign_in).click()

    def get_login_error_banner_text(self):
        return self.driver.find_element(*HomePage.login_error_banner).text

    def get_logged_in_intials(self):
        return self.driver.find_element(*HomePage.loggedIn_initials).text
