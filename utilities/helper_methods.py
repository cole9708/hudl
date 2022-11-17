from tests.conftest import getConfigAPI

username = getConfigAPI()['WEB']['username']
password = getConfigAPI()['WEB']['password']
wrong_password =getConfigAPI()['WEB']['wrong_password']