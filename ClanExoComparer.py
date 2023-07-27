# Connor Downs
# Started: 7-26-2023
# Last Updated: 7-26-2023
# This program

import json
import os
import requests

from prettytable import PrettyTable

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://jotncomparer.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token"


def URLZero(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics.json', 'w')
    writeFile.write(exotic_data)
def URLOne(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_1.json', 'w')
    writeFile.write(exotic_data)
def URLTwo(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_2.json', 'w')
    writeFile.write(exotic_data)
def URLThree(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_3.json', 'w')
    writeFile.write(exotic_data)
def URLFour(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_4.json', 'w')
    writeFile.write(exotic_data)
def URLFive(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_5.json', 'w')
    writeFile.write(exotic_data)
def URLSix(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_6.json', 'w')
    writeFile.write(exotic_data)
def URLSeven(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_7.json', 'w')
    writeFile.write(exotic_data)
def URLEight(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_8.json', 'w')
    writeFile.write(exotic_data)
def URLNine(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_9.json', 'w')
    writeFile.write(exotic_data)
def URLTen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_10.json', 'w')
    writeFile.write(exotic_data)
def URLEleven(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_11.json', 'w')
    writeFile.write(exotic_data)
def URLTwelve(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_12.json', 'w')
    writeFile.write(exotic_data)
def URLThirteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_13.json', 'w')
    writeFile.write(exotic_data)
def URLFourteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_14.json', 'w')
    writeFile.write(exotic_data)
def URLFifteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_15.json', 'w')
    writeFile.write(exotic_data)
def URLSixteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_16.json', 'w')
    writeFile.write(exotic_data)
def URLSeventeen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_17.json', 'w')
    writeFile.write(exotic_data)
def URLEighteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_18.json', 'w')
    writeFile.write(exotic_data)
def URLNineteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_19.json', 'w')
    writeFile.write(exotic_data)
def URLTwenty(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_20.json', 'w')
    writeFile.write(exotic_data)
def URLTwenOne(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_21.json', 'w')
    writeFile.write(exotic_data)
def URLTwenTwo(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_22.json', 'w')
    writeFile.write(exotic_data)
def URLTwenThree(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_23.json', 'w')
    writeFile.write(exotic_data)

def ClanExoCombiner():
    SWB_K = 0
    SWB_P = 0

    STR_K = 0
    STR_P = 0

    VIG_K = 0
    VIG_P = 0

    RTK_K = 0
    RTK_P = 0

    MMT_K = 0
    MMT_P = 0

    CRM_K = 0
    CRM_P = 0

    JDR_K = 0
    JDR_P = 0

    HKB_K = 0
    HKB_P = 0

    SRR_K = 0
    SRR_P = 0

    CBS_K = 0
    CBS_P = 0

    WHE_K = 0
    WHE_P = 0

    MFC_K = 0
    MFC_P = 0

    AOS_K = 0
    AOS_P = 0

    CPR_K = 0
    CPR_P = 0

    IZB_K = 0
    IZB_P = 0

    TLW_K = 0
    TLW_P = 0

    ABL_K = 0
    ABL_P = 0

    TRN_K = 0
    TRN_P = 0

    OBP_K = 0
    OBP_P = 0

    LMN_K = 0
    LMN_P = 0

    BJJ_K = 0
    BJJ_P = 0

    MTC_K = 0
    MTC_P = 0

    BSN_K = 0
    BSN_P = 0

    WTH_K = 0
    WTH_P = 0

    TVC_K = 0
    TVC_P = 0

    HKM_K = 0
    HKM_P = 0

    NTE_K = 0
    NTE_P = 0

    DMT_K = 0
    DMT_P = 0

    CSK_K = 0
    CSK_P = 0

    ASP_K = 0
    ASP_P = 0

    FRN_K = 0
    FRN_P = 0

    OTS_K = 0
    OTS_P = 0

    TOM_K = 0
    TOM_P = 0

    QSS_K = 0
    QSS_P = 0

    RVZ_K = 0
    RVZ_P = 0

    FNW_K = 0
    FNW_P = 0

    CDF_K = 0
    CDF_P = 0

    VGC_K = 0
    VGC_P = 0

    WKI_K = 0
    WKI_P = 0

    NVG_K = 0
    NVG_P = 0

    CDH_K = 0
    CDH_P = 0

    MCL_K = 0
    MCL_P = 0

    FTL_K = 0
    FTL_P = 0

    SNS_K = 0
    SNS_P = 0

    GVL_K = 0
    GVL_P = 0

    SBO_K = 0
    SBO_P = 0

    BEL_K = 0
    BEL_P = 0

    RSR_K = 0
    RSR_P = 0

    HDL_K = 0
    HDL_P = 0

    PML_K = 0
    PML_P = 0

    TLT_K = 0
    TLT_P = 0

    PLL_K = 0
    PLL_P = 0

    TNG_K = 0
    TNG_P = 0

    WVP_K = 0
    WVP_P = 0

    LOW_K = 0
    LOW_P = 0

    LMR_K = 0
    LMR_P = 0

    JTN_K = 0
    JTN_P = 0

    TRB_K = 0
    TRB_P = 0

    EIV_K = 0
    EIV_P = 0

    DVN_K = 0
    DVN_P = 0

    SMY_K = 0
    SMY_P = 0

    DVR_K = 0
    DVR_P = 0

    TMB_K = 0
    TMB_P = 0

    TFH_K = 0
    TFH_P = 0

    RNE_K = 0
    RNE_P = 0

    DLT_K = 0
    DLT_P = 0

    CDS_K = 0
    CDS_P = 0

    TCD_K = 0
    TCD_P = 0

    VMC_K = 0
    VMC_P = 0

    LRD_K = 0
    LRD_P = 0

    EOC_K = 0
    EOC_P = 0

    EOA_K = 0
    EOA_P = 0

    EOI_K = 0
    EOI_P = 0

    DMS_K = 0
    DMS_P = 0

    CLO_K = 0
    CLO_P = 0

    DCT_K = 0
    DCT_P = 0

    TSP_K = 0
    TSP_P = 0

    TMC_K = 0
    TMC_P = 0

    HON_K = 0
    HON_P = 0

    VCB_K = 0
    VCB_P = 0

    CTF_K = 0
    CTF_P = 0

    PST_K = 0
    PST_P = 0

    WCC_K = 0
    WCC_P = 0

    TCC_K = 0
    TCC_P = 0

    LOA_K = 0
    LOA_P = 0

    DRC_K = 0
    DRC_P = 0

    CLN_K = 0
    CLN_P = 0

    WLZ_K = 0
    WLZ_P = 0

    SPS_K = 0
    SPS_P = 0

    OKV_K = 0
    OKV_P = 0

    TTF_K = 0
    TTF_P = 0

    BKT_K = 0
    BKT_P = 0

    QNB_K = 0
    QNB_P = 0

    TDL_K = 0
    TDL_P = 0

    ARK_K = 0
    ARK_P = 0

    LVB_K = 0
    LVB_P = 0

    XNP_K = 0
    XNP_P = 0

    DBG_K = 0
    DBG_P = 0

    HAP_K = 0
    HAP_P = 0

    SVG_K = 0
    SVG_P = 0

    EOT_K = 0
    EOT_P = 0

    LMT_K = 0
    LMT_P = 0

    GLH_K = 0
    GLH_P = 0

    PRS_K = 0
    PRS_P = 0

    GOT_K = 0
    GOT_P = 0

    HSD_K = 0
    HSD_P = 0

    DTC_K = 0
    DTC_P = 0

    WTB_K = 0
    WTB_P = 0

    TUH_K = 0
    TUH_P = 0

    WOW_K = 0
    WOW_P = 0

    with open('Exotics.json') as f:
        data1 = json.load(f)
    with open('Exotics_1.json') as f:
        data2 = json.load(f)
    with open('Exotics_2.json') as f:
        data3 = json.load(f)
    with open('Exotics_3.json') as f:
        data4 = json.load(f)
    with open('Exotics_4.json') as f:
        data5 = json.load(f)
    with open('Exotics_5.json') as f:
        data6 = json.load(f)
    with open('Exotics_6.json') as f:
        data7 = json.load(f)
    with open('Exotics_7.json') as f:
        data8 = json.load(f)
    with open('Exotics_8.json') as f:
        data9 = json.load(f)
    with open('Exotics_9.json') as f:
        data10 = json.load(f)
    with open('Exotics_10.json') as f:
        data11 = json.load(f)
    with open('Exotics_11.json') as f:
        data12 = json.load(f)
    with open('Exotics_12.json') as f:
        data13 = json.load(f)
    with open('Exotics_13.json') as f:
        data14 = json.load(f)
    with open('Exotics_14.json') as f:
        data15 = json.load(f)
    with open('Exotics_15.json') as f:
        data16 = json.load(f)
    with open('Exotics_16.json') as f:
        data17 = json.load(f)
    with open('Exotics_17.json') as f:
        data18 = json.load(f)
    with open('Exotics_18.json') as f:
        data19 = json.load(f)
    with open('Exotics_19.json') as f:
        data20 = json.load(f)
    with open('Exotics_20.json') as f:
        data21 = json.load(f)
    with open('Exotics_21.json') as f:
        data22 = json.load(f)
    with open('Exotics_22.json') as f:
        data23 = json.load(f)
    with open('Exotics_23.json') as f:
        data24 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]
    items4 = data4["Response"]
    items5 = data5["Response"]
    items6 = data6["Response"]
    items7 = data7["Response"]
    items8 = data8["Response"]
    items9 = data9["Response"]
    items10 = data10["Response"]
    items11 = data11["Response"]
    items12 = data12["Response"]
    items13 = data13["Response"]
    items14 = data14["Response"]
    items15 = data15["Response"]
    items16 = data16["Response"]
    items17 = data17["Response"]
    items18 = data18["Response"]
    items19 = data19["Response"]
    items20 = data20["Response"]
    items21 = data21["Response"]
    items22 = data22["Response"]
    items23 = data23["Response"]
    items24 = data24["Response"]

    exotic_json = {"Response": []}

    exotic_json['Response'].append(items1)
    exotic_json["Response"].append(items2)
    exotic_json["Response"].append(items3)
    exotic_json['Response'].append(items4)
    exotic_json["Response"].append(items5)
    exotic_json["Response"].append(items6)
    exotic_json['Response'].append(items7)
    exotic_json["Response"].append(items8)
    exotic_json["Response"].append(items9)
    exotic_json['Response'].append(items10)
    exotic_json["Response"].append(items11)
    exotic_json["Response"].append(items12)
    exotic_json['Response'].append(items13)
    exotic_json["Response"].append(items14)
    exotic_json["Response"].append(items15)
    exotic_json['Response'].append(items16)
    exotic_json["Response"].append(items17)
    exotic_json["Response"].append(items18)
    exotic_json['Response'].append(items19)
    exotic_json["Response"].append(items20)
    exotic_json["Response"].append(items21)
    exotic_json['Response'].append(items22)
    exotic_json["Response"].append(items23)
    exotic_json["Response"].append(items24)

    with open('exotic.json', "w") as f:
        f.write(json.dumps(exotic_json, indent=2))

    exotic_len_1 = len(exotic_json["Response"][0]['weapons'])
    exotic_len_2 = len(exotic_json["Response"][1]['weapons'])
    exotic_len_3 = len(exotic_json["Response"][2]['weapons'])
    exotic_len_4 = len(exotic_json["Response"][3]['weapons'])
    exotic_len_5 = len(exotic_json["Response"][4]['weapons'])
    exotic_len_6 = len(exotic_json["Response"][5]['weapons'])
    exotic_len_7 = len(exotic_json["Response"][6]['weapons'])
    exotic_len_8 = len(exotic_json["Response"][7]['weapons'])
    exotic_len_9 = len(exotic_json["Response"][8]['weapons'])
    exotic_len_10 = len(exotic_json["Response"][9]['weapons'])
    exotic_len_11 = len(exotic_json["Response"][10]['weapons'])
    exotic_len_12 = len(exotic_json["Response"][11]['weapons'])
    exotic_len_13 = len(exotic_json["Response"][12]['weapons'])
    exotic_len_14 = len(exotic_json["Response"][13]['weapons'])
    exotic_len_15 = len(exotic_json["Response"][14]['weapons'])
    exotic_len_16 = len(exotic_json["Response"][15]['weapons'])
    exotic_len_17 = len(exotic_json["Response"][16]['weapons'])
    exotic_len_18 = len(exotic_json["Response"][17]['weapons'])
    exotic_len_19 = len(exotic_json["Response"][18]['weapons'])
    exotic_len_20 = len(exotic_json["Response"][19]['weapons'])
    exotic_len_21 = len(exotic_json["Response"][20]['weapons'])
    exotic_len_22 = len(exotic_json["Response"][21]['weapons'])
    exotic_len_23 = len(exotic_json["Response"][22]['weapons'])
    exotic_len_24 = len(exotic_json["Response"][23]['weapons'])

    Exotic = {"Exotic": []}
    Kills = {"Kills": []}
    Precision = {"Precision Kills": []}

    for number in range(0, exotic_len_1):
        Name_1 = exotic_json["Response"][0]["weapons"][number]["referenceId"]
        Kills_1 = exotic_json["Response"][0]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_1 = \
            exotic_json["Response"][0]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_1)
        Kills['Kills'].append(Kills_1)
        Precision['Precision Kills'].append(Precision_1)
    for number in range(0, exotic_len_2):
        Name_2 = exotic_json["Response"][1]["weapons"][number]["referenceId"]
        Kills_2 = exotic_json["Response"][1]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_2 = \
            exotic_json["Response"][1]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_2)
        Kills['Kills'].append(Kills_2)
        Precision['Precision Kills'].append(Precision_2)
    for number in range(0, exotic_len_3):
        Name_3 = exotic_json["Response"][2]["weapons"][number]["referenceId"]
        Kills_3 = exotic_json["Response"][2]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_3 = \
            exotic_json["Response"][2]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_3)
        Kills['Kills'].append(Kills_3)
        Precision['Precision Kills'].append(Precision_3)
    for number in range(0, exotic_len_4):
        Name_4 = exotic_json["Response"][3]["weapons"][number]["referenceId"]
        Kills_4 = exotic_json["Response"][3]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_4 = \
            exotic_json["Response"][3]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_4)
        Kills['Kills'].append(Kills_4)
        Precision['Precision Kills'].append(Precision_4)
    for number in range(0, exotic_len_5):
        Name_5 = exotic_json["Response"][4]["weapons"][number]["referenceId"]
        Kills_5 = exotic_json["Response"][4]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_5 = \
            exotic_json["Response"][4]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_5)
        Kills['Kills'].append(Kills_5)
        Precision['Precision Kills'].append(Precision_5)
    for number in range(0, exotic_len_6):
        Name_6 = exotic_json["Response"][5]["weapons"][number]["referenceId"]
        Kills_6 = exotic_json["Response"][5]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_6 = \
            exotic_json["Response"][5]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_6)
        Kills['Kills'].append(Kills_6)
        Precision['Precision Kills'].append(Precision_6)
    for number in range(0, exotic_len_7):
        Name_7 = exotic_json["Response"][6]["weapons"][number]["referenceId"]
        Kills_7 = exotic_json["Response"][6]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_7 = \
            exotic_json["Response"][6]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_7)
        Kills['Kills'].append(Kills_7)
        Precision['Precision Kills'].append(Precision_7)
    for number in range(0, exotic_len_8):
        Name_8 = exotic_json["Response"][7]["weapons"][number]["referenceId"]
        Kills_8 = exotic_json["Response"][7]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_8 = \
            exotic_json["Response"][7]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_8)
        Kills['Kills'].append(Kills_8)
        Precision['Precision Kills'].append(Precision_8)
    for number in range(0, exotic_len_9):
        Name_9 = exotic_json["Response"][8]["weapons"][number]["referenceId"]
        Kills_9 = exotic_json["Response"][8]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_9 = \
            exotic_json["Response"][8]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_9)
        Kills['Kills'].append(Kills_9)
        Precision['Precision Kills'].append(Precision_9)
    for number in range(0, exotic_len_10):
        Name_10 = exotic_json["Response"][9]["weapons"][number]["referenceId"]
        Kills_10 = exotic_json["Response"][9]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_10 = \
            exotic_json["Response"][9]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_10)
        Kills['Kills'].append(Kills_10)
        Precision['Precision Kills'].append(Precision_10)
    for number in range(0, exotic_len_11):
        Name_11 = exotic_json["Response"][10]["weapons"][number]["referenceId"]
        Kills_11 = exotic_json["Response"][10]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_11 = \
            exotic_json["Response"][10]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_11)
        Kills['Kills'].append(Kills_11)
        Precision['Precision Kills'].append(Precision_11)
    for number in range(0, exotic_len_12):
        Name_12 = exotic_json["Response"][11]["weapons"][number]["referenceId"]
        Kills_12 = exotic_json["Response"][11]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_12 = \
            exotic_json["Response"][11]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_12)
        Kills['Kills'].append(Kills_12)
        Precision['Precision Kills'].append(Precision_12)
    for number in range(0, exotic_len_13):
        Name_13 = exotic_json["Response"][12]["weapons"][number]["referenceId"]
        Kills_13 = exotic_json["Response"][12]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_13 = \
            exotic_json["Response"][12]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_13)
        Kills['Kills'].append(Kills_13)
        Precision['Precision Kills'].append(Precision_13)
    for number in range(0, exotic_len_14):
        Name_14 = exotic_json["Response"][13]["weapons"][number]["referenceId"]
        Kills_14 = exotic_json["Response"][13]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_14 = \
            exotic_json["Response"][13]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_14)
        Kills['Kills'].append(Kills_14)
        Precision['Precision Kills'].append(Precision_14)
    for number in range(0, exotic_len_15):
        Name_15 = exotic_json["Response"][14]["weapons"][number]["referenceId"]
        Kills_15 = exotic_json["Response"][14]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_15 = \
            exotic_json["Response"][14]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_15)
        Kills['Kills'].append(Kills_15)
        Precision['Precision Kills'].append(Precision_15)
    for number in range(0, exotic_len_16):
        Name_16 = exotic_json["Response"][15]["weapons"][number]["referenceId"]
        Kills_16 = exotic_json["Response"][15]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_16 = \
            exotic_json["Response"][15]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_16)
        Kills['Kills'].append(Kills_16)
        Precision['Precision Kills'].append(Precision_16)
    for number in range(0, exotic_len_17):
        Name_17 = exotic_json["Response"][16]["weapons"][number]["referenceId"]
        Kills_17 = exotic_json["Response"][16]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_17 = \
            exotic_json["Response"][16]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_17)
        Kills['Kills'].append(Kills_17)
        Precision['Precision Kills'].append(Precision_17)
    for number in range(0, exotic_len_18):
        Name_18 = exotic_json["Response"][17]["weapons"][number]["referenceId"]
        Kills_18 = exotic_json["Response"][17]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_18 = \
            exotic_json["Response"][17]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_18)
        Kills['Kills'].append(Kills_18)
        Precision['Precision Kills'].append(Precision_18)
    for number in range(0, exotic_len_19):
        Name_19 = exotic_json["Response"][18]["weapons"][number]["referenceId"]
        Kills_19 = exotic_json["Response"][18]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_19 = \
            exotic_json["Response"][18]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_19)
        Kills['Kills'].append(Kills_19)
        Precision['Precision Kills'].append(Precision_19)
    for number in range(0, exotic_len_20):
        Name_20 = exotic_json["Response"][19]["weapons"][number]["referenceId"]
        Kills_20 = exotic_json["Response"][19]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_20 = \
            exotic_json["Response"][19]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_20)
        Kills['Kills'].append(Kills_20)
        Precision['Precision Kills'].append(Precision_20)
    for number in range(0, exotic_len_21):
        Name_21 = exotic_json["Response"][20]["weapons"][number]["referenceId"]
        Kills_21 = exotic_json["Response"][20]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_21 = \
            exotic_json["Response"][20]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_21)
        Kills['Kills'].append(Kills_21)
        Precision['Precision Kills'].append(Precision_21)
    for number in range(0, exotic_len_22):
        Name_22 = exotic_json["Response"][21]["weapons"][number]["referenceId"]
        Kills_22 = exotic_json["Response"][21]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_22 = \
            exotic_json["Response"][21]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_22)
        Kills['Kills'].append(Kills_22)
        Precision['Precision Kills'].append(Precision_22)
    for number in range(0, exotic_len_23):
        Name_23 = exotic_json["Response"][22]["weapons"][number]["referenceId"]
        Kills_23 = exotic_json["Response"][22]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_23 = \
            exotic_json["Response"][22]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_23)
        Kills['Kills'].append(Kills_23)
        Precision['Precision Kills'].append(Precision_23)
    for number in range(0, exotic_len_24):
        Name_24 = exotic_json["Response"][23]["weapons"][number]["referenceId"]
        Kills_24 = exotic_json["Response"][23]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_24 = \
            exotic_json["Response"][23]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_24)
        Kills['Kills'].append(Kills_24)
        Precision['Precision Kills'].append(Precision_24)

    Exotic_Info = [Exotic, Kills, Precision]

    length = len(Exotic_Info[0]['Exotic'])

    for numb in range(0, length):
        ID = Exotic_Info[0]['Exotic'][numb]
        Kills = Exotic_Info[1]['Kills'][numb]
        Precision = Exotic_Info[2]['Precision Kills'][numb]

        if ID == 2208405142:
            Exotic = "Telesto"
            TLT_K += Kills
            TLT_P += Precision
        elif ID == 2232171099:
            Exotic = "Deathbringer"
            DBG_K += Kills
            DBG_P += Precision
        elif ID == 2357297366:
            Exotic = "Witherhoard"
            WTH_K += Kills
            WTH_P += Precision
        elif ID == 2591746970:
            Exotic = "Leviathan's Breath"
            LVB_K += Kills
            LVB_P += Precision
        elif ID == 2694576561:
            Exotic = "Two-Tailed Fox"
            TTF_K += Kills
            TTF_P += Precision
        elif ID == 2812324400:
            Exotic = "Parasite"
            PRS_K += Kills
            PRS_P += Precision
        elif ID == 2812324401:
            Exotic = "Dead Messenger"
            DMS_K += Kills
            DMS_P += Precision
        elif ID == 2816212794:
            Exotic = "Bad Juju"
            BJJ_K += Kills
            BJJ_P += Precision
        elif ID == 2856683562:
            Exotic = "SUROS Regime"
            SRR_K += Kills
            SRR_P += Precision
        elif ID == 2907129557:
            Exotic = "Sunshot"
            SNS_K += Kills
            SNS_P += Precision
        elif ID == 3089417789:
            Exotic = "Riskrunner"
            RSR_K += Kills
            RSR_P += Precision
        elif ID == 3118061005:
            Exotic = "Vexcalibur"
            VCB_K += Kills
            VCB_P += Precision
        elif ID == 3141979346:
            Exotic = "D.A.R.C.I."
            DRC_K += Kills
            DRC_P += Precision
        elif ID == 3260753130:
            Exotic = "Ticuu's Divination"
            TCD_K += Kills
            TCD_P += Precision
        elif ID == 3325463374:
            Exotic = "Thunderlord"
            TDL_K += Kills
            TDL_P += Precision
        elif ID == 3413074534:
            Exotic = "Polaris Lance"
            PLL_K += Kills
            PLL_P += Precision
        elif ID == 3413860062:
            Exotic = "The Chaperone"
            CPR_K += Kills
            CPR_P += Precision
        elif ID == 3413860063:
            Exotic = "Lord of Wolves"
            LOW_K += Kills
            LOW_P += Precision
        elif ID == 3437746471:
            Exotic = "Crimson"
            CRM_K += Kills
            CRM_P += Precision
        elif ID == 3460576091:
            Exotic = "Duality"
            DLT_K += Kills
            DLT_P += Precision
        elif ID == 3487253372:
            Exotic = "The Lament"
            LMT_K += Kills
            LMT_P += Precision
        elif ID == 3524313097:
            Exotic = "Eriana's Vow"
            EIV_K += Kills
            EIV_P += Precision
        elif ID == 3580904581:
            Exotic = "Tractor Cannon"
            TCC_K += Kills
            TCC_P += Precision
        elif ID == 3588934839:
            Exotic = "Le Monarque"
            LMR_K += Kills
            LMR_P += Precision
        elif ID == 3628991658:
            Exotic = "Graviton Lance"
            GVL_K += Kills
            GVL_P += Precision
        elif ID == 3628991659:
            Exotic = "Vigilance Wing"
            VIG_K += Kills
            VIG_P += Precision
        elif ID == 3654674561:
            Exotic = "Dead Man's Tale"
            DMT_K += Kills
            DMT_P += Precision
        elif ID == 3659414143:
            Exotic = "Verglas Curve"
            VGC_K += Kills
            VGC_P += Precision
        elif ID == 3664831848:
            Exotic = "Heartshadow"
            HSD_K += Kills
            HSD_P += Precision
        elif ID == 3973202132:
            Exotic = "Thorn"
            TRN_K += Kills
            TRN_P += Precision
        elif ID == 4017959782:
            Exotic = "Symmetry"
            SMY_K += Kills
            SMY_P += Precision
        elif ID == 4036115577:
            Exotic = "Sleeper Simulant"
            SPS_K += Kills
            SPS_P += Precision
        elif ID == 4068264807:
            Exotic = "Monte Carlo"
            MTC_K += Kills
            MTC_P += Precision
        elif ID == 4124984448:
            Exotic = "Hard Light"
            HDL_K += Kills
            HDL_P += Precision
        elif ID == 4255268456:
            Exotic = "Skyburner's Oath"
            SBO_K += Kills
            SBO_P += Precision
        elif ID == 4293613902:
            Exotic = "Quicksilver Storm"
            QSS_K += Kills
            QSS_P += Precision
        elif ID == 19024058:
            Exotic = "Prometheus Lens"
            PML_K += Kills
            PML_P += Precision
        elif ID == 46524085:
            Exotic = "Osteo Striga"
            OTS_K += Kills
            OTS_P += Precision
        elif ID == 204878059:
            Exotic = "Malfeasance"
            MFC_K += Kills
            MFC_P += Precision
        elif ID == 370712896:
            Exotic = "Salvation's Grip"
            SVG_K += Kills
            SVG_P += Precision
        elif ID == 374573733:
            Exotic = "Delicate Tomb"
            DCT_K += Kills
            DCT_P += Precision
        elif ID == 400096939:
            Exotic = "Outbreak Perfected"
            OBP_K += Kills
            OBP_P += Precision
        elif ID == 417164956:
            Exotic = "Jötunn"
            JTN_K += Kills
            JTN_P += Precision
        elif ID == 449318888:
            Exotic = "Deterministic Chaos"
            DTC_K += Kills
            DTC_P += Precision
        elif ID == 776191470:
            Exotic = "Tommy's Matchbook"
            TMB_K += Kills
            TMB_P += Precision
        elif ID == 814876684:
            Exotic = "Wish-Ender"
            WHE_K += Kills
            WHE_P += Precision
        elif ID == 814876685:
            Exotic = "Trinity Ghoul"
            TNG_K += Kills
            TNG_P += Precision
        elif ID == 1345867570:
            Exotic = "Sweet Business"
            SWB_K += Kills
            SWB_P += Precision
        elif ID == 1345867571:
            Exotic = "Coldheart"
            CDH_K += Kills
            CDH_P += Precision
        elif ID == 1363238943:
            Exotic = "Ruinous Effigy"
            RNE_K += Kills
            RNE_P += Precision
        elif ID == 1363886209:
            Exotic = "Gjallarhorn"
            GLH_K += Kills
            GLH_P += Precision
        elif ID == 1395261499:
            Exotic = "Xenophage"
            XNP_K += Kills
            XNP_P += Precision
        elif ID == 1441805468:
            Exotic = "The Navigator"
            NVG_K += Kills
            NVG_P += Precision
        elif ID == 1473821207:
            Exotic = "Revision Zero"
            RVZ_K += Kills
            RVZ_P += Precision
        elif ID == 1508896098:
            Exotic = "The Wardcliff Coil"
            WCC_K += Kills
            WCC_P += Precision
        elif ID == 1594120904:
            Exotic = "No Time to Explain"
            NTE_K += Kills
            NTE_P += Precision
        elif ID == 1665952087:
            Exotic = "The Fourth Horseman"
            TFH_K += Kills
            TFH_P += Precision
        elif ID == 1763584999:
            Exotic = "Grand Overture"
            GOT_K += Kills
            GOT_P += Precision
        elif ID == 1833195496:
            Exotic = "Ager's Scepter"
            ASP_K += Kills
            ASP_P += Precision
        elif ID == 1912669214:
            Exotic = "Centrifuse"
            CTF_K += Kills
            CTF_P += Precision
        elif ID == 2044500762:
            Exotic = "The Queenbreaker"
            QNB_K += Kills
            QNB_P += Precision
        elif ID == 2130065553:
            Exotic = "Arbalest"
            ABL_K += Kills
            ABL_P += Precision
        elif ID == 2179048386:
            Exotic = "Forerunner"
            FRN_K += Kills
            FRN_P += Precision
        elif ID == 2286143274:
            Exotic = "Huckleberry"
            HKB_K += Kills
            HKB_P += Precision
        elif ID == 2362471601:
            Exotic = "Rat King"
            RTK_K += Kills
            RTK_P += Precision
        elif ID == 2376481550:
            Exotic = "Anarchy"
            ARK_K += Kills
            ARK_P += Precision
        elif ID == 2399110176:
            Exotic = "Eyes of Tomorrow"
            EOT_K += Kills
            EOT_P += Precision
        elif ID == 2415517654:
            Exotic = "Bastion"
            BSN_K += Kills
            BSN_P += Precision
        elif ID == 2603483885:
            Exotic = "Cloudstrike"
            CDS_K += Kills
            CDS_P += Precision
        elif ID == 2907129556:
            Exotic = "Strum"
            STR_K += Kills
            STR_P += Precision
        elif ID == 3110698812:
            Exotic = "Tarrabah"
            TRB_K += Kills
            TRB_P += Precision
        elif ID == 3118061004:
            Exotic = "Winterbite"
            WTB_K += Kills
            WTB_P += Precision
        elif ID == 3121540812:
            Exotic = "Final Warning"
            FNW_K += Kills
            FNW_P += Precision
        elif ID == 3141979347:
            Exotic = "Borealis"
            BEL_K += Kills
            BEL_P += Precision
        elif ID == 3211806999:
            Exotic = "Izanagi's Burden"
            IZB_K += Kills
            IZB_P += Precision
        elif ID == 3371017761:
            Exotic = "Conditional Finality"
            CDF_K += Kills
            CDF_P += Precision
        elif ID == 3505113722:
            Exotic = "Collective Obligation"
            CLO_K += Kills
            CLO_P += Precision
        elif ID == 3512014804:
            Exotic = "Lumina"
            LMN_K += Kills
            LMN_P += Precision
        elif ID == 3580904580 or ID == 1744115122:
            Exotic = "Legend of Acrius"
            LOA_K += Kills
            LOA_P += Precision
        elif ID == 3761898871:
            Exotic = "Lorentz Driver"
            LRD_K += Kills
            LRD_P += Precision
        elif ID == 3766045777:
            Exotic = "Black Talon"
            BKT_K += Kills
            BKT_P += Precision
        elif ID == 3824106094:
            Exotic = "Devil's Ruin"
            DVR_K += Kills
            DVR_P += Precision
        elif ID == 3844694310:
            Exotic = "The Jade Rabbit"
            JDR_K += Kills
            JDR_P += Precision
        elif ID == 3856705927:
            Exotic = "Hawkmoon"
            HKM_K += Kills
            HKM_P += Precision
        elif ID == 3899270607:
            Exotic = "The Colony"
            CLN_K += Kills
            CLN_P += Precision
        elif ID == 4174431791:
            Exotic = "Hierarchy of Needs"
            HON_K += Kills
            HON_P += Precision
        elif ID == 4289226715:
            Exotic = "Vex Mythoclast"
            VMC_K += Kills
            VMC_P += Precision
        elif ID == 14194600:
            Exotic = "Edge of Intent"
            EOI_K += Kills
            EOI_P += Precision
        elif ID == 219145368:
            Exotic = "The Manticore"
            TMC_K += Kills
            TMC_P += Precision
        elif ID == 347366834:
            Exotic = "Ace of Spades"
            AOS_K += Kills
            AOS_P += Precision
        elif ID == 940371471:
            Exotic = "Wicked Implement"
            WKI_K += Kills
            WKI_P += Precision
        elif ID == 1201830623:
            Exotic = "Truth"
            TUH_K += Kills
            TUH_P += Precision
        elif ID == 1234150730:
            Exotic = "Trespasser"
            TSP_K += Kills
            TSP_P += Precision
        elif ID == 1331482397:
            Exotic = "MIDA Multi-Tool"
            MMT_K += Kills
            MMT_P += Precision
        elif ID == 1364093401:
            Exotic = "The Last WOrd"
            TLW_K += Kills
            TLW_P += Precision
        elif ID == 1541131350:
            Exotic = "Cerberus+1"
            CBS_K += Kills
            CBS_P += Precision
        elif ID == 1802135586:
            Exotic = "Touch of Malice"
            TOM_K += Kills
            TOM_P += Precision
        elif ID == 1852863732:
            Exotic = "Wavesplitter"
            WVP_K += Kills
            WVP_P += Precision
        elif ID == 1853180924:
            Exotic = "Traveler's Chosen"
            TVC_K += Kills
            TVC_P += Precision
        elif ID == 1864563948:
            Exotic = "Worldline Zero"
            WLZ_K += Kills
            WLZ_P += Precision
        elif ID == 1891561814:
            Exotic = "Whisper of the Worm"
            WOW_K += Kills
            WOW_P += Precision
        elif ID == 2069224589:
            Exotic = "One Thousand Voices"
            OKV_K += Kills
            OKV_P += Precision
        elif ID == 2084878005:
            Exotic = "Heir Apparent"
            HAP_K += Kills
            HAP_P += Precision
        # elif ID ==
        # elif ID ==
        # elif ID ==

    Primary = PrettyTable()
    Primary.add_column("Exotic", ["Sweet Business", "Strum", "Vigilance Wing", "Rat King", "MIDA Multi-Tool", "Crimson",
                                  "The Jade Rabbit", "The Huckleberry", "SUROS Regime", "Cerberus+1", "Wish-Ender",
                                  "Malfeasance", "Ace of Spades", "The Last Word", "Thorn", "Outbreak Perfected",
                                  "Lumina", "Bad Juju", "Monte Carlo", "Traveler's Chosen", "Hawkmoon",
                                  "No Time to Explain",
                                  "Dead Man's Tale", "Cryosthethesia 77K", "Osteo Striga", "Touch of Malice",
                                  "Quicksilver Storm", "Revision Zero", "Final Warning", "Verglas Curve",
                                  "Wicked Implement",
                                  "Fighting Lion", "Sunshot", "Skyburner's Oath", "Riskrunner", "Hard Light",
                                  "Polaris Lance",
                                  "Trinity Ghoul", "Le Monarque", "Tarrabah", "Symmetry", "Devil's Ruin",
                                  "Tommy's Matchbook",
                                  "Ticuu's Divination", "Vex Mythoclast", "Collective Obligation", "Trespasser",
                                  "The Manticore", "Hierarchy of Needs", "Centrifuse"])
    Primary.add_column("Element",
                       ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                        "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                        "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis",
                        "Kinetic", "Kinetic", "Kinetic/Strand", "Kinetic", "Strand", "Stasis", "Stasis",
                        "Void", "Solar", "Solar", "Arc", "Arc/Void/Solar", "Solar", "Arc", "Void", "Solar",
                        "Arc", "Solar", "Solar", "Solar", "Solar", "Void", "Arc", "Void", "Solar", "Arc"])
    Primary.add_column("Weapon Type", ["Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sidearm", "Scout Rifle",
                                       "Hand Cannon", "Scout Rifle", "Submachine Gun", "Auto Rifle", "Auto Rifle",
                                       "Combat Bow", "Hand Cannon", "Hand Cannon", "Hand Cannon", "Hand Cannon",
                                       "Pulse Rifle", "Hand Cannon", "Pulse Rifle", "Auto Rifle", "Sidearm",
                                       "Hand Cannon", "Pulse Rifle", "Scout Rifle", "Sidearm", "Submachine Gun",
                                       "Scout Rifle", "Auto Rifle", "Pulse Rifle", "Sidearm", "Combat Bow",
                                       "Scout Rifle", "Grenade Launcher", "Hand Cannon", "Scout Rifle",
                                       "Submachine Gun", "Auto Rifle", "Scout Rifle", "Combat Bow", "Combat Bow",
                                       "Submachine Gun", "Scout Rifle", "Sidearm", "Auto Rifle", "Combat Bow",
                                       "Fusion Rifle", "Pulse Rifle", "Sidearm", "Submachine Gun", "Combat Bow",
                                       "Auto Rifle"])
    Primary.add_column("Kills",
                       [SWB_K, STR_K, VIG_K, RTK_K, MMT_K, CRM_K, JDR_K, HKB_K, SRR_K, CBS_K, WHE_K, MFC_K, AOS_K,
                        TLW_K, TRN_K, OBP_K, LMN_K, BJJ_K, MTC_K, TVC_K, HKM_K, NTE_K, DMT_K, CSK_K, OTS_K, TOM_K,
                        QSS_K, RVZ_K, FNW_K, VGC_K, WKI_K, FTL_K, SNS_K, SBO_K, RSR_K, HDL_K, PLL_K, TNG_K, LMR_K,
                        TRB_K, SMY_K, DVR_K, TMB_K, TCD_K, VMC_K, CLO_K, TSP_K, TMC_K, HON_K, CTF_K])
    Primary.add_column("Precision Kills",
                       [SWB_P, STR_P, VIG_P, RTK_P, MMT_P, CRM_P, JDR_P, HKB_P, SRR_P, CBS_P, WHE_P, MFC_P, AOS_P,
                        TLW_P, TRN_P, OBP_P, LMN_P, BJJ_P, MTC_P, TVC_P, HKM_P, NTE_P, DMT_P, CSK_P, OTS_P, TOM_P,
                        QSS_P, RVZ_P, FNW_P, VGC_P, WKI_P, FTL_P, SNS_P, SBO_P, RSR_P, HDL_P, PLL_P, TNG_P, LMR_P,
                        TRB_P, SMY_P, DVR_P, TMB_P, TCD_P, VMC_P, CLO_P, TSP_P, TMC_P, HON_P, CTF_K])
    Primary.align["Exotic"] = 'l'
    Primary.align["Element"] = 'l'
    Primary.align["Weapon Type"] = 'l'
    Primary.align["Kills"] = 'r'
    Primary.align["Precision Kills"] = 'r'
    Primary.reversesort = True
    print(Primary.get_string(sortby="Kills", start=0, end=5))

    Special = PrettyTable()
    Special.add_column("Exotic",
                       ["The Chaperone", "Izanagi's Burden", "Arbalest", "Bastion", "Witherhoard", "Ager's Scepter",
                        "Forerunner", "Conditional Finality", "The Navigator", "Coldheart", "Merciless", "Borealis",
                        "Prometheus Lens", "Telesto", "Wavesplitter", "Lord of Wolves", "Jötunn", "Eriana's Vow",
                        "Divinity", "The Fourth Horseman", "Ruinous Effigy", "Duality", "Cloudstrike",
                        "Lorentz Driver", "Edge of Concurrence", "Edge of Action", "Edge of Intent",
                        "Dead Messenger", "Delicate Tomb", "Vexcalibur"])
    Special.add_column("Element", ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis", "Kinetic",
                                   "Stasis/Solar", "Strand", "Arc", "Solar", "Arc/Void/Solar", "Solar", "Void", "Void",
                                   "Solar", "Solar", "Solar", "Arc", "Arc", "Void", "Solar", "Arc", "Void", "Arc",
                                   "Void", "Solar", "Arc/Void/Solar", "Arc", "Void"])
    Special.add_column("Weapon Type", ["Shotgun", "Sniper Rifle", "Linear Fusion Rifle", "Fusion Rifle",
                                       "Grenade Launcher", "Trace Rifle", "Sidearm", "Shotgun", "Trace Rifle",
                                       "Trace Rifle", "Fusion Rifle", "Sniper Rifle", "Trace Rifle", "Fusion Rifle",
                                       "Trace Rifle", "Shotgun", "Fusion Rifle", "Hand Cannon", "Trace Rifle",
                                       "Shotgun", "Trace Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle",
                                       "Glaive", "Glaive", "Glaive", "Grenade Launcher", "Fusion Rifle", "Glaive"])
    Special.add_column("Kills",
                       [CPR_K, IZB_K, ABL_K, BSN_K, WTH_K, ASP_K, FRN_K, CDF_K, NVG_K, CDH_K, MCL_K, BEL_K, PML_K,
                        TLT_K, WVP_K, LOW_K, JTN_K, EIV_K, DVN_K, TFH_K, RNE_K, DLT_K, CDS_K, LRD_K, EOC_K, EOA_K,
                        EOI_K, DMS_K, DCT_K, VCB_K])
    Special.add_column("Precision Kills",
                       [CPR_P, IZB_P, ABL_P, BSN_P, WTH_P, ASP_P, FRN_P, CDF_P, NVG_P, CDH_P, MCL_P, BEL_P,
                        PML_P, TLT_P, WVP_P, LOW_P, JTN_P, EIV_P, DVN_P, TFH_P, RNE_P, DLT_P, CDS_P, LRD_P,
                        EOC_P, EOA_P, EOI_P, DMS_P, DCT_P, VCB_P])
    Special.align["Exotic"] = 'l'
    Special.align["Element"] = 'l'
    Special.align["Weapon Type"] = 'l'
    Special.align["Kills"] = 'r'
    Special.align["Precision Kills"] = 'r'
    Special.reversesort = True
    print(Special.get_string(sortby="Kills", start=0, end=5))

    Heavy = PrettyTable()
    Heavy.add_column("Exotic",
                     ["The Prospector", "The Wardcliff Coil", "Tractor Cannon", "Legend of Acrius", "D.A.R.C.I.",
                      "The Colony", "Worldline Zero", "Sleeper Simulant", "One Thousand Voices", "Two-Tailed Fox",
                      "Black Talon", "The Queenbreaker", "Thunderlord", "Anarchy", "Leviathan's Breath",
                      "Xenophage", "Deathbringer", "Heir Apparent", "Salvation's Grip", "Eyes of Tomorrow",
                      "The Lament", "Gjallarhorn", "Parasite", "Grand Overture", "Heartshadow",
                      "Deterministic Chaos", "Winterbite", "Truth", "Whisper of the Worm"])
    Heavy.add_column("Element", ["Arc", "Arc", "Void", "Arc", "Arc", "Void", "Arc", "Solar", "Solar", "Arc/Void/Solar",
                                 "Void", "Arc", "Arc", "Arc", "Void", "Solar", "Void", "Solar", "Stasis", "Solar",
                                 "Solar", "Solar", "Solar", "Arc", "Void", "Void", "Stasis", "Void", "Void"])
    Heavy.add_column("Weapon Type", ["Grenade Launcher", "Rocket Launcher", "Shotgun", "Shotgun", "Sniper Rifle",
                                     "Grenade Launcher", "Sword", "Linear Fusion Rifle", "Fusion Rifle",
                                     "Rocket Launcher", "Sword", "Linear Fusion Rifle", "Machine Gun",
                                     "Grenade Launcher", "Combat Bow", "Machine Gun", "Rocket Launcher", "Machine Gun",
                                     "Grenade Launcher", "Rocket Launcher", "Sword", "Rocket Launcher",
                                     "Grenade Launcher", "Machine Gun", "Sword", "Machine Gun", "Glaive",
                                     "Rocket Launcher", "Sniper Rifle"])
    Heavy.add_column("Kills",
                     [PST_K, WCC_K, TCC_K, LOA_K, DRC_K, CLN_K, WLZ_K, SPS_K, OKV_K, TTF_K, BKT_K, QNB_K, TDL_K,
                      ARK_K, LVB_K, XNP_K, DBG_K, HAP_K, SVG_K, EOT_K, LMT_K, GLH_K, PRS_K, GOT_K, HSD_K, DTC_K,
                      WTB_K, TUH_K, WOW_K])
    Heavy.add_column("Precision Kills",
                     [PST_P, WCC_P, TCC_P, LOA_P, DRC_P, CLN_P, WLZ_P, SPS_P, OKV_P, TTF_P, BKT_P, QNB_P,
                      TDL_P, ARK_P, LVB_P, XNP_P, DBG_P, HAP_P, SVG_P, EOT_P, LMT_P, GLH_P, PRS_P, GOT_P,
                      HSD_P, DTC_P, WTB_P, TUH_P, WOW_P])
    Heavy.align["Exotic"] = 'l'
    Heavy.align["Element"] = 'l'
    Heavy.align["Weapon Type"] = 'l'
    Heavy.align["Kills"] = 'r'
    Heavy.align["Precision Kills"] = 'r'
    Heavy.reversesort = True
    print(Heavy.get_string(sortby="Kills", start=0, end=5))

    Full = PrettyTable()
    Full.add_column("Exotic", ["Sweet Business", "Strum", "Vigilance Wing", "Rat King", "MIDA Multi-Tool", "Crimson",
                               "The Jade Rabbit", "The Huckleberry", "SUROS Regime", "Cerberus+1", "Wish-Ender",
                               "Malfeasance", "Ace of Spades", "The Last Word", "Thorn", "Outbreak Perfected",
                               "Lumina", "Bad Juju", "Monte Carlo", "Traveler's Chosen", "Hawkmoon",
                               "No Time to Explain", "Dead Man's Tale", "Cryosthethesia 77K", "Osteo Striga",
                               "Touch of Malice",
                               "Quicksilver Storm", "Revision Zero", "Final Warning", "Verglas Curve",
                               "Wicked Implement", "Fighting Lion", "Sunshot", "Skyburner's Oath", "Riskrunner",
                               "Hard Light",
                               "Polaris Lance", "Trinity Ghoul", "Le Monarque", "Tarrabah", "Symmetry", "Devil's Ruin",
                               "Tommy's Matchbook", "Ticuu's Divination", "Vex Mythoclast", "Collective Obligation",
                               "Trespasser",
                               "The Manticore", "Hierarchy of Needs", "Centrifuse", "The Chaperone", "Izanagi's Burden",
                               "Arbalest", "Bastion", "Witherhoard", "Ager's Scepter",
                               "Forerunner", "Conditional Finality", "The Navigator", "Coldheart", "Merciless",
                               "Borealis", "Prometheus Lens", "Telesto", "Wavesplitter", "Lord of Wolves", "Jötunn",
                               "Eriana's Vow",
                               "Divinity", "The Fourth Horseman", "Ruinous Effigy", "Duality", "Cloudstrike",
                               "Lorentz Driver", "Edge of Concurrence", "Edge of Action", "Edge of Intent",
                               "Dead Messenger", "Delicate Tomb", "Vexcalibur", "The Prospector",
                               "The Wardcliff Coil", "Tractor Cannon", "Legend of Acrius", "D.A.R.C.I.",
                               "The Colony", "Worldline Zero", "Sleeper Simulant", "One Thousand Voices",
                               "Two-Tailed Fox", "Black Talon", "The Queenbreaker", "Thunderlord", "Anarchy",
                               "Leviathan's Breath",
                               "Xenophage", "Deathbringer", "Heir Apparent", "Salvation's Grip", "Eyes of Tomorrow",
                               "The Lament", "Gjallarhorn", "Parasite", "Grand Overture", "Heartshadow",
                               "Deterministic Chaos", "Winterbite", "Truth", "Whisper of the Worm"])
    Full.add_column("Element", ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis",
                                "Kinetic", "Kinetic", "Kinetic/Strand", "Kinetic", "Strand", "Stasis", "Stasis",
                                "Void", "Solar", "Solar", "Arc", "Arc/Void/Solar", "Solar", "Arc", "Void", "Solar",
                                "Arc", "Solar", "Solar", "Solar", "Solar", "Void", "Arc", "Void", "Solar", "Arc",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis", "Kinetic",
                                "Stasis/Solar", "Strand", "Arc", "Solar", "Arc/Void/Solar", "Solar", "Void", "Void",
                                "Solar", "Solar", "Solar", "Arc", "Arc", "Void", "Solar", "Arc", "Void", "Arc",
                                "Void", "Solar", "Arc/Void/Solar", "Arc", "Void", "Arc", "Arc", "Void", "Arc", "Arc",
                                "Void", "Arc", "Solar", "Solar", "Arc/Void/Solar",
                                "Void", "Arc", "Arc", "Arc", "Void", "Solar", "Void", "Solar", "Stasis", "Solar",
                                "Solar", "Solar", "Solar", "Arc", "Void", "Void", "Stasis", "Void", "Void"])
    Full.add_column("Weapon Type", ["Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sidearm", "Scout Rifle",
                                    "Hand Cannon", "Scout Rifle", "Submachine Gun", "Auto Rifle", "Auto Rifle",
                                    "Combat Bow", "Hand Cannon", "Hand Cannon", "Hand Cannon", "Hand Cannon",
                                    "Pulse Rifle", "Hand Cannon", "Pulse Rifle", "Auto Rifle", "Sidearm",
                                    "Hand Cannon", "Pulse Rifle", "Scout Rifle", "Sidearm", "Submachine Gun",
                                    "Scout Rifle", "Auto Rifle", "Pulse Rifle", "Sidearm", "Combat Bow",
                                    "Scout Rifle", "Grenade Launcher", "Hand Cannon", "Scout Rifle",
                                    "Submachine Gun", "Auto Rifle", "Scout Rifle", "Combat Bow", "Combat Bow",
                                    "Submachine Gun", "Scout Rifle", "Sidearm", "Auto Rifle", "Combat Bow",
                                    "Fusion Rifle", "Pulse Rifle", "Sidearm", "Submachine Gun", "Combat Bow",
                                    "Auto Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle", "Fusion Rifle",
                                    "Grenade Launcher", "Trace Rifle", "Sidearm", "Shotgun", "Trace Rifle",
                                    "Trace Rifle", "Fusion Rifle", "Sniper Rifle", "Trace Rifle", "Fusion Rifle",
                                    "Trace Rifle", "Shotgun", "Fusion Rifle", "Hand Cannon", "Trace Rifle",
                                    "Shotgun", "Trace Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle",
                                    "Glaive", "Glaive", "Glaive", "Grenade Launcher", "Fusion Rifle", "Glaive",
                                    "Grenade Launcher", "Rocket Launcher", "Shotgun", "Shotgun", "Sniper Rifle",
                                    "Grenade Launcher", "Sword", "Linear Fusion Rifle", "Fusion Rifle",
                                    "Rocket Launcher", "Sword", "Linear Fusion Rifle", "Machine Gun",
                                    "Grenade Launcher", "Combat Bow", "Machine Gun", "Rocket Launcher", "Machine Gun",
                                    "Grenade Launcher", "Rocket Launcher", "Sword", "Rocket Launcher",
                                    "Grenade Launcher", "Machine Gun", "Sword", "Machine Gun", "Glaive",
                                    "Rocket Launcher", "Sniper Rifle"])
    Full.add_column("Kills",
                    [SWB_K, STR_K, VIG_K, RTK_K, MMT_K, CRM_K, JDR_K, HKB_K, SRR_K, CBS_K, WHE_K, MFC_K, AOS_K,
                     TLW_K, TRN_K, OBP_K, LMN_K, BJJ_K, MTC_K, TVC_K, HKM_K, NTE_K, DMT_K, CSK_K, OTS_K, TOM_K, QSS_K,
                     RVZ_K, FNW_K, VGC_K, WKI_K, FTL_K, SNS_K, SBO_K, RSR_K, HDL_K, PLL_K, TNG_K, LMR_K, TRB_K, SMY_K,
                     DVR_K, TMB_K, TCD_K, VMC_K, CLO_K, TSP_K, TMC_K, HON_K, CTF_K, CPR_K, IZB_K, ABL_K, BSN_K, WTH_K,
                     ASP_K, FRN_K, CDF_K, NVG_K, CDH_K, MCL_K, BEL_K, PML_K, TLT_K, WVP_K, LOW_K, JTN_K, EIV_K, DVN_K,
                     TFH_K, RNE_K, DLT_K, CDS_K, LRD_K, EOC_K, EOA_K, EOI_K, DMS_K, DCT_K, VCB_K, PST_K, WCC_K,
                     TCC_K, LOA_K, DRC_K, CLN_K, WLZ_K, SPS_K, OKV_K, TTF_K, BKT_K, QNB_K, TDL_K, ARK_K, LVB_K, XNP_K,
                     DBG_K, HAP_K, SVG_K, EOT_K, LMT_K, GLH_K, PRS_K, GOT_K, HSD_K, DTC_K, WTB_K, TUH_K, WOW_K])
    Full.add_column("Precision Kills",
                    [SWB_P, STR_P, VIG_P, RTK_P, MMT_P, CRM_P, JDR_P, HKB_P, SRR_P, CBS_P, WHE_P, MFC_P, AOS_P,
                     TLW_P, TRN_P, OBP_P, LMN_P, BJJ_P, MTC_P, TVC_P, HKM_P, NTE_P, DMT_P, CSK_P, OTS_P, TOM_P,
                     QSS_P, RVZ_P, FNW_P, VGC_P, WKI_P, FTL_P, SNS_P, SBO_P, RSR_P, HDL_P, PLL_P, TNG_P, LMR_P,
                     TRB_P, SMY_P, DVR_P, TMB_P, TCD_P, VMC_P, CLO_P, TSP_P, TMC_P, HON_P, CTF_K, CPR_P, IZB_P,
                     ABL_P, BSN_P, WTH_P, ASP_P, FRN_P, CDF_P, NVG_P, CDH_P, MCL_P, BEL_P, PML_P, TLT_P, WVP_P,
                     LOW_P, JTN_P, EIV_P, DVN_P, TFH_P, RNE_P, DLT_P, CDS_P, LRD_P, EOC_P, EOA_P, EOI_P, DMS_P,
                     DCT_P, VCB_P, PST_P, WCC_P, TCC_P, LOA_P, DRC_P, CLN_P, WLZ_P, SPS_P, OKV_P, TTF_P, BKT_P,
                     QNB_P, TDL_P, ARK_P, LVB_P, XNP_P, DBG_P, HAP_P, SVG_P, EOT_P, LMT_P, GLH_P, PRS_P, GOT_P,
                     HSD_P, DTC_P, WTB_P, TUH_P, WOW_P])
    Full.align["Exotic"] = 'l'
    Full.align["Element"] = 'l'
    Full.align["Weapon Type"] = 'l'
    Full.align["Kills"] = 'r'
    Full.align["Precision Kills"] = 'r'
    Full.reversesort = True
    print(Full.get_string(sortby="Kills", start=0, end=10))

