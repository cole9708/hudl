import requests
import pytest
from utilities.payloads import PayLoads
from tests.conftest import getConfigAPI

apiUrl = getConfigAPI()['API']['url']
headers = {"Content-Type": "application/json"}


def test_correctlogin():
    payload = PayLoads().successful_payload()
    login_response = requests.post(apiUrl, json=payload, headers=headers, )
    expected_response = {'success': True, 'forward': '/welcome/320073?forward=&isLogin=True', 'firstName': 'Chris',
                         'error': None}
    assert login_response.status_code == 200
    assert login_response.json() == expected_response
    print('api logged in')


def test_incorrect_login():
    payload = PayLoads().unsuccessful_payload()
    login_response = requests.post(apiUrl, json=payload, headers=headers, )
    expected_response = {"success": 'false', "forward": 'null', "firstName": 'null', "error": 1}
    assert login_response.status_code == 200
    assert login_response.json() != expected_response
    print('api not logged in')

