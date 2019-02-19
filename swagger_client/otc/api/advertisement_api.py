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


class AdvertisementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def advertise_create_advertise_post(self, body, **kwargs):  # noqa: E501
        """新建广告  # noqa: E501

        新建广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_create_advertise_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAdRequest body: (required)
        :return: CreateAdResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_create_advertise_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_create_advertise_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def advertise_create_advertise_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """新建广告  # noqa: E501

        新建广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_create_advertise_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAdRequest body: (required)
        :return: CreateAdResp
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
                    " to method advertise_create_advertise_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `advertise_create_advertise_post`")  # noqa: E501

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
            '/advertise/create-advertise', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateAdResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def advertise_delete_ad_id_delete(self, ad_id, **kwargs):  # noqa: E501
        """删除广告  # noqa: E501

        删除广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_delete_ad_id_delete(ad_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_delete_ad_id_delete_with_http_info(ad_id, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_delete_ad_id_delete_with_http_info(ad_id, **kwargs)  # noqa: E501
            return data

    def advertise_delete_ad_id_delete_with_http_info(self, ad_id, **kwargs):  # noqa: E501
        """删除广告  # noqa: E501

        删除广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_delete_ad_id_delete_with_http_info(ad_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ad_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method advertise_delete_ad_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ad_id' is set
        if ('ad_id' not in params or
                params['ad_id'] is None):
            raise ValueError("Missing the required parameter `ad_id` when calling `advertise_delete_ad_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ad_id' in params:
            path_params['adId'] = params['ad_id']  # noqa: E501

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
            '/advertise/delete/{adId}', 'DELETE',
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

    def advertise_info_ad_id_get(self, ad_id, **kwargs):  # noqa: E501
        """获取一条广告  # noqa: E501

        获取一条广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_info_ad_id_get(ad_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :return: AdvertisementQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_info_ad_id_get_with_http_info(ad_id, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_info_ad_id_get_with_http_info(ad_id, **kwargs)  # noqa: E501
            return data

    def advertise_info_ad_id_get_with_http_info(self, ad_id, **kwargs):  # noqa: E501
        """获取一条广告  # noqa: E501

        获取一条广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_info_ad_id_get_with_http_info(ad_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :return: AdvertisementQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ad_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method advertise_info_ad_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ad_id' is set
        if ('ad_id' not in params or
                params['ad_id'] is None):
            raise ValueError("Missing the required parameter `ad_id` when calling `advertise_info_ad_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ad_id' in params:
            path_params['adId'] = params['ad_id']  # noqa: E501

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
            '/advertise/info/{adId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdvertisementQueryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def advertise_my_list_get(self, **kwargs):  # noqa: E501
        """查看广告记录  # noqa: E501

        查看广告记录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_my_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: 页数从1开始
        :param int page_size: 页面大小
        :return: AdListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_my_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.advertise_my_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def advertise_my_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """查看广告记录  # noqa: E501

        查看广告记录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_my_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: 页数从1开始
        :param int page_size: 页面大小
        :return: AdListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method advertise_my_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/advertise/my-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def advertise_online_list_get(self, currency_id, type, **kwargs):  # noqa: E501
        """获取在线的广告列表  # noqa: E501

        获取在线的广告列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_online_list_get(currency_id, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency_id: 数字币id (required)
        :param str type: 交易类型 1 买币广告 2 卖币广告 (required)
        :param int page: 页数从1开始
        :param int page_size: 页面大小
        :return: AdListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_online_list_get_with_http_info(currency_id, type, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_online_list_get_with_http_info(currency_id, type, **kwargs)  # noqa: E501
            return data

    def advertise_online_list_get_with_http_info(self, currency_id, type, **kwargs):  # noqa: E501
        """获取在线的广告列表  # noqa: E501

        获取在线的广告列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_online_list_get_with_http_info(currency_id, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency_id: 数字币id (required)
        :param str type: 交易类型 1 买币广告 2 卖币广告 (required)
        :param int page: 页数从1开始
        :param int page_size: 页面大小
        :return: AdListResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_id', 'type', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method advertise_online_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_id' is set
        if ('currency_id' not in params or
                params['currency_id'] is None):
            raise ValueError("Missing the required parameter `currency_id` when calling `advertise_online_list_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `advertise_online_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency_id' in params:
            query_params.append(('currencyId', params['currency_id']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/advertise/online-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdListResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def advertise_put_off_ad_id_post(self, ad_id, **kwargs):  # noqa: E501
        """把广告下线  # noqa: E501

        把广告下线  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_put_off_ad_id_post(ad_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_put_off_ad_id_post_with_http_info(ad_id, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_put_off_ad_id_post_with_http_info(ad_id, **kwargs)  # noqa: E501
            return data

    def advertise_put_off_ad_id_post_with_http_info(self, ad_id, **kwargs):  # noqa: E501
        """把广告下线  # noqa: E501

        把广告下线  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_put_off_ad_id_post_with_http_info(ad_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ad_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method advertise_put_off_ad_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ad_id' is set
        if ('ad_id' not in params or
                params['ad_id'] is None):
            raise ValueError("Missing the required parameter `ad_id` when calling `advertise_put_off_ad_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ad_id' in params:
            path_params['adId'] = params['ad_id']  # noqa: E501

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
            '/advertise/put-off/{adId}', 'POST',
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

    def advertise_put_on_ad_id_amount_post(self, ad_id, amount, **kwargs):  # noqa: E501
        """把广告上架  # noqa: E501

        把广告上架  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_put_on_ad_id_amount_post(ad_id, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :param str amount: 上架数量 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_put_on_ad_id_amount_post_with_http_info(ad_id, amount, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_put_on_ad_id_amount_post_with_http_info(ad_id, amount, **kwargs)  # noqa: E501
            return data

    def advertise_put_on_ad_id_amount_post_with_http_info(self, ad_id, amount, **kwargs):  # noqa: E501
        """把广告上架  # noqa: E501

        把广告上架  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_put_on_ad_id_amount_post_with_http_info(ad_id, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ad_id: 广告id (required)
        :param str amount: 上架数量 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ad_id', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method advertise_put_on_ad_id_amount_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ad_id' is set
        if ('ad_id' not in params or
                params['ad_id'] is None):
            raise ValueError("Missing the required parameter `ad_id` when calling `advertise_put_on_ad_id_amount_post`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in params or
                params['amount'] is None):
            raise ValueError("Missing the required parameter `amount` when calling `advertise_put_on_ad_id_amount_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ad_id' in params:
            path_params['adId'] = params['ad_id']  # noqa: E501
        if 'amount' in params:
            path_params['amount'] = params['amount']  # noqa: E501

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
            '/advertise/put-on/{adId}/{amount}', 'POST',
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

    def advertise_update_put(self, body, **kwargs):  # noqa: E501
        """更新广告  # noqa: E501

        更新广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_update_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateAdvertisementRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.advertise_update_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.advertise_update_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def advertise_update_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """更新广告  # noqa: E501

        更新广告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.advertise_update_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateAdvertisementRequest body: (required)
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
                    " to method advertise_update_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `advertise_update_put`")  # noqa: E501

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
            '/advertise/update', 'PUT',
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