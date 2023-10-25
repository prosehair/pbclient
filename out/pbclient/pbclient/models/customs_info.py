# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.4
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from pbclient.models.address import Address
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomsInfo(BaseModel):
    """
    CustomsInfo
    """
    eelpfc: Optional[StrictStr] = Field(default=None, alias="EELPFC")
    blanket_end_date: Optional[StrictStr] = Field(default=None, description="format: YYYY-MM-DD", alias="blanketEndDate")
    blanket_start_date: Optional[StrictStr] = Field(default=None, description="format: YYYY-MM-DD", alias="blanketStartDate")
    certificate_number: Optional[StrictStr] = Field(default=None, alias="certificateNumber")
    comments: Optional[StrictStr] = None
    currency_code: StrictStr = Field(description="ISO-4217", alias="currencyCode")
    customs_declared_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customsDeclaredValue")
    declaration_statement: Optional[StrictStr] = Field(default=None, alias="declarationStatement")
    freight_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="freightCharge")
    from_customs_reference: Optional[StrictStr] = Field(default=None, alias="fromCustomsReference")
    handling_costs: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="handlingCosts")
    importer_customs_reference: Optional[StrictStr] = Field(default=None, alias="importerCustomsReference")
    insured_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="insuredAmount")
    insured_number: Optional[StrictStr] = Field(default=None, alias="insuredNumber")
    invoice_number: Optional[StrictStr] = Field(default=None, alias="invoiceNumber")
    license_number: Optional[StrictStr] = Field(default=None, alias="licenseNumber")
    other_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="otherCharge")
    other_description: Optional[StrictStr] = Field(default=None, alias="otherDescription")
    other_type: Optional[StrictStr] = Field(default=None, alias="otherType")
    packing_costs: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="packingCosts")
    producer_specification: Optional[StrictStr] = Field(default=None, alias="producerSpecification")
    reason_for_export: Optional[StrictStr] = Field(default=None, alias="reasonForExport")
    reason_for_export_explanation: Optional[StrictStr] = Field(default=None, alias="reasonForExportExplanation")
    sdr_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sdrValue")
    shipping_document_type: Optional[StrictStr] = Field(default=None, alias="shippingDocumentType")
    signature_contact: Optional[Address] = Field(default=None, alias="signatureContact")
    terms_of_sale: Optional[StrictStr] = Field(default=None, alias="termsOfSale")
    __properties: ClassVar[List[str]] = ["EELPFC", "blanketEndDate", "blanketStartDate", "certificateNumber", "comments", "currencyCode", "customsDeclaredValue", "declarationStatement", "freightCharge", "fromCustomsReference", "handlingCosts", "importerCustomsReference", "insuredAmount", "insuredNumber", "invoiceNumber", "licenseNumber", "otherCharge", "otherDescription", "otherType", "packingCosts", "producerSpecification", "reasonForExport", "reasonForExportExplanation", "sdrValue", "shippingDocumentType", "signatureContact", "termsOfSale"]

    @field_validator('other_type')
    def other_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('COMMISSIONS', 'DISCOUNTS', 'HANDLING_FEES', 'OTHER', 'ROYALTIES_AND_LICENSE_FEES', 'TAXES'):
            raise ValueError("must be one of enum values ('COMMISSIONS', 'DISCOUNTS', 'HANDLING_FEES', 'OTHER', 'ROYALTIES_AND_LICENSE_FEES', 'TAXES')")
        return value

    @field_validator('producer_specification')
    def producer_specification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MULTIPLE_SPECIFIED', 'SAME', 'SINGLE_SPECIFIED', 'UNKNOWN', 'AVAILABLE_UPON_REQUEST'):
            raise ValueError("must be one of enum values ('MULTIPLE_SPECIFIED', 'SAME', 'SINGLE_SPECIFIED', 'UNKNOWN', 'AVAILABLE_UPON_REQUEST')")
        return value

    @field_validator('reason_for_export')
    def reason_for_export_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('GIFT', 'COMMERCIAL_SAMPLE', 'MERCHANDISE', 'DOCUMENTS', 'RETURNED_GOODS', 'SOLD', 'NOT_SOLD', 'OTHER', 'DANGEROUS_GOOD', 'HUMANITARIAN_GOODS'):
            raise ValueError("must be one of enum values ('GIFT', 'COMMERCIAL_SAMPLE', 'MERCHANDISE', 'DOCUMENTS', 'RETURNED_GOODS', 'SOLD', 'NOT_SOLD', 'OTHER', 'DANGEROUS_GOOD', 'HUMANITARIAN_GOODS')")
        return value

    @field_validator('shipping_document_type')
    def shipping_document_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NAFTA', 'COO'):
            raise ValueError("must be one of enum values ('NAFTA', 'COO')")
        return value

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
        """Create an instance of CustomsInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of signature_contact
        if self.signature_contact:
            _dict['signatureContact'] = self.signature_contact.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CustomsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "EELPFC": obj.get("EELPFC"),
            "blanketEndDate": obj.get("blanketEndDate"),
            "blanketStartDate": obj.get("blanketStartDate"),
            "certificateNumber": obj.get("certificateNumber"),
            "comments": obj.get("comments"),
            "currencyCode": obj.get("currencyCode"),
            "customsDeclaredValue": obj.get("customsDeclaredValue"),
            "declarationStatement": obj.get("declarationStatement"),
            "freightCharge": obj.get("freightCharge"),
            "fromCustomsReference": obj.get("fromCustomsReference"),
            "handlingCosts": obj.get("handlingCosts"),
            "importerCustomsReference": obj.get("importerCustomsReference"),
            "insuredAmount": obj.get("insuredAmount"),
            "insuredNumber": obj.get("insuredNumber"),
            "invoiceNumber": obj.get("invoiceNumber"),
            "licenseNumber": obj.get("licenseNumber"),
            "otherCharge": obj.get("otherCharge"),
            "otherDescription": obj.get("otherDescription"),
            "otherType": obj.get("otherType"),
            "packingCosts": obj.get("packingCosts"),
            "producerSpecification": obj.get("producerSpecification"),
            "reasonForExport": obj.get("reasonForExport"),
            "reasonForExportExplanation": obj.get("reasonForExportExplanation"),
            "sdrValue": obj.get("sdrValue"),
            "shippingDocumentType": obj.get("shippingDocumentType"),
            "signatureContact": Address.from_dict(obj.get("signatureContact")) if obj.get("signatureContact") is not None else None,
            "termsOfSale": obj.get("termsOfSale")
        })
        return _obj


