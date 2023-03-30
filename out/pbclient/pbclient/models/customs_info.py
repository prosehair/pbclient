# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
from pydantic import BaseModel, Field, StrictFloat, StrictStr, validator
from pbclient.models.address import Address

class CustomsInfo(BaseModel):
    """
    CustomsInfo
    """
    eelpfc: Optional[StrictStr] = Field(None, alias="EELPFC")
    blanket_end_date: Optional[StrictStr] = Field(None, alias="blanketEndDate", description="format: YYYY-MM-DD")
    blanket_start_date: Optional[StrictStr] = Field(None, alias="blanketStartDate", description="format: YYYY-MM-DD")
    certificate_number: Optional[StrictStr] = Field(None, alias="certificateNumber")
    comments: Optional[StrictStr] = None
    currency_code: StrictStr = Field(..., alias="currencyCode", description="ISO-4217")
    customs_declared_value: Optional[StrictFloat] = Field(None, alias="customsDeclaredValue")
    declaration_statement: Optional[StrictStr] = Field(None, alias="declarationStatement")
    freight_charge: Optional[StrictFloat] = Field(None, alias="freightCharge")
    from_customs_reference: Optional[StrictStr] = Field(None, alias="fromCustomsReference")
    handling_costs: Optional[StrictFloat] = Field(None, alias="handlingCosts")
    importer_customs_reference: Optional[StrictStr] = Field(None, alias="importerCustomsReference")
    insured_amount: Optional[StrictFloat] = Field(None, alias="insuredAmount")
    insured_number: Optional[StrictStr] = Field(None, alias="insuredNumber")
    invoice_number: Optional[StrictStr] = Field(None, alias="invoiceNumber")
    license_number: Optional[StrictStr] = Field(None, alias="licenseNumber")
    other_charge: Optional[StrictFloat] = Field(None, alias="otherCharge")
    other_description: Optional[StrictStr] = Field(None, alias="otherDescription")
    other_type: Optional[StrictStr] = Field(None, alias="otherType")
    packing_costs: Optional[StrictFloat] = Field(None, alias="packingCosts")
    producer_specification: Optional[StrictStr] = Field(None, alias="producerSpecification")
    reason_for_export: Optional[StrictStr] = Field(None, alias="reasonForExport")
    reason_for_export_explanation: Optional[StrictStr] = Field(None, alias="reasonForExportExplanation")
    sdr_value: Optional[StrictFloat] = Field(None, alias="sdrValue")
    shipping_document_type: Optional[StrictStr] = Field(None, alias="shippingDocumentType")
    signature_contact: Optional[Address] = Field(None, alias="signatureContact")
    terms_of_sale: Optional[StrictStr] = Field(None, alias="termsOfSale")
    __properties = ["EELPFC", "blanketEndDate", "blanketStartDate", "certificateNumber", "comments", "currencyCode", "customsDeclaredValue", "declarationStatement", "freightCharge", "fromCustomsReference", "handlingCosts", "importerCustomsReference", "insuredAmount", "insuredNumber", "invoiceNumber", "licenseNumber", "otherCharge", "otherDescription", "otherType", "packingCosts", "producerSpecification", "reasonForExport", "reasonForExportExplanation", "sdrValue", "shippingDocumentType", "signatureContact", "termsOfSale"]

    @validator('other_type')
    def other_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('COMMISSIONS', 'DISCOUNTS', 'HANDLING_FEES', 'OTHER', 'ROYALTIES_AND_LICENSE_FEES', 'TAXES'):
            raise ValueError("must validate the enum values ('COMMISSIONS', 'DISCOUNTS', 'HANDLING_FEES', 'OTHER', 'ROYALTIES_AND_LICENSE_FEES', 'TAXES')")
        return v

    @validator('producer_specification')
    def producer_specification_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('MULTIPLE_SPECIFIED', 'SAME', 'SINGLE_SPECIFIED', 'UNKNOWN', 'AVAILABLE_UPON_REQUEST'):
            raise ValueError("must validate the enum values ('MULTIPLE_SPECIFIED', 'SAME', 'SINGLE_SPECIFIED', 'UNKNOWN', 'AVAILABLE_UPON_REQUEST')")
        return v

    @validator('reason_for_export')
    def reason_for_export_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('GIFT', 'COMMERCIAL_SAMPLE', 'MERCHANDISE', 'DOCUMENTS', 'RETURNED_GOODS', 'SOLD', 'NOT_SOLD', 'OTHER', 'DANGEROUS_GOOD', 'HUMANITARIAN_GOODS'):
            raise ValueError("must validate the enum values ('GIFT', 'COMMERCIAL_SAMPLE', 'MERCHANDISE', 'DOCUMENTS', 'RETURNED_GOODS', 'SOLD', 'NOT_SOLD', 'OTHER', 'DANGEROUS_GOOD', 'HUMANITARIAN_GOODS')")
        return v

    @validator('shipping_document_type')
    def shipping_document_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('NAFTA', 'COO'):
            raise ValueError("must validate the enum values ('NAFTA', 'COO')")
        return v

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
    def from_json(cls, json_str: str) -> CustomsInfo:
        """Create an instance of CustomsInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of signature_contact
        if self.signature_contact:
            _dict['signatureContact'] = self.signature_contact.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomsInfo:
        """Create an instance of CustomsInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CustomsInfo.parse_obj(obj)

        _obj = CustomsInfo.parse_obj({
            "eelpfc": obj.get("EELPFC"),
            "blanket_end_date": obj.get("blanketEndDate"),
            "blanket_start_date": obj.get("blanketStartDate"),
            "certificate_number": obj.get("certificateNumber"),
            "comments": obj.get("comments"),
            "currency_code": obj.get("currencyCode"),
            "customs_declared_value": obj.get("customsDeclaredValue"),
            "declaration_statement": obj.get("declarationStatement"),
            "freight_charge": obj.get("freightCharge"),
            "from_customs_reference": obj.get("fromCustomsReference"),
            "handling_costs": obj.get("handlingCosts"),
            "importer_customs_reference": obj.get("importerCustomsReference"),
            "insured_amount": obj.get("insuredAmount"),
            "insured_number": obj.get("insuredNumber"),
            "invoice_number": obj.get("invoiceNumber"),
            "license_number": obj.get("licenseNumber"),
            "other_charge": obj.get("otherCharge"),
            "other_description": obj.get("otherDescription"),
            "other_type": obj.get("otherType"),
            "packing_costs": obj.get("packingCosts"),
            "producer_specification": obj.get("producerSpecification"),
            "reason_for_export": obj.get("reasonForExport"),
            "reason_for_export_explanation": obj.get("reasonForExportExplanation"),
            "sdr_value": obj.get("sdrValue"),
            "shipping_document_type": obj.get("shippingDocumentType"),
            "signature_contact": Address.from_dict(obj.get("signatureContact")) if obj.get("signatureContact") is not None else None,
            "terms_of_sale": obj.get("termsOfSale")
        })
        return _obj

