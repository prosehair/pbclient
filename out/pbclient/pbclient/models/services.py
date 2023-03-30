# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Services(str, Enum):
    """
    The abbreviated name of the carrier-specific service. For abbreviations, see the Services table on the [carrier's reference page](https://shipping.pitneybowes.com/reference/carrier-services.html).   EM - Priority Mail Express | PM - Priority Mail | FCM - First-Class Mail | PRCLSEL - Parcel Select | STDPOST - Standard Post | LIB - Library Mail | MEDIA - Media Mail | PMOD - Priority Mail Open and Distribute | EMI - Priority Mail Express International | PMI - Priority Mail International | FCMI - First-Class Mail International | FCPIS - First-Class Package International Service. For overseas tracking,  [Do the APIs support E-USPS DELCON?](https://shipping.pitneybowes.com/faqs/shipments.html#usps-e-delcon-faq)
    """

    """
    allowed enum values
    """
    EM = 'EM'
    PM = 'PM'
    FCM = 'FCM'
    PRCLSEL = 'PRCLSEL'
    STDPOST = 'STDPOST'
    LIB = 'LIB'
    MEDIA = 'MEDIA'
    PMOD = 'PMOD'
    EMI = 'EMI'
    PMI = 'PMI'
    FCMI = 'FCMI'
    FCPIS = 'FCPIS'
    BPM = 'BPM'
    PSLW = 'PSLW'
    STANDARD = 'STANDARD'
    PBXPS = 'PBXPS'
    PBXUS = 'PBXUS'
    PBXPE = 'PBXPE'
    NDA_AM = 'NDA_AM'
    NDA = 'NDA'
    NDA_SVR = 'NDA_SVR'
    ENUM_2_DA_AM = '2DA_AM'
    ENUM_2DA = '2DA'
    ENUM_3DA = '3DA'
    GRD = 'GRD'
    HOM = 'HOM'
    NDA_AM_FREIGHT = 'NDA_AM_FREIGHT'
    NDA_FREIGHT = 'NDA_FREIGHT'
    ENUM_2_DA_FREIGHT = '2DA_FREIGHT'
    ENUM_3_DA_FREIGHT = '3DA_FREIGHT'
    SP_PRE_STD = 'SP_PRE_STD'
    SP_PRCLSEL = 'SP_PRCLSEL'
    SP_MEDIA = 'SP_MEDIA'
    SP_PRE_PRINT = 'SP_PRE_PRINT'
    XPP = 'XPP'
    EXP = 'EXP'
    XPD = 'XPD'
    STD = 'STD'
    EXS = 'EXS'
    EXP_FREIGHT = 'EXP_FREIGHT'
    XPD_FREIGHT = 'XPD_FREIGHT'

