# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.10
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from pbclient.models.container_manifest_response_data import ContainerManifestResponseData

class ContainerManifestResponse(BaseModel):
    """
    ContainerManifestResponse
    """
    data: Optional[ContainerManifestResponseData] = None
    __properties = ["data"]

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
    def from_json(cls, json_str: str) -> ContainerManifestResponse:
        """Create an instance of ContainerManifestResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContainerManifestResponse:
        """Create an instance of ContainerManifestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContainerManifestResponse.parse_obj(obj)

        _obj = ContainerManifestResponse.parse_obj({
            "data": ContainerManifestResponseData.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        return _obj


