# -*- coding: utf-8 -*-
# @File :  test_less_entrust.py
# @Author : lh
import random
import time
import pytest
import logging

import swagger_client.main
from swagger_client.main.api.entrust_api import EntrustApi  # NOQA: F401
from swagger_client.main.api.quotation_api import QuotationApi
from swagger_client.main.api.account_api import AccountApi
from swagger_client.tenant.api.quotation_api import QuotationApi as TenantQuotationApi
from swagger_client.venture.api.quotation_api import QuotationApi as VentureQuotationApi
from swagger_client.main.rest import ApiException
from swagger_client.main.models.post_entrusts_request import PostEntrustsRequest
from .profitloss_data import (QUOTATIONS_FIELDS, test_less_entrust_data)

logger = logging.getLogger('test_same_price_volume_deal_success')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

api = swagger_client.main.api.entrust_api.EntrustApi()
main_quota_api = QuotationApi()
main_ac_api = AccountApi()
tenant_quota_api = TenantQuotationApi()
venture_quota_api = VentureQuotationApi()


class TestSamePriceVolumeDealSuccess:
    def teardown_method(self):
        result = api.entrusts_get(status=["entrusting"])
        for i in result.items:
            # logger.error(f"canceling: {i}")
            try:
                api.entrusts_id_cancel_post(i.order_id)
            except Exception as e:
                logger.error(e)

    @pytest.mark.parametrize(QUOTATIONS_FIELDS, test_less_entrust_data)
    def test_same_price_volume_success(self, market_id, price, entrust_type, trade_type,
                                       volume, trigger_price, auto_cancel_at, exchange_ids, coin_id, sell_coin_id,
                                       trading_area_id, symbol, less_entrust_special_login):

        # login
        less_entrust_special_login([api, main_ac_api, main_quota_api, tenant_quota_api, venture_quota_api])
        for i in range(5):
            # price_range = (0.1, 18)
            # volume_range = (1, 10)
            # price = round(random.uniform(*price_range), 2)
            # volume = round(random.uniform(*volume_range), 2)
            coin_id = coin_id
            payload = PostEntrustsRequest()
            payload.market_id = market_id
            payload.price = price
            payload.entrust_type = entrust_type
            payload.trade_type = trade_type
            payload.trigger_price = trigger_price
            payload.volume = volume
            payload.auto_cancel_at = auto_cancel_at
            try:
                first_result = api.entrusts_post(body=payload)
                logger.info(f"{trade_type} id: {first_result.order_id}")
            except Exception as e:
                if e.status == 400:
                    logger.error('下单失败，没钱')
                raise e
            print('第一次下单result:', first_result)
            # 如果first_result的post参数trade_type是'buy'那么就要创建'sell'单
            if trade_type == 'buy':
                buy_id = first_result.order_id
                payload.trade_type = 'sell'
                result = api.entrusts_post(body=payload)
                sell_id = result.order_id
                logger.info(f"sell id :{sell_id}")
            # 如果first_result的post参数trade_type是'sell'那么就要创建'sell'单
            else:
                payload.trade_type = 'buy'
                sell_id = first_result.order_id
                print('*' * 20)
                result = api.entrusts_post(body=payload)
                print('第二次下买单:', result)
                buy_id = result.order_id
                logger.info(f"buy id :{buy_id}")
            result = api.entrusts_get(status=['done'])
            ids = [i.order_id for i in result.items]
            result_sell = api.trades_get(order_id=sell_id)
            logger.info(f"get result sell trades: {result}")
            result_buy = api.trades_get(order_id=buy_id)
            logger.info(f"get result buy trades:  {result}")
            time.sleep(5)
