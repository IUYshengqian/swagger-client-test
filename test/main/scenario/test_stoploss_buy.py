# -*- coding: utf-8 -*-
# @File :  test_stoploss_buy.py
# @Author : lh
# @time : 18-11-14 下午6:06
import time

import pytest
import logging
from swagger_client.main.api.account_api import AccountApi
from swagger_client.main.api.entrust_api import EntrustApi  # NOQA: F401
from swagger_client.main.models.post_entrusts_request import PostEntrustsRequest
from .profitloss_data import (FIELDS, stoploss_buy, stoploss_buy_fail, get_random_price_and_volume)

main_entrust_api = EntrustApi()
main_ac_api = AccountApi()
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())


# 止损买单
class TestStopLossBuy:
    @pytest.mark.parametrize(FIELDS, stoploss_buy)
    def test_stoploss_buy(self, market_id, price, entrust_type, trade_type,
                           volume, trigger_price, auto_cancel_at, entrust_special_login):
        # login
        special_info = entrust_special_login([main_entrust_api, main_ac_api])
        payload = PostEntrustsRequest()
        payload.price = 1000_00
        payload.entrust_type = 'market'
        payload.trade_type = 'sell'
        # payload.trigger_price = trigger_price
        payload.volume = 100000_00
        # payload.auto_cancel_at = auto_cancel_at
        # login
        payload.market_id = market_id

        # 清空
        main_entrust_api.entrusts_post(body=payload)
        payload.trade_type = 'buy'
        main_entrust_api.entrusts_post(body=payload)

        # 恢复限价
        price, volume = get_random_price_and_volume(special_info['precision'])

        # 构造entrust_post请求对象
        payload = PostEntrustsRequest()
        payload.market_id = market_id
        payload.price = price
        payload.entrust_type = entrust_type
        payload.trade_type = trade_type
        payload.trigger_price = trigger_price
        payload.volume = volume
        payload.auto_cancel_at = auto_cancel_at
        main_ac_info = main_ac_api.accounts_account_info_get()
        print('主平台用户信息:', main_ac_info)
        # 1.先下一买一卖,构造最新成交价
        print('下买卖单价格:', price)
        print('下买卖单数量:', volume)
        first_result = main_entrust_api.entrusts_post(body=payload)
        print('下卖单信息:', first_result)
        time.sleep(1)
        buy1_id = first_result.order_id
        payload.trade_type = 'buy'
        result = main_entrust_api.entrusts_post(body=payload)
        print('下买单信息:', result)
        sell1_id = result.order_id
        # 1.1 检查成交记录列表,委托交易列表
        # entrust_res = main_entrust_api.entrusts_get(status=['done'])
        time.sleep(5)
        entrust_res = main_entrust_api.entrusts_get()
        print('委托交易列表:', entrust_res)
        assert entrust_res.items
        entrust_list = [res.order_id for res in entrust_res.items]
        assert buy1_id in entrust_list
        assert sell1_id in entrust_list
        # 1.2 检查委托交易列表
        trade_res = main_entrust_api.trades_get(order_id=buy1_id)
        assert trade_res.items
        # 获取最新成交价
        new_price = trade_res.items[0].price
        # 2.下委托单(类型:止损 如果当前成交价大于触发价)
        payload.trigger_price = str(float(new_price) - 0.01)
        payload.price = str(float(new_price) - 0.01)
        payload.trade_type = 'buy'
        payload.entrust_type = 'profit_loss'
        tri_price = str(float(new_price) - 0.01)
        commi_price = tri_price
        buy_res = main_entrust_api.entrusts_post(body=payload)
        commission_order_id = buy_res.order_id
        # 3.再下一买一卖,达到触发价
        payload.price = str(float(new_price) - 0.04)
        payload.trade_type = 'buy'
        payload.entrust_type = 'limit'
        payload.trigger_price = None
        buy2_price = str(float(new_price) - 0.04)
        time.sleep(1)
        # 3.1先下一笔买单
        buy2_res = main_entrust_api.entrusts_post(body=payload)
        buy2_id = buy2_res.order_id
        print('buy2_id:', buy2_id)
        # 3.2再下一笔卖单
        payload.price = buy2_price
        payload.trade_type = 'sell'
        payload.entrust_type = 'limit'
        payload.trigger_price = None
        sell2_res = main_entrust_api.entrusts_post(body=payload)
        sell2_id = sell2_res.order_id
        print('sell2_id:', sell2_id)
        # 3.3检查委托交易列表
        # check_res = main_entrust_api.entrusts_get(status=['done'])
        time.sleep(5)
        check_res = main_entrust_api.entrusts_get()
        assert check_res.items
        print('第二次交易成交列表:', check_res)
        check_list = [res.order_id for res in check_res.items]
        assert buy2_id in check_list
        assert sell2_id in check_list
        # 3.4获取成交记录列表
        ch_trade_res = main_entrust_api.trades_get(order_id=buy2_id)
        assert ch_trade_res.items[0]
        latest_price = ch_trade_res.items[0].price
        # 4.当前成交价价变动时,当前价小于等于触发价，开始委托,检查委托列表是否有委托订单记录
        if latest_price <= tri_price:
            order_lists = main_entrust_api.entrusts_get(status=["entrusting"], trade_type='buy')
            assert order_lists.items
            order_list = [order_res.order_id for order_res in order_lists.items]
            assert commission_order_id in order_list
        # 5.下一个与第2步方向相反的单,促成第二步的单成交
        payload.trade_type = 'sell'
        # 委托价>=卖一时,撮合成功
        payload.price = commi_price
        result = main_entrust_api.entrusts_post(body=payload)
        sell_id = result.order_id
        time.sleep(5)
        result = main_entrust_api.trades_get()
        ids = [i.order_id for i in result.items]
        assert sell_id in ids
        assert commission_order_id in ids
        # 6.查看租户平台委托订单列表
        # 6.1 租户平台获取成交记录列表
        # 6.2 租户平台获取手续费记录列表

    @pytest.mark.parametrize(FIELDS, stoploss_buy_fail)
    def test_stoploss_buy_fail(self, market_id, price, entrust_type, trade_type,
                               volume, trigger_price, auto_cancel_at, entrust_special_login):
        # login
        entrust_special_info = entrust_special_login([main_entrust_api])

        payload = PostEntrustsRequest()
        payload.price = 1000_00
        payload.entrust_type = 'market'
        payload.trade_type = 'sell'
        # payload.trigger_price = trigger_price
        payload.volume = 100000_00
        # payload.auto_cancel_at = auto_cancel_at
        # login
        payload.market_id = market_id

        # 清空
        main_entrust_api.entrusts_post(body=payload)
        payload.trade_type = 'buy'
        main_entrust_api.entrusts_post(body=payload)

        # 恢复限价
        price, volume = get_random_price_and_volume(entrust_special_info['precision'])
        # 构造entrust_post请求对象
        payload = PostEntrustsRequest()
        payload.market_id = market_id
        payload.price = price
        payload.entrust_type = entrust_type
        payload.trade_type = trade_type
        payload.trigger_price = trigger_price
        payload.volume = volume
        payload.auto_cancel_at = auto_cancel_at

        # 1.先下一买一卖,构造最新成交价
        first_result = main_entrust_api.entrusts_post(body=payload)
        buy1_id = first_result.order_id
        payload.trade_type = 'buy'
        result = main_entrust_api.entrusts_post(body=payload)
        sell1_id = result.order_id
        # 1.1 检查成交记录列表,委托交易列表
        time.sleep(5)
        # entrust_res = main_entrust_api.entrusts_get(status=['done'])
        entrust_res = main_entrust_api.entrusts_get()
        print('委托交易列表:', entrust_res)
        assert entrust_res.items
        entrust_list = [res.order_id for res in entrust_res.items]
        assert buy1_id in entrust_list
        assert sell1_id in entrust_list
        # 1.2 检查委托交易列表
        trade_res = main_entrust_api.trades_get(order_id=buy1_id)
        assert trade_res.items
        # 获取最新成交价
        new_price = trade_res.items[0].price
        # 2.下委托单(类型:止损 如果当前成交价大于触发价)
        payload.trigger_price = str(float(new_price) - 0.01)
        payload.price = payload.trigger_price
        payload.trade_type = 'buy'
        payload.entrust_type = 'profit_loss'
        tri_price = str(float(new_price) - 0.01)
        commi_price = tri_price
        buy_res = main_entrust_api.entrusts_post(body=payload)
        commission_order_id = buy_res.order_id
        # 3.再下一买一卖,达到触发价
        payload.trade_type = 'buy'
        payload.trigger_price = None
        payload.price = str(float(new_price) - 0.04)
        buy2_price = str(float(new_price) - 0.04)
        payload.entrust_type = 'limit'
        # 3.1先下一笔买单
        buy2_res = main_entrust_api.entrusts_post(body=payload)
        buy2_id = buy2_res.order_id
        # 3.2再下一笔卖单
        payload.trade_type = 'sell'
        payload.price = buy2_price
        sell2_res = main_entrust_api.entrusts_post(body=payload)
        sell2_id = sell2_res.order_id
        # 3.3检查委托交易列表
        time.sleep(5)
        check_res = main_entrust_api.entrusts_get(status=['done'])
        assert check_res.items
        check_list = [res.order_id for res in check_res.items]
        assert buy2_id in check_list
        assert sell2_id in check_list
        # 3.4获取成交记录列表
        ch_trade_res = main_entrust_api.trades_get(order_id=buy2_id)
        assert ch_trade_res.items
        latest_price = ch_trade_res.items[0].price
        # 4.当前成交价价变动时,当前价小于等于触发价，开始委托,检查委托列表是否有委托订单记录
        if round(float(latest_price), 8) <= round(float(tri_price), 8):
            order_lists = main_entrust_api.entrusts_get(status=["entrusting"], trade_type='buy')
            assert order_lists.items
            order_list = [order_res.order_id for order_res in order_lists.items]
            assert commission_order_id in order_list
        # 5.下一个与第2步方向相反的单,促成第二步的单成交
        payload.trade_type = 'sell'
        # 委托价<卖一时,撮合不成功,2步下的止损sell单在委托列表
        payload.price = str(float(commi_price) + 0.01)
        result = main_entrust_api.entrusts_post(body=payload)
        sell_id = result.order_id
        time.sleep(5)
        result = main_entrust_api.trades_get()
        ids = [i.order_id for i in result.items]
        assert sell_id not in ids
        assert commission_order_id not in ids
        result = main_entrust_api.entrusts_get(status=["entrusting"])
        result_list = [i.order_id for i in result.items]
        assert commission_order_id in result_list
