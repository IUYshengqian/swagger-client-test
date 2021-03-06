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


class AssetManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def asset_mgmt_asset_password_check_post(self, body, **kwargs):  # noqa: E501
        """资金密码校验  # noqa: E501

        资金密码校验  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_asset_password_check_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAssetsPasswordCheckRequest body: (required)
        :return: PostAssetsPasswordCheckResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_mgmt_asset_password_check_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_mgmt_asset_password_check_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def asset_mgmt_asset_password_check_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """资金密码校验  # noqa: E501

        资金密码校验  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_asset_password_check_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAssetsPasswordCheckRequest body: (required)
        :return: PostAssetsPasswordCheckResponse
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
                    " to method asset_mgmt_asset_password_check_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `asset_mgmt_asset_password_check_post`")  # noqa: E501

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
            '/asset-mgmt/asset-password/check', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostAssetsPasswordCheckResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_mgmt_asset_password_get(self, **kwargs):  # noqa: E501
        """查询是否设置资金密码  # noqa: E501

        查询是否设置资金密码  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_asset_password_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAssetPasswordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_mgmt_asset_password_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.asset_mgmt_asset_password_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def asset_mgmt_asset_password_get_with_http_info(self, **kwargs):  # noqa: E501
        """查询是否设置资金密码  # noqa: E501

        查询是否设置资金密码  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_asset_password_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAssetPasswordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_mgmt_asset_password_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/asset-mgmt/asset-password', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAssetPasswordResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_mgmt_asset_password_put(self, body, **kwargs):  # noqa: E501
        """设置资金密码  # noqa: E501

        设置资金密码  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_asset_password_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutAssetsPasswordRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_mgmt_asset_password_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_mgmt_asset_password_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def asset_mgmt_asset_password_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """设置资金密码  # noqa: E501

        设置资金密码  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_asset_password_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutAssetsPasswordRequest body: (required)
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
                    " to method asset_mgmt_asset_password_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `asset_mgmt_asset_password_put`")  # noqa: E501

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
            '/asset-mgmt/asset-password', 'PUT',
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

    def asset_mgmt_assets_coin_id_get(self, coin_id, **kwargs):  # noqa: E501
        """获取币币单个币种资产  # noqa: E501

        获取币币单个币种资产  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_assets_coin_id_get(coin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str coin_id: 币种Id (required)
        :return: GetAssetsByCoinIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_mgmt_assets_coin_id_get_with_http_info(coin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_mgmt_assets_coin_id_get_with_http_info(coin_id, **kwargs)  # noqa: E501
            return data

    def asset_mgmt_assets_coin_id_get_with_http_info(self, coin_id, **kwargs):  # noqa: E501
        """获取币币单个币种资产  # noqa: E501

        获取币币单个币种资产  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_assets_coin_id_get_with_http_info(coin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str coin_id: 币种Id (required)
        :return: GetAssetsByCoinIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_mgmt_assets_coin_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coin_id' is set
        if ('coin_id' not in params or
                params['coin_id'] is None):
            raise ValueError("Missing the required parameter `coin_id` when calling `asset_mgmt_assets_coin_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'coin_id' in params:
            path_params['coinId'] = params['coin_id']  # noqa: E501

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
            '/asset-mgmt/assets/{coinId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAssetsByCoinIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_mgmt_assets_get(self, **kwargs):  # noqa: E501
        """获取币币账户资产  # noqa: E501

        获取币币账户资产  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_assets_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAssetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_mgmt_assets_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.asset_mgmt_assets_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def asset_mgmt_assets_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取币币账户资产  # noqa: E501

        获取币币账户资产  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_mgmt_assets_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAssetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_mgmt_assets_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/asset-mgmt/assets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAssetsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
