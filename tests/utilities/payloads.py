from tests.conftest import getConfigAPI

class PayLoads:

    def successful_payload(self):
        return {
            "username": getConfigAPI()['API']['username'],
            "password": getConfigAPI()['API']['password']
        }

    def unsuccessful_payload(self):
        return {
        "username": getConfigAPI()['API']['username'],
        "password": getConfigAPI()['API']['badPassword']
    }