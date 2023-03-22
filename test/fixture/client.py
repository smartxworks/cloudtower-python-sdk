import pytest
from os import path
import json

from cloudtower import ApiClient
from cloudtower.api.user_api import UserApi
from cloudtower.models import LoginInput, UserSource
from cloudtower.configuration import Configuration


@pytest.fixture(scope="session")
def login_info():
    with open(path.abspath(path.join(path.abspath(path.dirname(__file__)), '..', "resource/config.json"))) as config_file:
        config = json.load(config_file)
    config['usersource'] = UserSource.LDAP if config['usersource'] == 'LDAP' else UserSource.LOCAL
    return config


@pytest.fixture(scope="session")
def configuration(login_info):
    return Configuration(
        host=login_info["endpoint"]+"/v2/api"
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
