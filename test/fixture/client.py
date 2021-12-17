import pytest
from os import path
import json

from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.api.user_api import UserApi
from cloudtower_python_sdk.models import LoginInput, UserSource
from cloudtower_python_sdk.configuration import Configuration


@pytest.fixture(scope="session")
def login_info():
    with open(path.abspath(path.join(path.abspath(path.dirname(__file__)), '..', "resource/config.json"))) as config_file:
        config = json.load(config_file)
    config['usersource'] = UserSource.LDAP if config['usersource'] == 'LDAP' else UserSource.LOCAL
    return config


@pytest.fixture(scope="session")
def configuration():
    return Configuration(
        host="http://api-test.dev-cloudtower.smartx.com/v2/api"
    )


@pytest.fixture(scope="session")
def client(configuration, login_info):
    with ApiClient(configuration) as api_client:
        user_api = UserApi(api_client)
        login_input = LoginInput(
            username=login_info['username'],
            password=login_info['password'],
            source=login_info['usersource']
        )
        login_response = user_api.login(login_input)
        configuration.api_key['Authorization'] = login_response.data.token
        yield api_client
