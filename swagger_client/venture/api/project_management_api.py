# coding: utf-8

"""
    crush-venture 平台接口（项目方平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.venture.api_client import ApiClient


class ProjectManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_project_market_list(self, coin_id, **kwargs):  # noqa: E501
        """获取项目币的交易市场列表-邹凌威  # noqa: E501

        获取项目币的交易市场列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_market_list(coin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str coin_id: 币种ID (required)
        :param int page: 页码
        :param str exchange_name: 交易所名称
        :param str order_rule: 排序规则
        :param str order: 升序/降序
        :return: GetMarketsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_market_list_with_http_info(coin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_market_list_with_http_info(coin_id, **kwargs)  # noqa: E501
            return data

    def get_project_market_list_with_http_info(self, coin_id, **kwargs):  # noqa: E501
        """获取项目币的交易市场列表-邹凌威  # noqa: E501

        获取项目币的交易市场列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_market_list_with_http_info(coin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str coin_id: 币种ID (required)
        :param int page: 页码
        :param str exchange_name: 交易所名称
        :param str order_rule: 排序规则
        :param str order: 升序/降序
        :return: GetMarketsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coin_id', 'page', 'exchange_name', 'order_rule', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_market_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coin_id' is set
        if ('coin_id' not in params or
                params['coin_id'] is None):
            raise ValueError("Missing the required parameter `coin_id` when calling `get_project_market_list`")  # noqa: E501

        if ('exchange_name' in params and
                len(params['exchange_name']) > 16):
            raise ValueError("Invalid value for parameter `exchange_name` when calling `get_project_market_list`, length must be less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'coin_id' in params:
            path_params['coinId'] = params['coin_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'exchange_name' in params:
            query_params.append(('exchangeName', params['exchange_name']))  # noqa: E501
        if 'order_rule' in params:
            query_params.append(('orderRule', params['order_rule']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

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
            '/projects/{coinId}/markets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMarketsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_id_contacts_get(self, id, sponsor, **kwargs):  # noqa: E501
        """获取对接交易所列表-邹凌威  # noqa: E501

        获取对接交易所列表（接入交易所邀请列表）  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_id_contacts_get(id, sponsor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 项目ID (required)
        :param str sponsor: 发起方[项目方，交易所，全部] (required)
        :param int page: 页码
        :return: GetContactsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_id_contacts_get_with_http_info(id, sponsor, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_id_contacts_get_with_http_info(id, sponsor, **kwargs)  # noqa: E501
            return data

    def projects_id_contacts_get_with_http_info(self, id, sponsor, **kwargs):  # noqa: E501
        """获取对接交易所列表-邹凌威  # noqa: E501

        获取对接交易所列表（接入交易所邀请列表）  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_id_contacts_get_with_http_info(id, sponsor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 项目ID (required)
        :param str sponsor: 发起方[项目方，交易所，全部] (required)
        :param int page: 页码
        :return: GetContactsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'sponsor', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_id_contacts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `projects_id_contacts_get`")  # noqa: E501
        # verify the required parameter 'sponsor' is set
        if ('sponsor' not in params or
                params['sponsor'] is None):
            raise ValueError("Missing the required parameter `sponsor` when calling `projects_id_contacts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'sponsor' in params:
            query_params.append(('sponsor', params['sponsor']))  # noqa: E501
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
            '/projects/{id}/contacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetContactsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_id_exchanges_get(self, id, **kwargs):  # noqa: E501
        """获取项目未对接的交易所列表-邹凌威  # noqa: E501

        获取项目未对接的交易所列表（申请上交易所）  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_id_exchanges_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 项目ID (required)
        :param int page: 页码
        :param str exchange_name: 交易所名称
        :param str order_rule: 排序规则
        :param str order: 升序/降序
        :return: GetExchangesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_id_exchanges_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_id_exchanges_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def projects_id_exchanges_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取项目未对接的交易所列表-邹凌威  # noqa: E501

        获取项目未对接的交易所列表（申请上交易所）  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_id_exchanges_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 项目ID (required)
        :param int page: 页码
        :param str exchange_name: 交易所名称
        :param str order_rule: 排序规则
        :param str order: 升序/降序
        :return: GetExchangesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'exchange_name', 'order_rule', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_id_exchanges_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `projects_id_exchanges_get`")  # noqa: E501

        if ('exchange_name' in params and
                len(params['exchange_name']) > 16):
            raise ValueError("Invalid value for parameter `exchange_name` when calling `projects_id_exchanges_get`, length must be less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'exchange_name' in params:
            query_params.append(('exchangeName', params['exchange_name']))  # noqa: E501
        if 'order_rule' in params:
            query_params.append(('orderRule', params['order_rule']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

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
            '/projects/{id}/exchanges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetExchangesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
