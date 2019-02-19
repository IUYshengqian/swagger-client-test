# coding: utf-8

"""
    crush-otc 平台接口（法币交易）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.otc.api_client import ApiClient


class ChatApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def chat_msg_list_get(self, order_id, **kwargs):  # noqa: E501
        """查询历史聊天记录  # noqa: E501

        查询历史聊天记录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_msg_list_get(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: 订单Id (required)
        :param str end_time: 指定查询条件为 消息发送时间在endTime以前（不包括endTime） 国际时间
        :param int size: 指定查询最大多少条记录
        :return: ChatMsgListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_msg_list_get_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_msg_list_get_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def chat_msg_list_get_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """查询历史聊天记录  # noqa: E501

        查询历史聊天记录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_msg_list_get_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: 订单Id (required)
        :param str end_time: 指定查询条件为 消息发送时间在endTime以前（不包括endTime） 国际时间
        :param int size: 指定查询最大多少条记录
        :return: ChatMsgListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'end_time', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_msg_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `chat_msg_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

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
            '/chat/msg-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatMsgListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def chat_new_msg_list_get(self, order_id, **kwargs):  # noqa: E501
        """查询最新聊天记录  # noqa: E501

        查询最新聊天记录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_new_msg_list_get(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: 订单Id (required)
        :param str start_time: 指定查询条件为 消息发送时间在startTime之后(包括startTime) 国际时间
        :param int size: 指定查询最大多少条记录
        :return: ChatMsgListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_new_msg_list_get_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_new_msg_list_get_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def chat_new_msg_list_get_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """查询最新聊天记录  # noqa: E501

        查询最新聊天记录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_new_msg_list_get_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: 订单Id (required)
        :param str start_time: 指定查询条件为 消息发送时间在startTime之后(包括startTime) 国际时间
        :param int size: 指定查询最大多少条记录
        :return: ChatMsgListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'start_time', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_new_msg_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `chat_new_msg_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

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
            '/chat/new-msg-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatMsgListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def chat_send_post(self, body, **kwargs):  # noqa: E501
        """发送消息  # noqa: E501

        发送消息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_send_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendMsgRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chat_send_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.chat_send_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def chat_send_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """发送消息  # noqa: E501

        发送消息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chat_send_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendMsgRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_send_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `chat_send_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/chat/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
