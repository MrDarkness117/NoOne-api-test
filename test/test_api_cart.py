import json
import os
from collections import defaultdict

import requests
import pytest

from pathlib import Path
from .base._config import APIConfig


class TestCart(APIConfig):
    basepath = str(Path.cwd()) + '\\'

    items = [
        '1584486'
    ]

    @pytest.mark.cart
    def test_api_cart(self):
        url_method = 'cart'
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
        # print(self.token_params['accessToken'])
        assert response.status_code == 200
        assert json_response['status'] == 'ok'

    @pytest.mark.cart
    def test_api_cart_stats(self):
        url_method = 'cart/stats'
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
        assert response.status_code == 200
        assert json_response['status'] == 'ok'

    @pytest.mark.skip
    @pytest.mark.spamcart
    def test_api_spam_cart(self):
        url_method = 'cart'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        status = {'success': 0, 'fails': 0, 'code-400': 0, 'code-500': 0, 'unknown': 0}
        for c in range(0, 2000):
            try:
                response = requests.get(self.host_url + url_method, headers=headers)
                # response = requests.get(self.host_url + url_method, headers=self.headers)
            except Exception:
                print(f"Connection error, attempt #{c} retrying.")
                continue
            json_response = json.loads(response.text)
            if json_response['status'] != 'ok' or response.status_code != 200:
                status['fails'] += 1
                print(json_response)
                if response.status_code == 400: status['code-400'] += 1
                elif response.status_code == 500: status['code-500'] += 1
                else: status['unknown'] += 1
            else: status['success'] += 1
        assert status == {'success': 2000, 'fails': 0, 'code-400': 0, 'code-500': 0, 'unknown': 0}

    @pytest.mark.cart
    @pytest.mark.skip
    @pytest.mark.parametrize('ids', items)
    def test_api_cart_add_item(self, ids):
        url_method = f'cart/{ids}'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.post(self.host_url + url_method, headers=headers)
        # response = requests.get(self.host_url + url_method, headers=self.headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok'

