import pytest

from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from utilities.BassClass import BaseClass
from PageObjects.login_help_page import LoginHelpPage


@pytest.mark.usefixtures("getData")
class TestHomePage(BaseClass):
    def test_successfull_Login(self, getData):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.clickSignIn()
        loginPage.getEmailField().send_keys(getData["email"])
        loginPage.getPasswordField().send_keys(getData["password"])
        loginPage.clickLoginButton()
        self.verfifyCurrentUrl('https://www.hudl.com/home')
        assert self.driver.current_url == 'https://www.hudl.com/home'
        assert homePage.getLoggedInInitials() == 'Chris C'

    def test_unsuccessful_Login(self, getData):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.clickSignIn()
        loginPage.getEmailField().send_keys(getData["email"])
        loginPage.getPasswordField().send_keys(getData["wrongpassword"])
        loginPage.clickLoginButton()
        self.verfifyElementExists(homePage.login_error_banner)
        assert homePage.getLoginErrorBanner().text == "We didn't recognize that email and/or password.Need help?"

    def test_unsuccessful_login_no_password(self, getData):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.clickSignIn()
        loginPage.getEmailField().send_keys(getData["email"])
        loginPage.clickLoginButton()
        self.verfifyElementExists(homePage.login_error_banner)
        assert homePage.getLoginErrorBanner().text == "We didn't recognize that email and/or password.Need help?", "text does not match"

    def test_unsuccessful_login_with_no_username(self, getData):
        loginHelpPage = LoginHelpPage(self.driver)
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.clickSignIn()
        loginPage.getPasswordField().send_keys(getData["password"])
        loginPage.clickLoginButton()
        self.verfifyElementExists(homePage.login_error_banner)
        assert homePage.getLoginErrorBanner().text == "We didn't recognize that email and/or password.Need help?"

    def test_password_reset(self,getData):
        self.test_unsuccessful_Login(getData)
        loginPage = LoginPage(self.driver)
        loginHelpPage = LoginHelpPage(self.driver)
        loginPage.clickNeedHelpLink()
        self.verfifyCurrentUrl('https://www.hudl.com/login/help')
        assert self.driver.current_url == 'https://www.hudl.com/login/help'
        assert loginHelpPage.getRestEmailFieldValue() == getData['email']
        loginHelpPage.clickResetButton()
        self.verfifyCurrentUrl('https://www.hudl.com/login/check-email')
        assert self.driver.current_url == 'https://www.hudl.com/login/check-email'