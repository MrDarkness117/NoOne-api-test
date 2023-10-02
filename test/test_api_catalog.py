import os

from pathlib import Path
import pytest
import pytest_reportlog
import requests
import json

from .base._config import APIConfig


class TestCatalog(APIConfig):

    basepath = str(Path.cwd()) + '\\'

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

