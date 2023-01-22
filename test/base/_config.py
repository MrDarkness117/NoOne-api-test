import json
import os
from pathlib import Path
import pytest
import requests


class APIConfig:
    '''
    Configuration class for setting base path and host.
    Runs methods that set up access tokens, includes auth body.
    '''
    basepath = str(Path.cwd()) + '\\'

    token_params = {
        "accessToken": None,
        "refreshToken": None
    }

    host_url = "https://www.noone.ru/rest/v1/"
    auth_body = {
            "deviceType": "android",
            "version": "00958",
            "pushID": "push-me-now-2",
            "login": "m.romantsov@noone.ru",
            "password": "Mihailo117",
            "cityCode": "77000000000",
            "cityTitle": "Москва"
    }

    def setup_function(self):
        print("Running setup.")
        url_method = "auth/login"
        response = requests.post(self.host_url + url_method, json=self.auth_body)
        json_response = json.loads(response.text)
        self.token_params["accessToken"] = json_response['data']['accessToken']
        self.token_params["refreshToken"] = json_response['data']['refreshToken']
        with open(str(os.getcwd()) + 'global_params.json', 'w', encoding='utf-8') as f:
            json.dump(self.token_params, f, indent=4)
            f.close()
        print(f"Saved at: {os.getcwd()}")

    headers = {
        "User-Agent": 'PytestAgent',
        "Content-Type": 'application/json',
        "Connection": 'keep-alive',
        "Accept_Encoding": "gzip, enflate, br",
        'X-API-Auth': f"Bearer {token_params['accessToken']}"
    }