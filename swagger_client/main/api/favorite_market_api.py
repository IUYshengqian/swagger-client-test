# coding: utf-8

"""
    crush-main 平台接口（主平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.main.api_client import ApiClient


class FavoriteMarketApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def favorites_market_delete(self, id, **kwargs):  # noqa: E501
        """取消收藏市场  # noqa: E501

        取消收藏市场  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 收藏id (required)
        :return: PostFavoriterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.favorites_market_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.favorites_market_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def favorites_market_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """取消收藏市场  # noqa: E501

        取消收藏市场  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 收藏id (required)
        :return: PostFavoriterResponse
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
                    " to method favorites_market_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `favorites_market_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

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
            '/favorites/market', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostFavoriterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def favorites_market_get(self, **kwargs):  # noqa: E501
        """市场收藏列表  # noqa: E501

        市场收藏列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: 页码
        :param str exchange_id: 交易所Id
        :return: GetFavoriterMarketListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.favorites_market_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.favorites_market_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def favorites_market_get_with_http_info(self, **kwargs):  # noqa: E501
        """市场收藏列表  # noqa: E501

        市场收藏列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: 页码
        :param str exchange_id: 交易所Id
        :return: GetFavoriterMarketListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'exchange_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method favorites_market_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'exchange_id' in params:
            query_params.append(('exchangeId', params['exchange_id']))  # noqa: E501

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
            '/favorites/market', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFavoriterMarketListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def favorites_market_is_favorite_get(self, market_id, **kwargs):  # noqa: E501
        """判断是否被收藏市场  # noqa: E501

        判断是否被收藏市场  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_is_favorite_get(market_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market_id: 市场Id (required)
        :return: GetIsFavoriterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.favorites_market_is_favorite_get_with_http_info(market_id, **kwargs)  # noqa: E501
        else:
            (data) = self.favorites_market_is_favorite_get_with_http_info(market_id, **kwargs)  # noqa: E501
            return data

    def favorites_market_is_favorite_get_with_http_info(self, market_id, **kwargs):  # noqa: E501
        """判断是否被收藏市场  # noqa: E501

        判断是否被收藏市场  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_is_favorite_get_with_http_info(market_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str market_id: 市场Id (required)
        :return: GetIsFavoriterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['market_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method favorites_market_is_favorite_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'market_id' is set
        if ('market_id' not in params or
                params['market_id'] is None):
            raise ValueError("Missing the required parameter `market_id` when calling `favorites_market_is_favorite_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'market_id' in params:
            query_params.append(('marketId', params['market_id']))  # noqa: E501

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
            '/favorites/market/is-favorite', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetIsFavoriterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def favorites_market_post(self, body, **kwargs):  # noqa: E501
        """收藏市场  # noqa: E501

        收藏市场  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostTenantFavoriterMarketRequest body: 请求新建消息 (required)
        :return: PostFavoriterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.favorites_market_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.favorites_market_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def favorites_market_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """收藏市场  # noqa: E501

        收藏市场  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.favorites_market_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostTenantFavoriterMarketRequest body: 请求新建消息 (required)
        :return: PostFavoriterResponse
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
                    " to method favorites_market_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `favorites_market_post`")  # noqa: E501

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
            '/favorites/market', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostFavoriterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
