from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from tests.conftest import getConfigAPI

username = getConfigAPI()['WEB']['username']
password = getConfigAPI()['WEB']['password']
wrong_password = getConfigAPI()['WEB']['wrong_password']
homepage_url = 'https://www.hudl.com/home'


class helperMethods:
    def login(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()

        loginPage.get_email_field().send_keys(username)
        loginPage.get_password_field().send_keys(password)
        loginPage.click_login_button()
        self.verify_current_url(homepage_url)
        assert self.driver.current_url == homepage_url
        assert homePage.get_logged_in_intials() == 'Chris C'

    def unsuccessful_login(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_email_field().send_keys(username)
        loginPage.get_password_field().send_keys(wrong_password)
        loginPage.click_login_button()
        self.verify_elements_exist(homePage.login_error_banner)
        assert homePage.get_login_error_banner_text() == "We didn't recognize that email and/or password.Need help?"

