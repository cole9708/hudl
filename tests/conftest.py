import configparser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


def getConfigUI():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


def getConfigAPI():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        path = ("/HudlAutomation/chromedriver.exe")
        s = Service(path)
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        print('firefox')
    driver_url = getConfigUI()['WEB']['url']
    driver.get(driver_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
