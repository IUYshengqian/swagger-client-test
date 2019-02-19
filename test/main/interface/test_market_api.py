# coding: utf-8

"""
    crush 平台接口（主平台）

    `crush` 平台接口（主平台）  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: api@crush.team
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pytest
import json
import swagger_client.main
from swagger_client.main.api.market_api import MarketApi  # noqa: E501
from swagger_client.main.rest import ApiException
from conftest import verify, login, logout, register, BACK_DOOR_VERIFY_CODE, rand_password, rand_email, rand_phone, rand_indiv_cert


api = swagger_client.main.api.market_api.MarketApi()


def pytest_namespace():
    return {'email': "", "password": "", "base_token": "", "phone": ""}


class TestMarketApi:
    """MarketApi pytest stubs"""

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

    def test_markets_get(self):
        """Test case for markets_get

        获取交易对市场列表  # noqa: E501
        """
        pass

    def test_markets_trading_coins_get(self):
        """Test case for markets_trading_coins_get

        获取交易币种  # noqa: E501
        """
        pass

