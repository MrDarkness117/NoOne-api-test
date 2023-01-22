import os

from pathlib import Path
import pytest
import pytest_reportlog
import requests
import json

from .base._config import APIConfig


class TestCatalog(APIConfig):

    basepath = str(Path.cwd()) + '\\'

    # if os.path.exists(basepath + 'global_params.json'):
    #     with open(basepath + 'global_params.json', 'r') as f:
    #         token_params = json.load(f)
    #         f.close()
    #         print(token_params)
    #     print("Got login params")
    # else:
    #     try:
    #         raise Exception("File doesn't exist, please run auth first!")
    #     except Exception as e:
    #         print("Running Auth")
    #         from .test_api_auth import TestAuth
    #         TestAuth().test_auth()
    #         if not os.path.exists(basepath + 'global_params.json'):
    #             raise Exception("Failed to create global_params.json file, see auth method")
    #         with open("global_params.json", 'r') as f:
    #             token_params = json.load(f)
    #             print(token_params)
    #             f.close()
    #
    #
    # headers = {
    #     "User-Agent": 'PytestAgent',
    #     "Content-Type": 'application/json',
    #     "Connection": 'keep-alive',
    #     "Accept_Encoding": "gzip, enflate, br",
    #     'X-API-Auth': f"Bearer {token_params['accessToken']}"
    # }

    categories = [
        'f', 'm', 'k'
    ]

    @pytest.mark.parametrize('sex', categories)
    @pytest.mark.catalog
    def test_catalog_main(self, sex):
        url_method = 'catalog/main'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        payload = {'sex': sex}
        response = requests.get(self.host_url + url_method, params=payload, headers=headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok'
        assert len(json_response['data']['brands']) != 0

    @pytest.mark.catalog
    def test_catalog_novelty(self):
        url_method = 'catalog/novelty'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        json_response = json.loads(response.text)
        print(len(json_response['data']), "items found.")
        assert response.status_code == 200
        assert json_response['status'] == 'ok'
        assert len(json_response['data']) != 0

