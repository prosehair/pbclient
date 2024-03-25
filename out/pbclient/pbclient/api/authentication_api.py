# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 2.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from pbclient.models.o_auth_token import OAuthToken

from pbclient.api_client import ApiClient, RequestSerialized
from pbclient.api_response import ApiResponse
from pbclient.rest import RESTResponseType


class AuthenticationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def oauth_token(
        self,
        authorization: Annotated[StrictStr, Field(description="Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value>")],
        content_type: Annotated[Optional[StrictStr], Field(description="This mentions the content type getting passed in body of request.")] = None,
        grant_type: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> OAuthToken:
        """OAuth Authentication

        This API call generates the OAuth token based on the Base64-encoded value of the API key and secret associated with your PB Shipping APIs developer account. The token expires after 10 hours, after which you must create a new one.

        :param authorization: Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value> (required)
        :type authorization: str
        :param content_type: This mentions the content type getting passed in body of request.
        :type content_type: str
        :param grant_type:
        :type grant_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._oauth_token_serialize(
            authorization=authorization,
            content_type=content_type,
            grant_type=grant_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OAuthToken",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def oauth_token_with_http_info(
        self,
        authorization: Annotated[StrictStr, Field(description="Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value>")],
        content_type: Annotated[Optional[StrictStr], Field(description="This mentions the content type getting passed in body of request.")] = None,
        grant_type: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[OAuthToken]:
        """OAuth Authentication

        This API call generates the OAuth token based on the Base64-encoded value of the API key and secret associated with your PB Shipping APIs developer account. The token expires after 10 hours, after which you must create a new one.

        :param authorization: Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value> (required)
        :type authorization: str
        :param content_type: This mentions the content type getting passed in body of request.
        :type content_type: str
        :param grant_type:
        :type grant_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._oauth_token_serialize(
            authorization=authorization,
            content_type=content_type,
            grant_type=grant_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OAuthToken",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def oauth_token_without_preload_content(
        self,
        authorization: Annotated[StrictStr, Field(description="Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value>")],
        content_type: Annotated[Optional[StrictStr], Field(description="This mentions the content type getting passed in body of request.")] = None,
        grant_type: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """OAuth Authentication

        This API call generates the OAuth token based on the Base64-encoded value of the API key and secret associated with your PB Shipping APIs developer account. The token expires after 10 hours, after which you must create a new one.

        :param authorization: Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value> (required)
        :type authorization: str
        :param content_type: This mentions the content type getting passed in body of request.
        :type content_type: str
        :param grant_type:
        :type grant_type: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._oauth_token_serialize(
            authorization=authorization,
            content_type=content_type,
            grant_type=grant_type,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OAuthToken",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _oauth_token_serialize(
        self,
        authorization,
        content_type,
        grant_type,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if content_type is not None:
            _header_params['Content-Type'] = content_type
        if authorization is not None:
            _header_params['Authorization'] = authorization
        # process the form parameters
        if grant_type is not None:
            _form_params.append(('grant_type', grant_type))
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/x-www-form-urlencoded'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/oauth/token',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


