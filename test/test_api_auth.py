import os
import pathlib
import pytest
import pytest_reportlog
import requests
import json
from .base._config import APIConfig


@pytest.mark.auth
@pytest.mark.order("first")
class TestAuth(APIConfig):

    @pytest.mark.auth
    def test_auth(self):
        url_method = "auth/login"
        response = requests.post(self.host_url + url_method, json=self.auth_body)
        json_response = json.loads(response.text)
        print(os.getcwd())
        self.token_params["accessToken"] = json_response['data']['accessToken']
        self.token_params["refreshToken"] = json_response['data']['refreshToken']
        with open(str(os.getcwd()) + '\\global_params.json', 'w', encoding='utf-8') as f:
            json.dump(self.token_params, f, indent=4)
            f.close()
        print(f"Saved at: {os.getcwd()}")
        assert json_response['status'] == 'ok'

    @pytest.mark.auth
    def test_check_site(self):
        url_method = "auth/status"
        response = requests.get(self.host_url + url_method, json=self.auth_body)
        json_response = json.loads(response.text)
        assert json_response['data']['siteClosed'] is False


# if __name__ == '__main__':
#     test_auth()
