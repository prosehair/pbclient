# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.12
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ParcelProtectionPolicyResponseContentInnerPolicyDetails(BaseModel):
    """
    ParcelProtectionPolicyResponseContentInnerPolicyDetails
    """
    policy_id: Optional[StrictStr] = Field(None, alias="policyId")
    policy_date: Optional[StrictStr] = Field(None, alias="policyDate")
    policy_status: Optional[StrictStr] = Field(None, alias="policyStatus")
    claim_status: Optional[StrictStr] = Field(None, alias="claimStatus")
    claim_status_update_date: Optional[StrictStr] = Field(None, alias="claimStatusUpdateDate")
    value_of_goods: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueOfGoods")
    insurance_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="insuranceValue")
    premium_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="premiumValue")
    base_premium: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="basePremium")
    technology_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="technologyFee")
    currency_code: Optional[StrictStr] = Field(None, alias="currencyCode")
    mail_class: Optional[StrictStr] = Field(None, alias="mailClass")
    mail_class_option: Optional[StrictStr] = Field(None, alias="mailClassOption")
    __properties = ["policyId", "policyDate", "policyStatus", "claimStatus", "claimStatusUpdateDate", "valueOfGoods", "insuranceValue", "premiumValue", "basePremium", "technologyFee", "currencyCode", "mailClass", "mailClassOption"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ParcelProtectionPolicyResponseContentInnerPolicyDetails:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerPolicyDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if claim_status (nullable) is None
        # and __fields_set__ contains the field
        if self.claim_status is None and "claim_status" in self.__fields_set__:
            _dict['claimStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionPolicyResponseContentInnerPolicyDetails:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerPolicyDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionPolicyResponseContentInnerPolicyDetails.parse_obj(obj)

        _obj = ParcelProtectionPolicyResponseContentInnerPolicyDetails.parse_obj({
            "policy_id": obj.get("policyId"),
            "policy_date": obj.get("policyDate"),
            "policy_status": obj.get("policyStatus"),
            "claim_status": obj.get("claimStatus"),
            "claim_status_update_date": obj.get("claimStatusUpdateDate"),
            "value_of_goods": obj.get("valueOfGoods"),
            "insurance_value": obj.get("insuranceValue"),
            "premium_value": obj.get("premiumValue"),
            "base_premium": obj.get("basePremium"),
            "technology_fee": obj.get("technologyFee"),
            "currency_code": obj.get("currencyCode"),
            "mail_class": obj.get("mailClass"),
            "mail_class_option": obj.get("mailClassOption")
        })
        return _obj


