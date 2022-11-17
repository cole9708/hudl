import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.login_help_page import LoginHelpPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def login(self, getData):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_email_field().send_keys(getData["email"])
        loginPage.get_password_field().send_keys(getData["password"])
        loginPage.click_login_button()
    def verfify_links_exist(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verfify_elements_exist(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((text)))

    def verfify_current_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.url_matches(url))

