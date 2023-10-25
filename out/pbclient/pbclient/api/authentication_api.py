# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.11
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from pbclient.models.o_auth_token import OAuthToken

from pbclient.api_client import ApiClient
from pbclient.api_response import ApiResponse
from pbclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuthenticationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def oauth_token(self, authorization : Annotated[StrictStr, Field(..., description="Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value>")], content_type : Annotated[Optional[StrictStr], Field(description="This mentions the content type getting passed in body of request.")] = None, grant_type : Optional[StrictStr] = None, **kwargs) -> OAuthToken:  # noqa: E501
        """OAuth Authentication  # noqa: E501

        This API call generates the OAuth token based on the Base64-encoded value of the API key and secret associated with your PB Shipping APIs developer account. The token expires after 10 hours, after which you must create a new one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.oauth_token(authorization, content_type, grant_type, async_req=True)
        >>> result = thread.get()

        :param authorization: Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value> (required)
        :type authorization: str
        :param content_type: This mentions the content type getting passed in body of request.
        :type content_type: str
        :param grant_type:
        :type grant_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: OAuthToken
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the oauth_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.oauth_token_with_http_info(authorization, content_type, grant_type, **kwargs)  # noqa: E501

    @validate_arguments
    def oauth_token_with_http_info(self, authorization : Annotated[StrictStr, Field(..., description="Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value>")], content_type : Annotated[Optional[StrictStr], Field(description="This mentions the content type getting passed in body of request.")] = None, grant_type : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """OAuth Authentication  # noqa: E501

        This API call generates the OAuth token based on the Base64-encoded value of the API key and secret associated with your PB Shipping APIs developer account. The token expires after 10 hours, after which you must create a new one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.oauth_token_with_http_info(authorization, content_type, grant_type, async_req=True)
        >>> result = thread.get()

        :param authorization: Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value> (required)
        :type authorization: str
        :param content_type: This mentions the content type getting passed in body of request.
        :type content_type: str
        :param grant_type:
        :type grant_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
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
        :rtype: tuple(OAuthToken, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization',
            'content_type',
            'grant_type'
        ]
        _all_params.extend(
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

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        if _params['grant_type']:
            _form_params.append(('grant_type', _params['grant_type']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/x-www-form-urlencoded']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "OAuthToken",
        }

        return self.api_client.call_api(
            '/oauth/token', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
