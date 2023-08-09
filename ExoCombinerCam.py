import json

from prettytable import PrettyTable


def ExoCombinerCam():
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

    with open('Exotics_18.json') as f:
        data1 = json.load(f)
    with open('Exotics_19.json') as f:
        data2 = json.load(f)
    with open('Exotics_20.json') as f:
        data3 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]

    exotic_json = {"Response": []}

    exotic_json['Response'].append(items1)
    exotic_json["Response"].append(items2)
    exotic_json["Response"].append(items3)

    with open('exotic.json', "w") as f:
        f.write(json.dumps(exotic_json, indent=2))

    exotic_len_1 = len(exotic_json["Response"][0]['weapons'])
    exotic_len_2 = len(exotic_json["Response"][1]['weapons'])
    exotic_len_3 = len(exotic_json["Response"][2]['weapons'])

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
        elif ID == 4103414242:
            Exotic = 'Divinity'
            DVN_K += Kills
            DVN_P += Precision
        elif ID == 603721696:
            Exotic = 'Cryosthethesia 77K'
            CSK_K += Kills
            CSK_P += Precision
        elif ID == 4190156464:
            Exotic = "Merciless"
            MCL_K += Kills
            MCL_P += Precision
        elif ID == 3549153978:
            Exotic = 'Fighting Lion'
            FTL_K += Kills
            FTL_P += Precision

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
    Full.add_column("Kills",
                    [SWB_K, STR_K, VIG_K, RTK_K, MMT_K, CRM_K, JDR_K, HKB_K, SRR_K, CBS_K, WHE_K, MFC_K, AOS_K,
                     TLW_K, TRN_K, OBP_K, LMN_K, BJJ_K, MTC_K, TVC_K, HKM_K, NTE_K, DMT_K, CSK_K, OTS_K, TOM_K, QSS_K,
                     RVZ_K, FNW_K, VGC_K, WKI_K, FTL_K, SNS_K, SBO_K, RSR_K, HDL_K, PLL_K, TNG_K, LMR_K, TRB_K, SMY_K,
                     DVR_K, TMB_K, TCD_K, VMC_K, CLO_K, TSP_K, TMC_K, HON_K, CTF_K, CPR_K, IZB_K, ABL_K, BSN_K, WTH_K,
                     ASP_K, FRN_K, CDF_K, NVG_K, CDH_K, MCL_K, BEL_K, PML_K, TLT_K, WVP_K, LOW_K, JTN_K, EIV_K, DVN_K,
                     TFH_K, RNE_K, DLT_K, CDS_K, LRD_K, EOC_K, EOA_K, EOI_K, DMS_K, DCT_K, VCB_K, PST_K, WCC_K,
                     TCC_K, LOA_K, DRC_K, CLN_K, WLZ_K, SPS_K, OKV_K, TTF_K, BKT_K, QNB_K, TDL_K, ARK_K, LVB_K, XNP_K,
                     DBG_K, HAP_K, SVG_K, EOT_K, LMT_K, GLH_K, PRS_K, GOT_K, HSD_K, DTC_K, WTB_K, TUH_K, WOW_K])

    Full.align["Exotic"] = 'l'
    Full.align["Kills"] = 'r'
    Full.reversesort = True
    print(Full.get_string(sortby="Kills", start=0, end=10))