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

from pydantic import Field, StrictBool, StrictStr
from typing import Optional
from typing_extensions import Annotated
from pbclient.models.cancel_pickup200_response import CancelPickup200Response
from pbclient.models.schedule_pickup import SchedulePickup
from pbclient.models.schedule_pickup_response import SchedulePickupResponse

from pbclient.api_client import ApiClient, RequestSerialized
from pbclient.api_response import ApiResponse
from pbclient.rest import RESTResponseType


class PickupApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def cancel_pickup(
        self,
        x_pb_transaction_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        pickup_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        x_pb_unified_error_structure: Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None,
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
    ) -> CancelPickup200Response:
        """Cancel Pickup

        This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

        :param x_pb_transaction_id: A unique identifier for the transaction, up to 25 characters (required)
        :type x_pb_transaction_id: str
        :param pickup_id: A unique identifier for the transaction, up to 25 characters (required)
        :type pickup_id: str
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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

        _param = self._cancel_pickup_serialize(
            x_pb_transaction_id=x_pb_transaction_id,
            pickup_id=pickup_id,
            x_pb_unified_error_structure=x_pb_unified_error_structure,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CancelPickup200Response",
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
    def cancel_pickup_with_http_info(
        self,
        x_pb_transaction_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        pickup_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        x_pb_unified_error_structure: Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None,
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
    ) -> ApiResponse[CancelPickup200Response]:
        """Cancel Pickup

        This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

        :param x_pb_transaction_id: A unique identifier for the transaction, up to 25 characters (required)
        :type x_pb_transaction_id: str
        :param pickup_id: A unique identifier for the transaction, up to 25 characters (required)
        :type pickup_id: str
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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

        _param = self._cancel_pickup_serialize(
            x_pb_transaction_id=x_pb_transaction_id,
            pickup_id=pickup_id,
            x_pb_unified_error_structure=x_pb_unified_error_structure,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CancelPickup200Response",
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
    def cancel_pickup_without_preload_content(
        self,
        x_pb_transaction_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        pickup_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        x_pb_unified_error_structure: Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None,
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
        """Cancel Pickup

        This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

        :param x_pb_transaction_id: A unique identifier for the transaction, up to 25 characters (required)
        :type x_pb_transaction_id: str
        :param pickup_id: A unique identifier for the transaction, up to 25 characters (required)
        :type pickup_id: str
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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

        _param = self._cancel_pickup_serialize(
            x_pb_transaction_id=x_pb_transaction_id,
            pickup_id=pickup_id,
            x_pb_unified_error_structure=x_pb_unified_error_structure,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CancelPickup200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _cancel_pickup_serialize(
        self,
        x_pb_transaction_id,
        pickup_id,
        x_pb_unified_error_structure,
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
        if pickup_id is not None:
            _path_params['pickupId'] = pickup_id
        # process the query parameters
        # process the header parameters
        if x_pb_unified_error_structure is not None:
            _header_params['X-PB-UnifiedErrorStructure'] = x_pb_unified_error_structure
        if x_pb_transaction_id is not None:
            _header_params['X-PB-TransactionId'] = x_pb_transaction_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/shippingservices/v1/pickups/{pickupId}/cancel',
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




    @validate_call
    def get_pickupschedule(
        self,
        x_pb_transaction_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        schedule_pickup: Annotated[SchedulePickup, Field(description="Schedule Pickup request.")],
        x_pb_unified_error_structure: Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None,
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
    ) -> SchedulePickupResponse:
        """Address validation

        This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

        :param x_pb_transaction_id: A unique identifier for the transaction, up to 25 characters (required)
        :type x_pb_transaction_id: str
        :param schedule_pickup: Schedule Pickup request. (required)
        :type schedule_pickup: SchedulePickup
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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

        _param = self._get_pickupschedule_serialize(
            x_pb_transaction_id=x_pb_transaction_id,
            schedule_pickup=schedule_pickup,
            x_pb_unified_error_structure=x_pb_unified_error_structure,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SchedulePickupResponse",
            '405': None,
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
    def get_pickupschedule_with_http_info(
        self,
        x_pb_transaction_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        schedule_pickup: Annotated[SchedulePickup, Field(description="Schedule Pickup request.")],
        x_pb_unified_error_structure: Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None,
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
    ) -> ApiResponse[SchedulePickupResponse]:
        """Address validation

        This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

        :param x_pb_transaction_id: A unique identifier for the transaction, up to 25 characters (required)
        :type x_pb_transaction_id: str
        :param schedule_pickup: Schedule Pickup request. (required)
        :type schedule_pickup: SchedulePickup
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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

        _param = self._get_pickupschedule_serialize(
            x_pb_transaction_id=x_pb_transaction_id,
            schedule_pickup=schedule_pickup,
            x_pb_unified_error_structure=x_pb_unified_error_structure,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SchedulePickupResponse",
            '405': None,
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
    def get_pickupschedule_without_preload_content(
        self,
        x_pb_transaction_id: Annotated[StrictStr, Field(description="A unique identifier for the transaction, up to 25 characters")],
        schedule_pickup: Annotated[SchedulePickup, Field(description="Schedule Pickup request.")],
        x_pb_unified_error_structure: Annotated[Optional[StrictBool], Field(description="Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.")] = None,
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
        """Address validation

        This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

        :param x_pb_transaction_id: A unique identifier for the transaction, up to 25 characters (required)
        :type x_pb_transaction_id: str
        :param schedule_pickup: Schedule Pickup request. (required)
        :type schedule_pickup: SchedulePickup
        :param x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :type x_pb_unified_error_structure: bool
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

        _param = self._get_pickupschedule_serialize(
            x_pb_transaction_id=x_pb_transaction_id,
            schedule_pickup=schedule_pickup,
            x_pb_unified_error_structure=x_pb_unified_error_structure,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SchedulePickupResponse",
            '405': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_pickupschedule_serialize(
        self,
        x_pb_transaction_id,
        schedule_pickup,
        x_pb_unified_error_structure,
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
        if x_pb_unified_error_structure is not None:
            _header_params['X-PB-UnifiedErrorStructure'] = x_pb_unified_error_structure
        if x_pb_transaction_id is not None:
            _header_params['X-PB-TransactionId'] = x_pb_transaction_id
        # process the form parameters
        # process the body parameter
        if schedule_pickup is not None:
            _body_params = schedule_pickup


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
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/shippingservices/v1/pickups/schedule',
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


