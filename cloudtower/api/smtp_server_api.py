# coding: utf-8
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudtower.api_client import ApiClient
from cloudtower.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SmtpServerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_smtp_servers(self, get_smtp_servers_request_body, **kwargs):  # noqa: E501
        """get_smtp_servers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_smtp_servers(get_smtp_servers_request_body, async_req=True)
        >>> result = thread.get()

        :param get_smtp_servers_request_body: (required)
        :type get_smtp_servers_request_body: GetSmtpServersRequestBody
        :param content_language:
        :type content_language: ContentLanguage
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[SmtpServer]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_smtp_servers_with_http_info(get_smtp_servers_request_body, **kwargs)  # noqa: E501

    def get_smtp_servers_with_http_info(self, get_smtp_servers_request_body, **kwargs):  # noqa: E501
        """get_smtp_servers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_smtp_servers_with_http_info(get_smtp_servers_request_body, async_req=True)
        >>> result = thread.get()

        :param get_smtp_servers_request_body: (required)
        :type get_smtp_servers_request_body: GetSmtpServersRequestBody
        :param content_language:
        :type content_language: ContentLanguage
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[SmtpServer], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_smtp_servers_request_body',
            'content_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_smtp_servers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_smtp_servers_request_body' is set
        if self.api_client.client_side_validation and ('get_smtp_servers_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_smtp_servers_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_smtp_servers_request_body` when calling `get_smtp_servers`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_smtp_servers_request_body' in local_var_params:
            body_params = local_var_params['get_smtp_servers_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "list[SmtpServer]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-smtp-servers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_smtp_servers_connection(self, get_smtp_servers_connection_request_body, **kwargs):  # noqa: E501
        """get_smtp_servers_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_smtp_servers_connection(get_smtp_servers_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_smtp_servers_connection_request_body: (required)
        :type get_smtp_servers_connection_request_body: GetSmtpServersConnectionRequestBody
        :param content_language:
        :type content_language: ContentLanguage
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SmtpServerConnection
        """
        kwargs['_return_http_data_only'] = True
        return self.get_smtp_servers_connection_with_http_info(get_smtp_servers_connection_request_body, **kwargs)  # noqa: E501

    def get_smtp_servers_connection_with_http_info(self, get_smtp_servers_connection_request_body, **kwargs):  # noqa: E501
        """get_smtp_servers_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_smtp_servers_connection_with_http_info(get_smtp_servers_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_smtp_servers_connection_request_body: (required)
        :type get_smtp_servers_connection_request_body: GetSmtpServersConnectionRequestBody
        :param content_language:
        :type content_language: ContentLanguage
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SmtpServerConnection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_smtp_servers_connection_request_body',
            'content_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_smtp_servers_connection" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_smtp_servers_connection_request_body' is set
        if self.api_client.client_side_validation and ('get_smtp_servers_connection_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_smtp_servers_connection_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_smtp_servers_connection_request_body` when calling `get_smtp_servers_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_smtp_servers_connection_request_body' in local_var_params:
            body_params = local_var_params['get_smtp_servers_connection_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "SmtpServerConnection",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-smtp-servers-connection', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
