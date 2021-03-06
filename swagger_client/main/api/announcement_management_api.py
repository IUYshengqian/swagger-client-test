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


class AnnouncementManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def exchange_announcements_exchange_id_exchange_get(self, exchange_id, **kwargs):  # noqa: E501
        """获取某一个交易所公告列表  # noqa: E501

        交易所公告列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exchange_announcements_exchange_id_exchange_get(exchange_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str exchange_id: 交易所ID (required)
        :param int page: 页码
        :return: GetAnnouncementsByExchangeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.exchange_announcements_exchange_id_exchange_get_with_http_info(exchange_id, **kwargs)  # noqa: E501
        else:
            (data) = self.exchange_announcements_exchange_id_exchange_get_with_http_info(exchange_id, **kwargs)  # noqa: E501
            return data

    def exchange_announcements_exchange_id_exchange_get_with_http_info(self, exchange_id, **kwargs):  # noqa: E501
        """获取某一个交易所公告列表  # noqa: E501

        交易所公告列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exchange_announcements_exchange_id_exchange_get_with_http_info(exchange_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str exchange_id: 交易所ID (required)
        :param int page: 页码
        :return: GetAnnouncementsByExchangeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exchange_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exchange_announcements_exchange_id_exchange_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'exchange_id' is set
        if ('exchange_id' not in params or
                params['exchange_id'] is None):
            raise ValueError("Missing the required parameter `exchange_id` when calling `exchange_announcements_exchange_id_exchange_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'exchange_id' in params:
            path_params['exchangeId'] = params['exchange_id']  # noqa: E501

        query_params = []
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/exchange-announcements/{exchangeId}/exchange', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAnnouncementsByExchangeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def exchange_announcements_id_get(self, id, **kwargs):  # noqa: E501
        """交易所公告详情  # noqa: E501

        交易所公告详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exchange_announcements_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 公告ID (required)
        :return: GetAnnouncementsExchangeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.exchange_announcements_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.exchange_announcements_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def exchange_announcements_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """交易所公告详情  # noqa: E501

        交易所公告详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exchange_announcements_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 公告ID (required)
        :return: GetAnnouncementsExchangeResponse
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
                    " to method exchange_announcements_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `exchange_announcements_id_get`")  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/exchange-announcements/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAnnouncementsExchangeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def newest_announcements_get(self, ids, type, **kwargs):  # noqa: E501
        """根据项目id/交易所id、类型获取最新公告  # noqa: E501

        根据项目id/交易所id、类型获取最新公告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.newest_announcements_get(ids, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: 项目id/交易所id，字符串拼接（1,2,3） (required)
        :param str type: 类型 exchange 交易所,project 项目; (required)
        :return: GetNewestAnnouncementResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.newest_announcements_get_with_http_info(ids, type, **kwargs)  # noqa: E501
        else:
            (data) = self.newest_announcements_get_with_http_info(ids, type, **kwargs)  # noqa: E501
            return data

    def newest_announcements_get_with_http_info(self, ids, type, **kwargs):  # noqa: E501
        """根据项目id/交易所id、类型获取最新公告  # noqa: E501

        根据项目id/交易所id、类型获取最新公告  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.newest_announcements_get_with_http_info(ids, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: 项目id/交易所id，字符串拼接（1,2,3） (required)
        :param str type: 类型 exchange 交易所,project 项目; (required)
        :return: GetNewestAnnouncementResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method newest_announcements_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `newest_announcements_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `newest_announcements_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/newest-announcements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetNewestAnnouncementResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_announcements_id_get(self, id, **kwargs):  # noqa: E501
        """项目公告详情  # noqa: E501

        项目公告详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_announcements_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: GetProjectAnnouncementInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_announcements_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.project_announcements_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def project_announcements_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """项目公告详情  # noqa: E501

        项目公告详情  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_announcements_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: GetProjectAnnouncementInfoResponse
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
                    " to method project_announcements_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `project_announcements_id_get`")  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project-announcements/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetProjectAnnouncementInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_announcements_project_id_announcement_get(self, project_id, **kwargs):  # noqa: E501
        """项目公告列表  # noqa: E501

        项目公告列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_announcements_project_id_announcement_get(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: 项目id (required)
        :param int page: 页码
        :return: GetProjectAnnouncementListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_announcements_project_id_announcement_get_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.project_announcements_project_id_announcement_get_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def project_announcements_project_id_announcement_get_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """项目公告列表  # noqa: E501

        项目公告列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_announcements_project_id_announcement_get_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: 项目id (required)
        :param int page: 页码
        :return: GetProjectAnnouncementListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method project_announcements_project_id_announcement_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `project_announcements_project_id_announcement_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project-announcements/{projectId}/announcement', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetProjectAnnouncementListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
