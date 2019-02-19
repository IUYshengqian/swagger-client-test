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
from swagger_client.main.api.quotation_api import QuotationApi  # noqa: E501
from swagger_client.main.rest import ApiException

api = swagger_client.main.api.quotation_api.QuotationApi()


class TestQuotationApi:
    """QuotationApi pytest stubs"""

    @pytest.mark.parametrize('exchangeids', ['kingli, kingmall, fsjfk'])
    def test_quotations_exchange_get(self, exchangeids):
        """Test case for quotations_exchange_get

        交易所行情信息  # noqa: E501
        """
        api.quotations_exchange_get(exchangeids, async_req=True)
        assert exchangeids == ''

    @pytest.mark.parametrize('exchangeid', ['kingli', ''])
    def test_quotations_get(self, exchangeid):
        """Test case for quotations_get

        首页行情信息展示  # noqa: E501
        """
        api.quotations_exchange_get(exchangeid, async_req=True)

    @pytest.mark.parametrize('body', [])
    def test_quotations_historical_data_get(self, body):
        """Test case for quotations_historical_data_get

        K线数据  # noqa: E501
        """

        api.quotations_historical_data_get(body, async_req=True)

    @pytest.mark.parametrize('projectids', ['jfasdjf', ''])
    def test_quotations_project_get(self, projectids):
        """Test case for quotations_project_get

        项目行情信息  # noqa: E501
        """
        api.quotations_project_get(projectids, async_req=True)
        assert projectids == ''


if __name__ == '__main__':
    pytest.main()
