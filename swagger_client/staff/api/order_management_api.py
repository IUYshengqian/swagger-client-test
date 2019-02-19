# coding: utf-8

"""
    crush-staff 平台接口（职员管理平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.staff.api_client import ApiClient


class OrderManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def orders_details_add_market_id_get(self, id, **kwargs):  # noqa: E501
        """获取新增市场订单详情  # noqa: E501

        获取新增市场订单详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orders_details_add_market_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 订单id (required)
        :return: GetAddMarketOrderDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.orders_details_add_market_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.orders_details_add_market_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def orders_details_add_market_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取新增市场订单详情  # noqa: E501

        获取新增市场订单详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orders_details_add_market_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 订单id (required)
        :return: GetAddMarketOrderDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_details_add_market_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `orders_details_add_market_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/orders/details/add-market/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAddMarketOrderDetailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def orders_details_recharge_market_id_get(self, id, **kwargs):  # noqa: E501
        """获取续费市场订单详情  # noqa: E501

        获取续费市场订单详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orders_details_recharge_market_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 订单id (required)
        :return: GetRechargeMarketOrderDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.orders_details_recharge_market_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.orders_details_recharge_market_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def orders_details_recharge_market_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取续费市场订单详情  # noqa: E501

        获取续费市场订单详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orders_details_recharge_market_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 订单id (required)
        :return: GetRechargeMarketOrderDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_details_recharge_market_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `orders_details_recharge_market_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/orders/details/recharge-market/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRechargeMarketOrderDetailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def orders_orders_get(self, **kwargs):  # noqa: E501
        """获取订单列表  # noqa: E501

        获取订单列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orders_orders_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: 页码
        :param str start_at: 时间起始
        :param str end_at: 时间结束
        :param str account_id: 账户Id
        :param str order_id: 订单编号
        :param str status: 状态
        :param str type: 类型
        :return: GetOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.orders_orders_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.orders_orders_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def orders_orders_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取订单列表  # noqa: E501

        获取订单列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.orders_orders_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: 页码
        :param str start_at: 时间起始
        :param str end_at: 时间结束
        :param str account_id: 账户Id
        :param str order_id: 订单编号
        :param str status: 状态
        :param str type: 类型
        :return: GetOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'start_at', 'end_at', 'account_id', 'order_id', 'status', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_orders_get" % key
                )
            params[key] = val
        del params['kwargs']

        if ('order_id' in params and
                len(params['order_id']) > 64):
            raise ValueError("Invalid value for parameter `order_id` when calling `orders_orders_get`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('startAt', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('endAt', params['end_at']))  # noqa: E501
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/orders/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
