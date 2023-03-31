# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from pbclient.models.cross_border_quotes_request import CrossBorderQuotesRequest
from pbclient.models.cross_border_quotes_response import CrossBorderQuotesResponse
from pbclient.models.manifest import Manifest
from pbclient.models.parcel_protection_policy_response import ParcelProtectionPolicyResponse

from pbclient.api_client import ApiClient
from pbclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CrossBorderQuotesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_cross_border_quotes(self, cross_border_quotes_request : CrossBorderQuotesRequest, x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, **kwargs) -> CrossBorderQuotesResponse:  # noqa: E501
        """Cross-Border Quotes  # noqa: E501

        This operation provides an estimate of the duties, taxes, and transportation costs for the items in a buyer's online shopping basket. The API calculates how many separate parcels are required to ship the items and estimates costs. The API checks each item's eligibility to clear customs and returns the quote for eligible items. To look for futher info please look into [Cross-Border Quotes](https://shipping.pitneybowes.com/api/post-quotes.html#)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cross_border_quotes(cross_border_quotes_request, x_pb_unified_error_structure, async_req=True)
        >>> result = thread.get()

        :param cross_border_quotes_request: (required)
        :type cross_border_quotes_request: CrossBorderQuotesRequest
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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
        :rtype: CrossBorderQuotesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_cross_border_quotes_with_http_info(cross_border_quotes_request, x_pb_unified_error_structure, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cross_border_quotes_with_http_info(self, cross_border_quotes_request : CrossBorderQuotesRequest, x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, **kwargs):  # noqa: E501
        """Cross-Border Quotes  # noqa: E501

        This operation provides an estimate of the duties, taxes, and transportation costs for the items in a buyer's online shopping basket. The API calculates how many separate parcels are required to ship the items and estimates costs. The API checks each item's eligibility to clear customs and returns the quote for eligible items. To look for futher info please look into [Cross-Border Quotes](https://shipping.pitneybowes.com/api/post-quotes.html#)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cross_border_quotes_with_http_info(cross_border_quotes_request, x_pb_unified_error_structure, async_req=True)
        >>> result = thread.get()

        :param cross_border_quotes_request: (required)
        :type cross_border_quotes_request: CrossBorderQuotesRequest
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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
        :rtype: tuple(CrossBorderQuotesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cross_border_quotes_request',
            'x_pb_unified_error_structure'
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
                    " to method get_cross_border_quotes" % _key
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
        if _params['x_pb_unified_error_structure']:
            _header_params['X-PB-UnifiedErrorStructure'] = _params['x_pb_unified_error_structure']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['cross_border_quotes_request']:
            _body_params = _params['cross_border_quotes_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        _response_types_map = {
            '200': "CrossBorderQuotesResponse",
        }

        return self.api_client.call_api(
            '/shippingservices/v1/crossborder/checkout/quotes', 'POST',
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

    @validate_arguments
    def predicted_hs_code(self, x_pb_transaction_id : Annotated[StrictStr, Field(..., description="Required. A unique identifier for the transaction, up to 25 characters.")], manifest : Annotated[Manifest, Field(..., description="manifest")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, **kwargs) -> ParcelProtectionPolicyResponse:  # noqa: E501
        """Predicts the HS Code for a parcel  # noqa: E501

        This operation predicts the HS Code for a parcel being shipped internationally and gives the level of confidence in the prediction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.predicted_hs_code(x_pb_transaction_id, manifest, x_pb_unified_error_structure, async_req=True)
        >>> result = thread.get()

        :param x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :type x_pb_transaction_id: str
        :param manifest: manifest (required)
        :type manifest: Manifest
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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
        :rtype: ParcelProtectionPolicyResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.predicted_hs_code_with_http_info(x_pb_transaction_id, manifest, x_pb_unified_error_structure, **kwargs)  # noqa: E501

    @validate_arguments
    def predicted_hs_code_with_http_info(self, x_pb_transaction_id : Annotated[StrictStr, Field(..., description="Required. A unique identifier for the transaction, up to 25 characters.")], manifest : Annotated[Manifest, Field(..., description="manifest")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, **kwargs):  # noqa: E501
        """Predicts the HS Code for a parcel  # noqa: E501

        This operation predicts the HS Code for a parcel being shipped internationally and gives the level of confidence in the prediction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.predicted_hs_code_with_http_info(x_pb_transaction_id, manifest, x_pb_unified_error_structure, async_req=True)
        >>> result = thread.get()

        :param x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :type x_pb_transaction_id: str
        :param manifest: manifest (required)
        :type manifest: Manifest
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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
        :rtype: tuple(ParcelProtectionPolicyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'x_pb_transaction_id',
            'manifest',
            'x_pb_unified_error_structure'
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
                    " to method predicted_hs_code" % _key
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
        if _params['x_pb_unified_error_structure']:
            _header_params['X-PB-UnifiedErrorStructure'] = _params['x_pb_unified_error_structure']

        if _params['x_pb_transaction_id']:
            _header_params['X-PB-TransactionId'] = _params['x_pb_transaction_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['manifest']:
            _body_params = _params['manifest']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        _response_types_map = {
            '200': "ParcelProtectionPolicyResponse",
        }

        return self.api_client.call_api(
            '/shippingservices/v1/crossborder/hs-classification/items', 'POST',
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
