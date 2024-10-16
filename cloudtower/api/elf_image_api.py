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


class ElfImageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_elf_image(self, file, **kwargs):  # noqa: E501
        """create_elf_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_elf_image(file, async_req=True)
        >>> result = thread.get()

        :param file: (required)
        :type file: file
        :param content_language:
        :type content_language: ContentLanguage
        :param cluster_id:
        :type cluster_id: str
        :param name:
        :type name: str
        :param size:
        :type size: str
        :param size_unit:
        :type size_unit: str
        :param description:
        :type description: str
        :param upload_task_id:
        :type upload_task_id: str
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
        :rtype: list[UploadTask]
        """
        kwargs['_return_http_data_only'] = True
        return self.create_elf_image_with_http_info(file, **kwargs)  # noqa: E501

    def create_elf_image_with_http_info(self, file, **kwargs):  # noqa: E501
        """create_elf_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_elf_image_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param file: (required)
        :type file: file
        :param content_language:
        :type content_language: ContentLanguage
        :param cluster_id:
        :type cluster_id: str
        :param name:
        :type name: str
        :param size:
        :type size: str
        :param size_unit:
        :type size_unit: str
        :param description:
        :type description: str
        :param upload_task_id:
        :type upload_task_id: str
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
        :rtype: tuple(list[UploadTask], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'file',
            'content_language',
            'cluster_id',
            'name',
            'size',
            'size_unit',
            'description',
            'upload_task_id'
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
                    " to method create_elf_image" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in local_var_params or  # noqa: E501
                                                        local_var_params['file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `create_elf_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'cluster_id' in local_var_params:
            form_params.append(('cluster_id', local_var_params['cluster_id']))  # noqa: E501
        if 'name' in local_var_params:
            form_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'size' in local_var_params:
            form_params.append(('size', local_var_params['size']))  # noqa: E501
        if 'size_unit' in local_var_params:
            form_params.append(('size_unit', local_var_params['size_unit']))  # noqa: E501
        if 'description' in local_var_params:
            form_params.append(('description', local_var_params['description']))  # noqa: E501
        if 'upload_task_id' in local_var_params:
            form_params.append(('upload_task_id', local_var_params['upload_task_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "list[UploadTask]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/upload-elf-image', 'POST',
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

    def delete_elf_image(self, elf_image_deletion_params, **kwargs):  # noqa: E501
        """delete_elf_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_elf_image(elf_image_deletion_params, async_req=True)
        >>> result = thread.get()

        :param elf_image_deletion_params: (required)
        :type elf_image_deletion_params: ElfImageDeletionParams
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
        :rtype: list[WithTaskDeleteElfImage]
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_elf_image_with_http_info(elf_image_deletion_params, **kwargs)  # noqa: E501

    def delete_elf_image_with_http_info(self, elf_image_deletion_params, **kwargs):  # noqa: E501
        """delete_elf_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_elf_image_with_http_info(elf_image_deletion_params, async_req=True)
        >>> result = thread.get()

        :param elf_image_deletion_params: (required)
        :type elf_image_deletion_params: ElfImageDeletionParams
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
        :rtype: tuple(list[WithTaskDeleteElfImage], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'elf_image_deletion_params',
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
                    " to method delete_elf_image" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'elf_image_deletion_params' is set
        if self.api_client.client_side_validation and ('elf_image_deletion_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['elf_image_deletion_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `elf_image_deletion_params` when calling `delete_elf_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'elf_image_deletion_params' in local_var_params:
            body_params = local_var_params['elf_image_deletion_params']
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
            200: "list[WithTaskDeleteElfImage]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/delete-elf-image', 'POST',
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

    def get_elf_images(self, get_elf_images_request_body, **kwargs):  # noqa: E501
        """get_elf_images  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_elf_images(get_elf_images_request_body, async_req=True)
        >>> result = thread.get()

        :param get_elf_images_request_body: (required)
        :type get_elf_images_request_body: GetElfImagesRequestBody
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
        :rtype: list[ElfImage]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_elf_images_with_http_info(get_elf_images_request_body, **kwargs)  # noqa: E501

    def get_elf_images_with_http_info(self, get_elf_images_request_body, **kwargs):  # noqa: E501
        """get_elf_images  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_elf_images_with_http_info(get_elf_images_request_body, async_req=True)
        >>> result = thread.get()

        :param get_elf_images_request_body: (required)
        :type get_elf_images_request_body: GetElfImagesRequestBody
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
        :rtype: tuple(list[ElfImage], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_elf_images_request_body',
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
                    " to method get_elf_images" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_elf_images_request_body' is set
        if self.api_client.client_side_validation and ('get_elf_images_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_elf_images_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_elf_images_request_body` when calling `get_elf_images`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_elf_images_request_body' in local_var_params:
            body_params = local_var_params['get_elf_images_request_body']
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
            200: "list[ElfImage]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-elf-images', 'POST',
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

    def get_elf_images_connection(self, get_elf_images_connection_request_body, **kwargs):  # noqa: E501
        """get_elf_images_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_elf_images_connection(get_elf_images_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_elf_images_connection_request_body: (required)
        :type get_elf_images_connection_request_body: GetElfImagesConnectionRequestBody
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
        :rtype: ElfImageConnection
        """
        kwargs['_return_http_data_only'] = True
        return self.get_elf_images_connection_with_http_info(get_elf_images_connection_request_body, **kwargs)  # noqa: E501

    def get_elf_images_connection_with_http_info(self, get_elf_images_connection_request_body, **kwargs):  # noqa: E501
        """get_elf_images_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_elf_images_connection_with_http_info(get_elf_images_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_elf_images_connection_request_body: (required)
        :type get_elf_images_connection_request_body: GetElfImagesConnectionRequestBody
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
        :rtype: tuple(ElfImageConnection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_elf_images_connection_request_body',
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
                    " to method get_elf_images_connection" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_elf_images_connection_request_body' is set
        if self.api_client.client_side_validation and ('get_elf_images_connection_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_elf_images_connection_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_elf_images_connection_request_body` when calling `get_elf_images_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_elf_images_connection_request_body' in local_var_params:
            body_params = local_var_params['get_elf_images_connection_request_body']
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
            200: "ElfImageConnection",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-elf-images-connection', 'POST',
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

    def update_elf_image(self, elf_image_updation_params, **kwargs):  # noqa: E501
        """update_elf_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_elf_image(elf_image_updation_params, async_req=True)
        >>> result = thread.get()

        :param elf_image_updation_params: (required)
        :type elf_image_updation_params: ElfImageUpdationParams
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
        :rtype: list[WithTaskElfImage]
        """
        kwargs['_return_http_data_only'] = True
        return self.update_elf_image_with_http_info(elf_image_updation_params, **kwargs)  # noqa: E501

    def update_elf_image_with_http_info(self, elf_image_updation_params, **kwargs):  # noqa: E501
        """update_elf_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_elf_image_with_http_info(elf_image_updation_params, async_req=True)
        >>> result = thread.get()

        :param elf_image_updation_params: (required)
        :type elf_image_updation_params: ElfImageUpdationParams
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
        :rtype: tuple(list[WithTaskElfImage], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'elf_image_updation_params',
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
                    " to method update_elf_image" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'elf_image_updation_params' is set
        if self.api_client.client_side_validation and ('elf_image_updation_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['elf_image_updation_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `elf_image_updation_params` when calling `update_elf_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'elf_image_updation_params' in local_var_params:
            body_params = local_var_params['elf_image_updation_params']
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
            200: "list[WithTaskElfImage]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/update-elf-image', 'POST',
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
