# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.5
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from pbclient.models.infectious_substance_contact import InfectiousSubstanceContact
from pbclient.models.radio_activity_detail import RadioActivityDetail
from pbclient.models.radio_nuclide_detail import RadioNuclideDetail
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CommodityInfo(BaseModel):
    """
    CommodityInfo
    """
    cargo_air_craft: Optional[StrictBool] = Field(default=None, alias="cargoAirCraft")
    hazard_class: Optional[StrictStr] = Field(default=None, alias="hazardClass")
    infectious_substance_contact: Optional[InfectiousSubstanceContact] = Field(default=None, alias="infectiousSubstanceContact")
    inner_receptacles_quantity: Optional[StrictInt] = Field(default=None, alias="innerReceptaclesQuantity")
    inner_receptacles_quantity_uom: Optional[StrictStr] = Field(default=None, alias="innerReceptaclesQuantityUOM")
    packaging_group: Optional[StrictStr] = Field(default=None, alias="packagingGroup")
    packaging_instructions: Optional[StrictStr] = Field(default=None, alias="packagingInstructions")
    percentage: Optional[Union[StrictFloat, StrictInt]] = None
    proper_shipping_name: Optional[StrictStr] = Field(default=None, alias="properShippingName")
    quantity: Optional[StrictInt] = None
    quantity_uom: Optional[StrictStr] = Field(default=None, alias="quantityUOM")
    radio_activity_detail: Optional[RadioActivityDetail] = Field(default=None, alias="radioActivityDetail")
    radio_nuclide_detail: Optional[RadioNuclideDetail] = Field(default=None, alias="radioNuclideDetail")
    reportable_quantity: Optional[StrictBool] = Field(default=None, alias="reportableQuantity")
    technical_name: Optional[StrictStr] = Field(default=None, alias="technicalName")
    un_id: Optional[StrictStr] = Field(default=None, alias="unId")
    __properties: ClassVar[List[str]] = ["cargoAirCraft", "hazardClass", "infectiousSubstanceContact", "innerReceptaclesQuantity", "innerReceptaclesQuantityUOM", "packagingGroup", "packagingInstructions", "percentage", "properShippingName", "quantity", "quantityUOM", "radioActivityDetail", "radioNuclideDetail", "reportableQuantity", "technicalName", "unId"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CommodityInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of infectious_substance_contact
        if self.infectious_substance_contact:
            _dict['infectiousSubstanceContact'] = self.infectious_substance_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of radio_activity_detail
        if self.radio_activity_detail:
            _dict['radioActivityDetail'] = self.radio_activity_detail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of radio_nuclide_detail
        if self.radio_nuclide_detail:
            _dict['radioNuclideDetail'] = self.radio_nuclide_detail.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CommodityInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cargoAirCraft": obj.get("cargoAirCraft"),
            "hazardClass": obj.get("hazardClass"),
            "infectiousSubstanceContact": InfectiousSubstanceContact.from_dict(obj.get("infectiousSubstanceContact")) if obj.get("infectiousSubstanceContact") is not None else None,
            "innerReceptaclesQuantity": obj.get("innerReceptaclesQuantity"),
            "innerReceptaclesQuantityUOM": obj.get("innerReceptaclesQuantityUOM"),
            "packagingGroup": obj.get("packagingGroup"),
            "packagingInstructions": obj.get("packagingInstructions"),
            "percentage": obj.get("percentage"),
            "properShippingName": obj.get("properShippingName"),
            "quantity": obj.get("quantity"),
            "quantityUOM": obj.get("quantityUOM"),
            "radioActivityDetail": RadioActivityDetail.from_dict(obj.get("radioActivityDetail")) if obj.get("radioActivityDetail") is not None else None,
            "radioNuclideDetail": RadioNuclideDetail.from_dict(obj.get("radioNuclideDetail")) if obj.get("radioNuclideDetail") is not None else None,
            "reportableQuantity": obj.get("reportableQuantity"),
            "technicalName": obj.get("technicalName"),
            "unId": obj.get("unId")
        })
        return _obj


