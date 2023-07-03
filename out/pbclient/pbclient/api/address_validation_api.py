# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from pbclient.models.address import Address
from pbclient.models.address_suggestion_response import AddressSuggestionResponse
from pbclient.models.address_verify_suggest import AddressVerifySuggest

from pbclient.api_client import ApiClient
from pbclient.api_response import ApiResponse
from pbclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AddressValidationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def verify_address(self, address : Annotated[Address, Field(..., description="Address object that needs to be validated.")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, minimal_address_validation : Annotated[Optional[StrictBool], Field(description="When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check.")] = None, **kwargs) -> Address:  # noqa: E501
        """Address validation  # noqa: E501

        Address validation verifies and cleanses postal addresses within the United States to help ensure packages are rated accurately and shipments arrive at their final destinations on time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_address(address, x_pb_unified_error_structure, minimal_address_validation, async_req=True)
        >>> result = thread.get()

        :param address: Address object that needs to be validated. (required)
        :type address: Address
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
        :param minimal_address_validation: When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check.
        :type minimal_address_validation: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Address
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the verify_address_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.verify_address_with_http_info(address, x_pb_unified_error_structure, minimal_address_validation, **kwargs)  # noqa: E501

    @validate_arguments
    def verify_address_with_http_info(self, address : Annotated[Address, Field(..., description="Address object that needs to be validated.")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, minimal_address_validation : Annotated[Optional[StrictBool], Field(description="When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Address validation  # noqa: E501

        Address validation verifies and cleanses postal addresses within the United States to help ensure packages are rated accurately and shipments arrive at their final destinations on time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_address_with_http_info(address, x_pb_unified_error_structure, minimal_address_validation, async_req=True)
        >>> result = thread.get()

        :param address: Address object that needs to be validated. (required)
        :type address: Address
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
        :param minimal_address_validation: When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check.
        :type minimal_address_validation: bool
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
        :rtype: tuple(Address, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'address',
            'x_pb_unified_error_structure',
            'minimal_address_validation'
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
                    " to method verify_address" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('minimal_address_validation') is not None:  # noqa: E501
            _query_params.append(('minimalAddressValidation', _params['minimal_address_validation']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_pb_unified_error_structure']:
            _header_params['X-PB-UnifiedErrorStructure'] = _params['x_pb_unified_error_structure']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['address'] is not None:
            _body_params = _params['address']

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
            '200': "Address",
            '405': None,
        }

        return self.api_client.call_api(
            '/shippingservices/v1/addresses/verify', 'POST',
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
    def verify_and_suggest_address(self, return_suggestions : Annotated[StrictStr, Field(..., description="To return suggested addresses, set this to true.")], address_verify_suggest : Annotated[AddressVerifySuggest, Field(..., description="Address object that needs to be validated.")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, **kwargs) -> AddressSuggestionResponse:  # noqa: E501
        """Address Suggestion  # noqa: E501

        This operation returns suggested addresses. Use this if the [Address Validation API](https://shipping.pitneybowes.com/api/post-address-verify.html) call has returned an error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_and_suggest_address(return_suggestions, address_verify_suggest, x_pb_unified_error_structure, async_req=True)
        >>> result = thread.get()

        :param return_suggestions: To return suggested addresses, set this to true. (required)
        :type return_suggestions: str
        :param address_verify_suggest: Address object that needs to be validated. (required)
        :type address_verify_suggest: AddressVerifySuggest
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddressSuggestionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the verify_and_suggest_address_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.verify_and_suggest_address_with_http_info(return_suggestions, address_verify_suggest, x_pb_unified_error_structure, **kwargs)  # noqa: E501

    @validate_arguments
    def verify_and_suggest_address_with_http_info(self, return_suggestions : Annotated[StrictStr, Field(..., description="To return suggested addresses, set this to true.")], address_verify_suggest : Annotated[AddressVerifySuggest, Field(..., description="Address object that needs to be validated.")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Address Suggestion  # noqa: E501

        This operation returns suggested addresses. Use this if the [Address Validation API](https://shipping.pitneybowes.com/api/post-address-verify.html) call has returned an error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_and_suggest_address_with_http_info(return_suggestions, address_verify_suggest, x_pb_unified_error_structure, async_req=True)
        >>> result = thread.get()

        :param return_suggestions: To return suggested addresses, set this to true. (required)
        :type return_suggestions: str
        :param address_verify_suggest: Address object that needs to be validated. (required)
        :type address_verify_suggest: AddressVerifySuggest
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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
        :rtype: tuple(AddressSuggestionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'return_suggestions',
            'address_verify_suggest',
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
                    " to method verify_and_suggest_address" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('return_suggestions') is not None:  # noqa: E501
            _query_params.append(('returnSuggestions', _params['return_suggestions']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_pb_unified_error_structure']:
            _header_params['X-PB-UnifiedErrorStructure'] = _params['x_pb_unified_error_structure']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['address_verify_suggest'] is not None:
            _body_params = _params['address_verify_suggest']

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
            '200': "AddressSuggestionResponse",
            '405': None,
        }

        return self.api_client.call_api(
            '/shippingservices/v1/addresses/verify-suggest', 'POST',
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
