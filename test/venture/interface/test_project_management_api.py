# coding: utf-8

"""
    crush 项目方平台（venture）相关接口

    crush 项目方相关的后段（staff）接口和（tenant）交易所接口  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: api@crush.team
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pytest
import json
import swagger_client.venture
from swagger_client.venture.api.project_management_api import ProjectManagementApi  # noqa: E501
from swagger_client.venture.rest import ApiException
from conftest import verify, login, logout, register, BACK_DOOR_VERIFY_CODE, rand_password, rand_email, rand_phone, rand_indiv_cert

api = swagger_client.venture.api.project_management_api.ProjectManagementApi()


def pytest_namespace():
    return {'email': "", "password": "", "base_token": "", "phone": ""}


class TestProjectManagementApi:
    """ProjectManagementApi pytest stubs"""

    def test_register_and_login_prepare(self):
        country = "86"
        pytest.email = rand_email()
        pytest.password = rand_password()
        register(email=pytest.email, password=pytest.password, promotion_code="",
                 verification_code=BACK_DOOR_VERIFY_CODE,
                 country=country)

        pytest.base_token = login(api, pytest.email, pytest.password, challenge="", seccode=BACK_DOOR_VERIFY_CODE,
                                  validate="")
        print("register return base_token:%s" % pytest.base_token)

    def test_get_project_market_list(self):
        """Test case for get_project_market_list
        获取项目币的交易市场列表  # noqa: E501
        """
        api.get_project_market_list(coin_id="")

    def test_projects_id_contacts_get(self):
        """Test case for projects_id_contacts_get
        获取对接交易所列表  # noqa: E501
        """
        api.projects_id_contacts_get(id="", sponsor="")

    def test_projects_id_exchanges_get(self):
        """Test case for projects_id_exchanges_get
        获取项目未对接的交易所列表  # noqa: E501
        """
        api.projects_id_exchanges_get(id="")
