import pytest

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from tests.conftest import getConfigAPI
from utilities.BassClass import BaseClass
from page_objects.login_help_page import LoginHelpPage
from utilities.helper_methods import *


class TestHomePage(BaseClass):
    def test_successfull_Login(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()

        loginPage.get_email_field().send_keys(username)
        loginPage.get_password_field().send_keys(password)
        loginPage.click_login_button()
        self.verify_current_url('https://www.hudl.com/home')
        assert self.driver.current_url == 'https://www.hudl.com/home'
        assert homePage.get_logged_in_intials() == 'Chris C'

    def test_unsuccessful_Login(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_email_field().send_keys(username)
        loginPage.get_password_field().send_keys(wrong_password)
        loginPage.click_login_button()
        self.verify_elements_exist(homePage.login_error_banner)
        assert homePage.get_login_error_banner_text()== "We didn't recognize that email and/or password.Need help?"

    def test_unsuccessful_login_no_password(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_email_field().send_keys(username)
        loginPage.click_login_button()
        self.verify_elements_exist(homePage.login_error_banner)
        assert homePage.get_login_error_banner_text()== "We didn't recognize that email and/or password.Need help?", "text does not match"

    def test_unsuccessful_login_with_no_username(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.click_sign_in()
        loginPage.get_password_field().send_keys(password)
        loginPage.click_login_button()
        self.verify_elements_exist(homePage.login_error_banner)
        assert homePage.get_login_error_banner_text() == "We didn't recognize that email and/or password.Need help?"

    def test_password_reset(self):
        self.test_unsuccessful_Login()
        loginPage = LoginPage(self.driver)
        loginHelpPage = LoginHelpPage(self.driver)
        loginPage.click_need_help_link()
        self.verify_current_url('https://www.hudl.com/login/help')
        assert self.driver.current_url == 'https://www.hudl.com/login/help'
        assert loginHelpPage.get_reset_email_field_value() == username
        loginHelpPage.click_reset_button()
        self.verify_current_url('https://www.hudl.com/login/check-email')
        assert self.driver.current_url == 'https://www.hudl.com/login/check-email'
