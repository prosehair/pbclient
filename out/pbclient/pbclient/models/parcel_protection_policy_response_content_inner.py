# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from pbclient.models.parcel_protection_policy_response_content_inner_policy_details import ParcelProtectionPolicyResponseContentInnerPolicyDetails
from pbclient.models.parcel_protection_policy_response_content_inner_shipment_details import ParcelProtectionPolicyResponseContentInnerShipmentDetails
from pbclient.models.parcel_protection_policy_response_content_inner_shipper_info import ParcelProtectionPolicyResponseContentInnerShipperInfo

class ParcelProtectionPolicyResponseContentInner(BaseModel):
    """
    ParcelProtectionPolicyResponseContentInner
    """
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionId")
    developer_id: Optional[StrictStr] = Field(None, alias="developerId")
    subscription_acc_no: Optional[StrictStr] = Field(None, alias="subscriptionAccNo")
    client_transaction_id: Optional[StrictStr] = Field(None, alias="clientTransactionId")
    policy_details: Optional[ParcelProtectionPolicyResponseContentInnerPolicyDetails] = Field(None, alias="policyDetails")
    shipment_details: Optional[ParcelProtectionPolicyResponseContentInnerShipmentDetails] = Field(None, alias="shipmentDetails")
    shipper_info: Optional[ParcelProtectionPolicyResponseContentInnerShipperInfo] = Field(None, alias="shipperInfo")
    consignee_info: Optional[ParcelProtectionPolicyResponseContentInnerShipperInfo] = Field(None, alias="consigneeInfo")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt")
    __properties = ["transactionId", "developerId", "subscriptionAccNo", "clientTransactionId", "policyDetails", "shipmentDetails", "shipperInfo", "consigneeInfo", "createdAt", "updatedAt"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ParcelProtectionPolicyResponseContentInner:
        """Create an instance of ParcelProtectionPolicyResponseContentInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of policy_details
        if self.policy_details:
            _dict['policyDetails'] = self.policy_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_details
        if self.shipment_details:
            _dict['shipmentDetails'] = self.shipment_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipper_info
        if self.shipper_info:
            _dict['shipperInfo'] = self.shipper_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consignee_info
        if self.consignee_info:
            _dict['consigneeInfo'] = self.consignee_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionPolicyResponseContentInner:
        """Create an instance of ParcelProtectionPolicyResponseContentInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParcelProtectionPolicyResponseContentInner.parse_obj(obj)

        _obj = ParcelProtectionPolicyResponseContentInner.parse_obj({
            "transaction_id": obj.get("transactionId"),
            "developer_id": obj.get("developerId"),
            "subscription_acc_no": obj.get("subscriptionAccNo"),
            "client_transaction_id": obj.get("clientTransactionId"),
            "policy_details": ParcelProtectionPolicyResponseContentInnerPolicyDetails.from_dict(obj.get("policyDetails")) if obj.get("policyDetails") is not None else None,
            "shipment_details": ParcelProtectionPolicyResponseContentInnerShipmentDetails.from_dict(obj.get("shipmentDetails")) if obj.get("shipmentDetails") is not None else None,
            "shipper_info": ParcelProtectionPolicyResponseContentInnerShipperInfo.from_dict(obj.get("shipperInfo")) if obj.get("shipperInfo") is not None else None,
            "consignee_info": ParcelProtectionPolicyResponseContentInnerShipperInfo.from_dict(obj.get("consigneeInfo")) if obj.get("consigneeInfo") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

