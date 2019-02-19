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
from swagger_client.venture.api.contacts_api import ContactsApi  # noqa: E501
from swagger_client.venture.rest import ApiException
from conftest import verify, login, logout, register, BACK_DOOR_VERIFY_CODE, rand_password, rand_email, rand_phone, \
    rand_indiv_cert

api = swagger_client.venture.api.contacts_api.ContactsApi()


def pytest_namespace():
    return {'email': "", "password": "", "base_token": "", "phone": ""}


class TestContactsApi:
    """ContactsApi pytest stubs"""

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

    def test_contacts_check_get(self):
        """Test case for contacts_check_get
        判断项目与交易所是否已经申请对接  # noqa: E501
        """
        api.contacts_check_get(project_id='', exchange_id='')

    def test_contacts_invite_number_get(self):
        """Test case for contacts_invite_number_get
        获取项目未处理的邀请记录数量  # noqa: E501
        """
        api.contacts_invite_number_get(id='')

    def test_contacts_post(self):
        """Test case for contacts_post
        申请对接  # noqa: E501
        """
        payload = {

            "exchange_id": 1,
            "project_id": 1,
            "sponsor": "tenant"
        }
        api.contacts_post(body=payload)

    def test_contacts_put(self):
        """Test case for contacts_put
        处理对接邀请  # noqa: E501
        """
        payload = {
            "contactId": 1,
            "status": "accept"
        }
        api.contacts_put(body=payload)
