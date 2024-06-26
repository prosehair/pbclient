# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.14
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SpecialServiceCodes(str, Enum):
    """
    * Ins - Insured Mail.  * RR - Return receipt.  * Sig - Item is trackable if special service is requested. * ADSIG - Adult signature required. * Cert - Certified mail. * DelCon - Delivery confirmation. * ERR - Electronic return receipt. * RRm - Return receipt for merchandise. * Reg - Registered mail. * RegIns - Registered mail with insurance. * SH - Special handling - fragile. * CertRD - Certified mail with restricted delivery. * COD - Collect on delivery. * CODRD - Collect on delivery with restricted delivery. * InsRD - Insurance with restricted delivery. * RegRD - Registered mail with restricted delivery. * RegCOD - Registered mail with COD. * SigRD - Signature required with restricted delivery. * ADSIGRD - Adult signature required with restricted delivery. * RegInsRD - Registered mail with insurance and restricted delivery. * CERTAD - Certified mail with adult signature. * CERTADRD - Certified mail with adult signature and restricted delivery. * hazmat - Hazardous materials. * liveanimal - Live animal surcharge. * liveanimal_poultry - Live Animal-Day Old Poultry Surcharge * holiday - Holiday Delivery- For Priority Mail Express Service Only * sunday - Sunday delivery. * sunday_holiday - Sunday and holiday delivery. * PO_to_Addressee - PO to addressee * noWeekend - Do not deliver on weekend * TenThirty - Delivery by 10:30 AM * PMOD_OPTIONS - PMOD options * NOTIFICATIONS - Notifications. 
    """

    """
    allowed enum values
    """
    ADSIG = 'ADSIG'
    ADSIGRD = 'ADSIGRD'
    CERT = 'Cert'
    CERTAD = 'CERTAD'
    CERTADRD = 'CERTADRD'
    CERTRD = 'CertRD'
    COD = 'COD'
    CODRD = 'CODRD'
    DELCON = 'DelCon'
    ERR = 'ERR'
    HAZMAT = 'hazmat'
    HOLIDAY = 'holiday'
    INSRD = 'InsRD'
    LIVEANIMAL = 'liveanimal'
    LIVEANIMAL_MINUS__POULTRY = 'liveanimal - poultry'
    PMOD_OPTIONS = 'PMOD_OPTIONS'
    REG = 'Reg'
    REGCOD = 'RegCOD'
    REGINS = 'RegIns'
    REGINSRD = 'RegInsRD'
    REGRD = 'RegRD'
    RR = 'RR'
    RRM = 'RRM'
    SH = 'SH'
    SIG = 'SIG'
    SIGRD = 'SigRD'
    SUNDAY = 'sunday'
    SUNDAY_MINUS__HOLIDAY = 'sunday - holiday'
    NOTIFICATIONS = 'NOTIFICATIONS'
    PBXPS = 'PBXPS'
    PBXUS = 'PBXUS'
    PBXPE = 'PBXPE'
    ANCILLARY_ENDORSEMENT = 'ANCILLARY_ENDORSEMENT'
    ADD_HDL = 'ADD_HDL'
    ALCOHOL = 'ALCOHOL'
    CARRIER_LEAVE_IF_NO_RES = 'CARRIER_LEAVE_IF_NO_RES'
    DIRECT_SIG = 'DIRECT_SIG'
    APPOINTMENT = 'APPOINTMENT'
    DATE = 'DATE'
    EVENING = 'EVENING'
    GCOD = 'GCOD'
    PAL = 'PAL'
    PAL_PLUS = 'PAL_PLUS'
    SAT_DELIVERY = 'SAT_DELIVERY'
    SAT_PICKUP = 'SAT_PICKUP'
    HOLD = 'HOLD'
    NO_SIG = 'NO_SIG'
    PRL = 'PRL'
    ADULT_SIG = 'ADULT_SIG'
    CARBON = 'CARBON'
    COD_CASHIER = 'COD_CASHIER'
    COD_CHECK = 'COD_CHECK'
    DIRECT = 'DIRECT'
    DRY_ICE = 'DRY_ICE'
    INS = 'INS'
    SHP_RELEASE = 'SHP_RELEASE'
    VERBAL = 'VERBAL'

    @classmethod
    def from_json(cls, json_str: str) -> SpecialServiceCodes:
        """Create an instance of SpecialServiceCodes from a JSON string"""
        return SpecialServiceCodes(json.loads(json_str))


