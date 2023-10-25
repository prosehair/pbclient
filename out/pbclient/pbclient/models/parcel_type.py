# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.10
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ParcelType(str, Enum):
    """
    * LETTER -  Letter. Generates a First-Class label with IMB barcode.  * FRE - Flat rate envelope. * LGENV - Legal flat rate envelope. * LGLFRENV - Padded flat rate envelope. * PFRENV - Small flat rate box. * SFRB - Medium flat rate box. * FRB - Large Flat rate box. * LFRB - DVD box. * DVDBOX - DVDBOX. * VIDEOBOX - Video box. * MLFRB - Military flat raqte box. * RBA - Regional rate box, type A * RBB -  Regional rate box, type B. * PKG - Package (not eligible for special package rate). * LP - Large package. * FLAT - USPS Flat or Large Envelope. * EMMTB - Extended Managed Mail Tray Box. * FTB - Full tray box. * HTB - Half tray box. * SACK - Sack. * FTTB - Flat tub tray. * SOFTPACK - Soft Pack Envelope. * MIX - PMOD Enclosed Package Type. * LTR - Letter for stamp API call. 
    """

    """
    allowed enum values
    """
    FLAT = 'FLAT'
    LETTER = 'LETTER'
    FRE = 'FRE'
    LGENV = 'LGENV'
    LGLFRENV = 'LGLFRENV'
    PFRENV = 'PFRENV'
    FRB = 'FRB'
    LFRB = 'LFRB'
    DVDBOX = 'DVDBOX'
    VIDEOBOX = 'VIDEOBOX'
    MLFRB = 'MLFRB'
    RBA = 'RBA'
    RBB = 'RBB'
    LP = 'LP'
    SACK = 'SACK'
    SOFTPACK = 'SOFTPACK'
    MIX = 'MIX'
    LTR = 'LTR'
    NMLETTER = 'NMLETTER'
    NMLTR = 'NMLTR'
    IRRPKG = 'IRRPKG'
    SFRB = 'SFRB'
    EMMTB = 'EMMTB'
    FTB = 'FTB'
    FTTB = 'FTTB'
    HTB = 'HTB'
    PACK = 'PACK'
    BOX = 'BOX'
    SMALL_EXP_BOX = 'SMALL_EXP_BOX'
    MED_EXP_BOX = 'MED_EXP_BOX'
    LG_EXP_BOX = 'LG_EXP_BOX'
    EXTRA_LG_EXP_BOX = 'EXTRA_LG_EXP_BOX'
    TUBE = 'TUBE'
    ENUM_25KG = '25KG'
    ENUM_10KG = '10KG'
    PKG = 'PKG'

    @classmethod
    def from_json(cls, json_str: str) -> ParcelType:
        """Create an instance of ParcelType from a JSON string"""
        return ParcelType(json.loads(json_str))


