import json
import os
import re
from collections import defaultdict

import requests
import pytest

from pathlib import Path
from .base._config import APIConfig


# @pytest.mark.skip
@pytest.mark.favorite
class TestFavorite(APIConfig):

    items = [
        '1682603'
    ]

    @pytest.mark.favorite
    @pytest.mark.parametrize('ids', items)
    def test_api_add_favorite(self, ids):
        url_method = f'favorite/{ids}'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.post(self.host_url + url_method, headers=headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200, json_response
        assert json_response['status'] == 'ok', json_response
        assert json_response['status'] == 'error' and json_response['reason'] == 'already_in_favorite', json_response

    @pytest.mark.favorite
    def test_api_favorite(self):
        url_method = 'favorite'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        # response = requests.get(self.host_url + url_method, headers=self.headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200, json_response
        assert json_response['status'] == 'ok', json_response
        assert len(json_response['data']['models']) > 0, json_response
        assert json_response['data']['models'][0]['id'] != (None or 0 or ''), json_response
        # for i, el in self.ids, json_response['data']['models']:
        #     assert i in json_response['data']['models']
        for n in len(json_response['data']['models']):
            assert json_response['data']['models'][n-1]['id'] == self.items[n-1], json_response

    @pytest.mark.favorite
    @pytest.mark.parametrize('ids', items)
    def test_api_delete_favorite(self, ids):
        url_method = f'favorite/{ids}'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.delete(self.host_url + url_method, headers=headers)
        # response = requests.get(self.host_url + url_method, headers=self.headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200, json_response
        assert json_response['status'] == 'ok', json_response
