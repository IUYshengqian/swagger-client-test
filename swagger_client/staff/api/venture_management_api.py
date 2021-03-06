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


class VentureManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def accounts_ventures_get(self, **kwargs):  # noqa: E501
        """查询项目方用户列表  # noqa: E501

        查询项目方用户列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accounts_ventures_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date created_start_at: 开始创建时间
        :param date created_end_at: 结束创建时间
        :param str venture_id: 项目方id
        :param str email: 邮箱地址
        :param int page: 页码
        :return: GetVenturesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.accounts_ventures_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.accounts_ventures_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def accounts_ventures_get_with_http_info(self, **kwargs):  # noqa: E501
        """查询项目方用户列表  # noqa: E501

        查询项目方用户列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accounts_ventures_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date created_start_at: 开始创建时间
        :param date created_end_at: 结束创建时间
        :param str venture_id: 项目方id
        :param str email: 邮箱地址
        :param int page: 页码
        :return: GetVenturesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_start_at', 'created_end_at', 'venture_id', 'email', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accounts_ventures_get" % key
                )
            params[key] = val
        del params['kwargs']

        if ('email' in params and
                len(params['email']) > 64):
            raise ValueError("Invalid value for parameter `email` when calling `accounts_ventures_get`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_start_at' in params:
            query_params.append(('createdStartAt', params['created_start_at']))  # noqa: E501
        if 'created_end_at' in params:
            query_params.append(('createdEndAt', params['created_end_at']))  # noqa: E501
        if 'venture_id' in params:
            query_params.append(('ventureId', params['venture_id']))  # noqa: E501
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/accounts/ventures', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetVenturesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def accounts_ventures_id_get(self, id, **kwargs):  # noqa: E501
        """获取项目方用户信息  # noqa: E501

        获取项目方用户信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accounts_ventures_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 账户id (required)
        :return: GetVentureResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.accounts_ventures_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.accounts_ventures_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def accounts_ventures_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取项目方用户信息  # noqa: E501

        获取项目方用户信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accounts_ventures_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 账户id (required)
        :return: GetVentureResponse
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
                    " to method accounts_ventures_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `accounts_ventures_id_get`")  # noqa: E501

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
            '/accounts/ventures/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetVentureResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
