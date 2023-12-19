# Thomas McGinley
# Started 12/17/2023
# Last Updated 12/18/2023

# Gathers exotic information about each desired player, cleans the data, and generates JSON files with relevant information


import json
import requests
 
def getWeaponFromId(id):
    idDict = {
        1345867570: 'Sweet Business',
        2907129556: 'Sturm',
        3628991659: 'Vigilance Wing',
        2362471601: 'Rat King',
        1331482397: 'MIDA Multi-Tool',
        3437746471: 'Crimson',
        3844694310: 'Jade Rabbit',
        2286143274: 'Huckleberry',
        2856683562: 'SUROS Regime',
        1541131350: 'Cerberus+1',
        814876684: 'Wish Ender',
        204878059: 'Malfeasance',
        347366834: 'Ace of Spades',
        3413860062: 'The Chaperone',
        3211806999: "Izanagi's Burden",
        1364093401: 'The Last Word',
        2130065553: 'Arbalest',
        3973202132: 'Thorn',
        400096939: 'Outbreak Perfected',
        3512014804: 'Lumina',
        2816212794: 'Bad Juju',
        4068264807: 'Monte Carlo',
        2415517654: 'Bastion',
        2357297366: 'Witherhoard',
        1853180924: "Traveler's Chosen",
        1594120904: 'No Time to Explain',
        3654674561: "Dead Man's Tale",
        603721696: 'Cryosthethesia 77K',
        1833195496: "Ager's Scepter",
        2179048386: 'Forerunner',
        46524085: 'Osteo Striga',
        1802135586: 'Touch of Malice',
        4293613902: 'Quicksilver Storm',
        1473821207: 'Revision Zero',
        3121540812: 'Final Warning',
        3371017761: 'Conditional Finality',
        3659414143: 'Verglas Curve',
        940371471: 'Wicked Implement',
        1441805468: 'The Navigator',
        1345867571: 'Coldheart',
        4190156464: 'Merciless',
        3549153978: 'Fighting Lion',
        2907129557: 'Sunshot',
        3628991658: 'Graviton Lance',
        4255268456: "Skyburner's Oath",
        3141979347: 'Borealis',
        3089417789: 'Riskrunner',
        4124984448: 'Hard Light',
        19024058: 'Prometheus Lens',
        2208405142: 'Telesto',
        3413074534: 'Polaris Lance',
        814876685: 'Trinity Ghoul',
        1852863732: 'Wavesplitter',
        3413860063: 'Lord of Wolves',
        3588934839: 'Le Monarque',
        417164956: 'Jötunn',
        3110698812: 'Tarrabah',
        3524313097: "Eriana's Vow",
        4103414242: 'Divinity',
        4017959782: 'Symmetry',
        3824106094: "Devil's Ruin",
        776191470: "Tommy's Matchbook",
        1665952087: "The Fourth Horseman",
        1363238943: 'Ruinous Effigy',
        3460576091: 'Duality',
        2603483885: 'Cloudstrike',
        3260753130: "Ticuu's Divination",
        4289226715: 'Vex Mythoclast',
        3761898871: 'Lorentz Driver',
        14194600: 'Edge of Intent',
        2812324401: 'Dead Messenger',
        3505113722: 'Collective Obligation',
        374573733: 'Delicate Tomb',
        1234150730: 'The Trespasser',
        219145368: 'The Manticore',
        4174431791: 'Hierarchy of Needs',
        3118061005: 'Vexcalibur',
        1912669214: 'Centrifuse',
        1508896098: 'Wardcliff Coil',
        3580904581: 'Tractor Cannon',
        3580904580: 'Legend of Acrius',
        1744115122: 'Legend of Acrius',
        3141979346: 'D.A.R.C.I',
        3899270607: 'The Colony',
        1864563948: 'Worldline Zero',
        4036115577: 'Sleeper Simulant',
        2069224589: 'One Thousand Voices',
        2694576561: 'Two-Tailed Fox',
        3766045777: 'Black Talon',
        2044500762: 'The Queenbreaker',
        3325463374: 'Thunderlord',
        2376481550: 'Anarchy',
        2591746970: "Leviathan's Breath",
        1395261499: 'Xenopahge',
        2232171099: 'Deathbringer',
        2084878005: 'Heir Apparent',
        370712896: "Salvation's Grip",
        2399110176: 'Eyes of Tomorrow',
        3487253372: 'Lament',
        1363886209: 'Gjallarhorn',
        2812324400: 'Parasite',
        1763584999: 'Grand Overture',
        3664831848: 'Heartshadow',
        449318888: 'Deterministic Chaos',
        3118061004: 'Winterbite',
        1201830623: 'Truth',
        1891561814: 'Whisper of the Worm',
        17096506: "Dragon's Breath",
        3561203890: "Tessellation",
        3886719505: "Buried Bloodline",
        1034055198: "Necrochasm",
        3821409356: "Ex Diris",
        3856705927: "Hawkmoon",
        3549153979: "The Prospector",
        2188764214: "Dead Man's Tale"
    }
    return idDict.get(id)



def weaponData():
    dictionary={
        'Sweet Business':{'kills':0,'precision':0},
        'Sturm':{'kills':0,'precision':0},
        'Vigilance Wing':{'kills':0,'precision':0},
        'Rat King':{'kills':0,'precision':0},
        'MIDA Multi-Tool':{'kills':0,'precision':0},
        'Crimson':{'kills':0,'precision':0},
        'Jade Rabbit':{'kills':0,'precision':0},
        'Huckleberry':{'kills':0,'precision':0},
        'SUROS Regime':{'kills':0,'precision':0},
        'Cerberus+1':{'kills':0,'precision':0},
        'Wish Ender':{'kills':0,'precision':0},
        'Malfeasance':{'kills':0,'precision':0},
        'Ace of Spades':{'kills':0,'precision':0},
        'The Chaperone':{'kills':0,'precision':0},
        "Izanagi's Burden":{'kills':0,'precision':0},
        'The Last Word':{'kills':0,'precision':0},
        'Arbalest':{'kills':0,'precision':0},
        'Thorn':{'kills':0,'precision':0},
        'Outbreak Perfected':{'kills':0,'precision':0},
        'Lumina':{'kills':0,'precision':0},
        'Bad Juju':{'kills':0,'precision':0},
        'Monte Carlo':{'kills':0,'precision':0},
        'Bastion':{'kills':0,'precision':0},
        'Witherhoard':{'kills':0,'precision':0},
        "Traveler's Chosen":{'kills':0,'precision':0},
        'No Time to Explain':{'kills':0,'precision':0},
        "Dead Man's Tale":{'kills':0,'precision':0},
        'Cryosthethesia 77K':{'kills':0,'precision':0},
        "Ager's Scepter":{'kills':0,'precision':0},
        'Forerunner':{'kills':0,'precision':0},
        'Osteo Striga':{'kills':0,'precision':0},
        'Touch of Malice':{'kills':0,'precision':0},
        'Quicksilver Storm':{'kills':0,'precision':0},
        'Revision Zero':{'kills':0,'precision':0},
        'Final Warning':{'kills':0,'precision':0},
        'Conditional Finality':{'kills':0,'precision':0},
        'Verglas Curve':{'kills':0,'precision':0},
        'Wicked Implement':{'kills':0,'precision':0},
        'The Navigator':{'kills':0,'precision':0},
        'Coldheart':{'kills':0,'precision':0},
        'Merciless':{'kills':0,'precision':0},
        'Fighting Lion':{'kills':0,'precision':0},
        'Sunshot':{'kills':0,'precision':0},
        'Graviton Lance':{'kills':0,'precision':0},
        "Skyburner's Oath":{'kills':0,'precision':0},
        'Borealis':{'kills':0,'precision':0},
        'Riskrunner':{'kills':0,'precision':0},
        'Hard Light':{'kills':0,'precision':0},
        'Prometheus Lens':{'kills':0,'precision':0},
        'Telesto':{'kills':0,'precision':0},
        'Polaris Lance':{'kills':0,'precision':0},
        'Trinity Ghoul':{'kills':0,'precision':0},
        'Wavesplitter':{'kills':0,'precision':0},
        'Lord of Wolves':{'kills':0,'precision':0},
        'Le Monarque':{'kills':0,'precision':0},
        'Jötunn':{'kills':0,'precision':0},
        'Tarrabah':{'kills':0,'precision':0},
        "Eriana's Vow":{'kills':0,'precision':0},
        'Divinity':{'kills':0,'precision':0},
        'Symmetry':{'kills':0,'precision':0},
        "Devil's Ruin":{'kills':0,'precision':0},
        "Tommy's Matchbook":{'kills':0,'precision':0},
        "The Fourth Horseman":{'kills':0,'precision':0},
        'Ruinous Effigy':{'kills':0,'precision':0},
        'Duality':{'kills':0,'precision':0},
        'Cloudstrike':{'kills':0,'precision':0},
        "Ticuu's Divination":{'kills':0,'precision':0},
        'Vex Mythoclast':{'kills':0,'precision':0},
        'Lorentz Driver':{'kills':0,'precision':0},
        'Edge of Intent':{'kills':0,'precision':0},
        'Dead Messenger':{'kills':0,'precision':0},
        'Collective Obligation':{'kills':0,'precision':0},
        'Delicate Tomb':{'kills':0,'precision':0},
        'The Trespasser':{'kills':0,'precision':0},
        'The Manticore':{'kills':0,'precision':0},
        'Hierarchy of Needs':{'kills':0,'precision':0},
        'Vexcalibur':{'kills':0,'precision':0},
        'Centrifuse':{'kills':0,'precision':0},
        'Wardcliff Coil':{'kills':0,'precision':0},
        'Tractor Cannon':{'kills':0,'precision':0},
        'Legend of Acrius':{'kills':0,'precision':0},
        'D.A.R.C.I':{'kills':0,'precision':0},
        'The Colony':{'kills':0,'precision':0},
        'Worldline Zero':{'kills':0,'precision':0},
        'Sleeper Simulant':{'kills':0,'precision':0},
        'One Thousand Voices':{'kills':0,'precision':0},
        'Two-Tailed Fox':{'kills':0,'precision':0},
        'Black Talon':{'kills':0,'precision':0},
        'The Queenbreaker':{'kills':0,'precision':0},
        'Thunderlord':{'kills':0,'precision':0},
        'Anarchy':{'kills':0,'precision':0},
        "Leviathan's Breath":{'kills':0,'precision':0},
        'Xenopahge':{'kills':0,'precision':0},
        'Deathbringer':{'kills':0,'precision':0},
        'Heir Apparent':{'kills':0,'precision':0},
        "Salvation's Grip":{'kills':0,'precision':0},
        'Eyes of Tomorrow':{'kills':0,'precision':0},
        'Lament':{'kills':0,'precision':0},
        'Gjallarhorn':{'kills':0,'precision':0},
        'Parasite':{'kills':0,'precision':0},
        'Grand Overture':{'kills':0,'precision':0},
        'Heartshadow':{'kills':0,'precision':0},
        'Deterministic Chaos':{'kills':0,'precision':0},
        'Winterbite':{'kills':0,'precision':0},
        'Truth':{'kills':0,'precision':0},
        'Whisper of the Worm':{'kills':0,'precision':0},
        "Dragon's Breath":{'kills':0,'precision':0},
        "Tessellation":{'kills':0,'precision':0},
        "Buried Bloodline":{'kills':0,'precision':0},
        "Necrochasm":{'kills':0,'precision':0},
        "Ex Diris":{'kills':0,'precision':0},
        "Hawkmoon":{'kills':0,'precision':0},
        "The Prospector":{'kills':0,'precision':0}
    }
    return dictionary
    
    

def getExoticData(memType, memId, charId1, charId2, charId3):
    charIds = [charId1,charId2,charId3]
    combinedExoticData = {"Response": []}
    for charId in charIds:

        url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Account/{memId}/Character/" \
            f"{charId}/Stats/UniqueWeapons/"
        payload = {}
        header = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=header, data=payload)
        
        exoticData = json.loads(response.content)
        
        combinedExoticData["Response"].append(exoticData["Response"])
    return combinedExoticData
    
    
    
def compileData(exoticData):
    dataDictionary = weaponData()
    #exoticData["Response"][value 0-2]["weapons"][num]["referenceId"] = reference Id
    #exoticData["Response"][charNum]["weapons"][num]["values"]["uniqueWeaponKills"]["basic"]["value"] = kills
    #exoticData["Response"][charNum]["weapons"][num]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"] = precision kills
    for charNum in range(0,3):
        weaponCount = len(exoticData["Response"][charNum]["weapons"])
        for num in range(0,weaponCount):
            exoticName = getWeaponFromId(exoticData["Response"][charNum]["weapons"][num]['referenceId'])
            exoticKills = exoticData["Response"][charNum]["weapons"][num]["values"]["uniqueWeaponKills"]["basic"]["value"]
            exoticPrecision = exoticData["Response"][charNum]["weapons"][num]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
            # print(str(exoticName) + "\t" + str(exoticData["Response"][charNum]["weapons"][num]['referenceId']))
            # print(exoticKills)
            # print(exoticPrecision)
            
            dataDictionary[exoticName]["kills"] += exoticKills
            dataDictionary[exoticName]["precision"] += exoticPrecision
    return dataDictionary


def compileClanData(playerDataList):
    dataDictionary = weaponData()
    
    for player in playerDataList:
        for exoticName in player:
            
            exoticKills = player[exoticName]['kills']
            exoticPrecision = player[exoticName]['precision']
            
            dataDictionary[exoticName]['kills'] +=exoticKills
            dataDictionary[exoticName]['precision'] += exoticPrecision
    return dataDictionary
  
  
def writeToDirectory(playerDict,name):
    f = open(f'./data/{name}Exotics.json', 'w')
    playerFile = json.dumps(playerDict, indent = 2)
    f.write(playerFile)
    f.close()
  


thomasExoticDataRaw = getExoticData(1,4611686018444441571,2305843009265786295,2305843009283965144,2305843009569534739)
thomasExoticDataClean = compileData(thomasExoticDataRaw)
writeToDirectory(thomasExoticDataClean, "Thomas")


douglasExoticDataRaw = getExoticData(1,4611686018434621591,2305843009293915719,2305843009301374530,2305843010083874501)
douglasExoticDataClean = compileData(douglasExoticDataRaw)
writeToDirectory(douglasExoticDataClean,"Douglas")


markExoticDataRaw = getExoticData(1,4611686018432221111,2305843009348154555,2305843009668854600,2305843009802904121)
markExoticDataClean = compileData(markExoticDataRaw)
writeToDirectory(markExoticDataClean, "Mark")


connorExoticDataRaw = getExoticData(1,4611686018450697084,2305843009644414176,2305843009663894341,2305843009703275457)
connorExoticDataClean = compileData(connorExoticDataRaw)
writeToDirectory(connorExoticDataClean, "Connor")


jackExoticDataRaw = getExoticData(2,4611686018469231992,2305843009268771475,2305843009891864023,2305843009890274343)
jackExoticDataClean = compileData(jackExoticDataRaw)
writeToDirectory(jackExoticDataClean,"Jack")


hunterExoticDataRaw = getExoticData(3,4611686018476416864,2305843009359734078,2305843009359365362,2305843009756404411)
hunterExoticDataClean = compileData(hunterExoticDataRaw)
writeToDirectory(hunterExoticDataClean,"Hunter")


cameronExoticDataRaw = getExoticData(3,4611686018501646188,2305843009624174508,2305843009683284492,2305843009683284493)
cameronExoticDataClean = compileData(cameronExoticDataRaw)
writeToDirectory(cameronExoticDataClean,"Cameron")


kadeExoticDataRaw = getExoticData(1,4611686018451886498,2305843009264637524,2305843009264637527,2305843010322954573)
kadeExoticDataClean = compileData(kadeExoticDataRaw)
writeToDirectory(kadeExoticDataClean, "Kade")


playerDataList = [thomasExoticDataClean,douglasExoticDataClean,markExoticDataClean,connorExoticDataClean,jackExoticDataClean,hunterExoticDataClean,cameronExoticDataClean,kadeExoticDataClean]
clanExoticDataClean = compileClanData(playerDataList)
writeToDirectory(clanExoticDataClean, "Clan")