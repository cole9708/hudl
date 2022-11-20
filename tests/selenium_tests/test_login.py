from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from tests.utilities.BaseClass import BaseClass
from page_objects.login_help_page import LoginHelpPage
from tests.utilities.helper_methods import helperMethods, username, password
from tests import conftest

base_url = conftest.getConfigUI()['WEB']['url']
help_page_url = 'login/help'
check_email_url = 'login/check-email'
logged_out_url = 'en_gb/'


class TestHomePage(BaseClass):

    def test_successful_login(self):
        helperMethods.login(self)

    def test_unsuccessful_login(self):
        helperMethods.unsuccessful_login(self)

    def test_unsuccessful_login_no_password(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_email_field().send_keys(username)
        loginPage.click_login_button()
        self.verify_elements_exist(homePage.login_error_banner)
        assert homePage.get_login_error_banner_text() == "We didn't recognize that email and/or password.Need help?"

    def test_unsuccessful_login_with_no_username(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_password_field().send_keys(password)
        loginPage.click_login_button()
        self.verify_elements_exist(homePage.login_error_banner)
        assert homePage.get_login_error_banner_text() == "We didn't recognize that email and/or password.Need help?"

    def test_password_reset(self):
        helperMethods.unsuccessful_login(self)
        loginPage = LoginPage(self.driver)
        loginHelpPage = LoginHelpPage(self.driver)
        loginPage.click_need_help_link()
        self.verify_current_url(help_page_url)
        assert self.driver.current_url == base_url + help_page_url
        assert loginHelpPage.get_reset_email_field_value() == username
        loginHelpPage.click_reset_button()
        self.verify_current_url(check_email_url)
        assert self.driver.current_url == base_url + check_email_url

    def test_log_out_successfully(self):
        helperMethods.login(self)
        homePage = HomePage(self.driver)
        homePage.click_logged_in_dropdown()
        homePage.select_logout()
        assert self.driver.current_url == base_url + logged_out_url
