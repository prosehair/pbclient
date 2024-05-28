# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.13
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from pbclient.models.shipment import Shipment

from pbclient.api_client import ApiClient
from pbclient.api_response import ApiResponse
from pbclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RateParcelsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def rate_parcel(self, shipment : Annotated[Shipment, Field(..., description="Shipment request for Rates")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, x_pb_shipper_rate_plan : Annotated[Optional[StrictStr], Field(description="USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq)")] = None, x_pb_integrator_carrier_id : Annotated[Optional[StrictStr], Field(description="USPS Only. Negotiated services rate, if applicable.")] = None, x_pb_shipper_carrier_account_id : Annotated[Optional[StrictStr], Field(description="UPS (United Parcel Service) Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account](https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) API.")] = None, include_delivery_commitment : Annotated[Optional[StrictBool], Field(description="When set to true, returns estimated transit time in days.")] = None, carrier : Annotated[Optional[StrictStr], Field(description="Cross-Border only. Required for PB Cross-Border. Set this to PBI.")] = None, **kwargs) -> Shipment:  # noqa: E501
        """Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.rate_parcel(shipment, x_pb_unified_error_structure, x_pb_shipper_rate_plan, x_pb_integrator_carrier_id, x_pb_shipper_carrier_account_id, include_delivery_commitment, carrier, async_req=True)
        >>> result = thread.get()

        :param shipment: Shipment request for Rates (required)
        :type shipment: Shipment
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
        :param x_pb_shipper_rate_plan: USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq)
        :type x_pb_shipper_rate_plan: str
        :param x_pb_integrator_carrier_id: USPS Only. Negotiated services rate, if applicable.
        :type x_pb_integrator_carrier_id: str
        :param x_pb_shipper_carrier_account_id: UPS (United Parcel Service) Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account](https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) API.
        :type x_pb_shipper_carrier_account_id: str
        :param include_delivery_commitment: When set to true, returns estimated transit time in days.
        :type include_delivery_commitment: bool
        :param carrier: Cross-Border only. Required for PB Cross-Border. Set this to PBI.
        :type carrier: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Shipment
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the rate_parcel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.rate_parcel_with_http_info(shipment, x_pb_unified_error_structure, x_pb_shipper_rate_plan, x_pb_integrator_carrier_id, x_pb_shipper_carrier_account_id, include_delivery_commitment, carrier, **kwargs)  # noqa: E501

    @validate_arguments
    def rate_parcel_with_http_info(self, shipment : Annotated[Shipment, Field(..., description="Shipment request for Rates")], x_pb_unified_error_structure : Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None, x_pb_shipper_rate_plan : Annotated[Optional[StrictStr], Field(description="USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq)")] = None, x_pb_integrator_carrier_id : Annotated[Optional[StrictStr], Field(description="USPS Only. Negotiated services rate, if applicable.")] = None, x_pb_shipper_carrier_account_id : Annotated[Optional[StrictStr], Field(description="UPS (United Parcel Service) Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account](https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) API.")] = None, include_delivery_commitment : Annotated[Optional[StrictBool], Field(description="When set to true, returns estimated transit time in days.")] = None, carrier : Annotated[Optional[StrictStr], Field(description="Cross-Border only. Required for PB Cross-Border. Set this to PBI.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.rate_parcel_with_http_info(shipment, x_pb_unified_error_structure, x_pb_shipper_rate_plan, x_pb_integrator_carrier_id, x_pb_shipper_carrier_account_id, include_delivery_commitment, carrier, async_req=True)
        >>> result = thread.get()

        :param shipment: Shipment request for Rates (required)
        :type shipment: Shipment
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
        :param x_pb_shipper_rate_plan: USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq)
        :type x_pb_shipper_rate_plan: str
        :param x_pb_integrator_carrier_id: USPS Only. Negotiated services rate, if applicable.
        :type x_pb_integrator_carrier_id: str
        :param x_pb_shipper_carrier_account_id: UPS (United Parcel Service) Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account](https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) API.
        :type x_pb_shipper_carrier_account_id: str
        :param include_delivery_commitment: When set to true, returns estimated transit time in days.
        :type include_delivery_commitment: bool
        :param carrier: Cross-Border only. Required for PB Cross-Border. Set this to PBI.
        :type carrier: str
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
        :rtype: tuple(Shipment, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'shipment',
            'x_pb_unified_error_structure',
            'x_pb_shipper_rate_plan',
            'x_pb_integrator_carrier_id',
            'x_pb_shipper_carrier_account_id',
            'include_delivery_commitment',
            'carrier'
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
                    " to method rate_parcel" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('include_delivery_commitment') is not None:  # noqa: E501
            _query_params.append(('includeDeliveryCommitment', _params['include_delivery_commitment']))

        if _params.get('carrier') is not None:  # noqa: E501
            _query_params.append(('carrier', _params['carrier']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_pb_unified_error_structure']:
            _header_params['X-PB-UnifiedErrorStructure'] = _params['x_pb_unified_error_structure']

        if _params['x_pb_shipper_rate_plan']:
            _header_params['X-PB-Shipper-Rate-Plan'] = _params['x_pb_shipper_rate_plan']

        if _params['x_pb_integrator_carrier_id']:
            _header_params['X-PB-Integrator-CarrierId'] = _params['x_pb_integrator_carrier_id']

        if _params['x_pb_shipper_carrier_account_id']:
            _header_params['X-PB-Shipper-Carrier-AccountId'] = _params['x_pb_shipper_carrier_account_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['shipment'] is not None:
            _body_params = _params['shipment']

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
            '200': "Shipment",
        }

        return self.api_client.call_api(
            '/shippingservices/v1/rates', 'POST',
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
