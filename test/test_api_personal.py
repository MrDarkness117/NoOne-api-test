import json
import os
import re
from collections import defaultdict

import requests
import pytest

from pathlib import Path
from .base._config import APIConfig


@pytest.mark.lk
class TestPersonal(APIConfig):
    # basepath = str(Path.cwd()) + '\\'

    @pytest.mark.lk
    def test_api_lk(self):
        url_method = 'lk/personal'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok'
        assert json_response['data']['user']['name']['value'] == 'Михаил'
        assert json_response['data']['user']['surname']['value'] == 'Романцов'
        assert int(re.sub('[^0-9]', '', json_response['data']['user']['phone']['id']['value'])) == 79167163300

    @pytest.mark.lk
    def test_api_lk_loyalty_program(self):
        url_method = 'lk/loyalty-program'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        print(response)
        json_response = json.loads(response.text)
        assert json_response['status'] == 'ok'
        assert response.status_code == 200

    @pytest.mark.lk
    def test_api_lk_password_correct(self):
        url_method = 'lk/password'
        headers = {
            "Authorization": f"Bearer {self.token_params['accessToken']}",
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        put_data = {
            'currentPassword': "Mihailo117",
            'newPassword': "Mihailo117",
            'confirmPassword': "Mihailo117"
        }
        response = requests.put(self.host_url + url_method, headers=headers, data=put_data)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok', json_response

    @pytest.mark.lk
    def test_api_lk_password_new(self):
        url_method = 'lk/password'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        put_data = {
            'currentPassword': "Mihailo117",
            'newPassword': "Mihailo117!",
            'confirmPassword': "Mihailo117"
        }
        response = requests.put(self.host_url + url_method, headers=headers, data=put_data)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok', json_response

    @pytest.mark.lk
    def test_api_lk_password_old(self):
        url_method = 'lk/password'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auяth': f"Bearer {self.token_params['accessToken']}"
        }
        put_data = {
            'currentPassword': "Mihailo117!",
            'newPassword': "Mihailo117",
            'confirmPassword': "Mihailo117"
        }
        response = requests.put(self.host_url + url_method, headers=headers, data=put_data)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok', json_response

    @pytest.mark.lk
    def test_api_lk_password_wrong_current(self):
        url_method = 'lk/password'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        put_data = {
            'currentPassword': "test",
            'newPassword': "Mihailo117",
            'confirmPassword': "Mihailo117"
        }
        response = requests.put(self.host_url + url_method, headers=headers, data=put_data)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'error', json_response
        assert json_response['reason'] == 'wrong_current_password', json_response['reason']

    @pytest.mark.lk
    def test_api_lk_password_wrong_confirm(self):
        url_method = 'lk/password'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        put_data = {
            'currentPassword': "Mihailo117",
            'newPassword': "Mihailo117!",
            'confirmPassword': "test"
        }
        response = requests.put(self.host_url + url_method, headers=headers, data=put_data)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'error', json_response
        assert json_response['reason'] == 'wrong_confirm_password', json_response['reason']

    @pytest.mark.lk
    def test_api_lk_loyalty(self):
        url_method = "lk/loyalty"
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        json_response = json.loads(response.text)
        assert response.status_code == 200
        assert json_response['status'] == 'ok', json_response
        # assert str(json_response['card']['id']) ==

    @pytest.mark.lk
    def test_api_lk_loyalty_program(self):
        url_method = "lk/loyalty-program"
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        json_response = json.loads(response.text)
        print(json_response)
        assert response.status_code == 200
        assert json_response['status'] == 'ok', json_response
        assert json_response['data']['bonuscardId'] != ''
        # assert str(json_response['data']['bonuscardId']) != ''  # TODO: Добавить ID

    @pytest.mark.lk
    def test_api_lk_new_password(self):
        url_method = 'lk/new-password'
        body = {
            'password': 'Mihailo117'
        }
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.put(self.host_url + url_method, headers=headers, json=body)
        # response = requests.put(self.host_url + url_method, headers=self.headers, json=body)
        print(response.text)
        json_response = json.loads(response.text)
        assert response.status_code == 200, json_response
        assert json_response['status'] == 'ok', json_response

    def test_api_lk_bonus_info(self):
        url_method = 'lk/bonus-info'
        headers = {
            "User-Agent": 'PytestAgent',
            "Content-Type": 'application/json',
            "Connection": 'keep-alive',
            "Accept_Encoding": "gzip, enflate, br",
            'X-API-Auth': f"Bearer {self.token_params['accessToken']}"
        }
        response = requests.get(self.host_url + url_method, headers=headers)
        # response = requests.put(self.host_url + url_method, headers=self.headers, json=body)
        print(response.text)
        json_response = json.loads(response.text)
        assert response.status_code == 200, json_response
        assert json_response['status'] == 'ok', json_response
