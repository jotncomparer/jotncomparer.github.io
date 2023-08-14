import json

from prettytable import PrettyTable


def ExoCombinerCon():
    class Exotic:
        def __init__(self, exotic_id, exotic_name):
            self.id = exotic_id
            self.name = exotic_name
            self.kills = 0
            self.prec = 0

        def weaponData(self, kills, prec):
            self.kills += Kills
            self.prec += Precision

    sweetBusiness = Exotic(1345867570, 'Sweet Business')
    strum = Exotic(2907129556, 'Strum')
    vigilance = Exotic(3628991659, 'Vigilance Wing')
    ratKing = Exotic(2362471601, 'Rat King')
    mida = Exotic(1331482397, 'MIDA Multi-Tool')
    crimson = Exotic(3437746471, 'Crimson')
    rabbit = Exotic(3844694310, 'Jade Rabbit')
    huckle = Exotic(2286143274, 'Huckleberry')
    suros = Exotic(2856683562, 'SUROS Regime')
    cerberus = Exotic(1541131350, 'Cerberus+1')
    wish = Exotic(814876684, 'Wish Ender')
    malfease = Exotic(204878059, 'Malfeasance')
    ace = Exotic(347366834, 'Ace of Spaced')
    chaperone = Exotic(3413860062, 'The Chaperone')
    izan = Exotic(3211806999, "Izanagi's Burden")
    lastword = Exotic(1364093401, 'The Last Word')
    arbalest = Exotic(2130065553, 'Arbalest')
    thorn = Exotic(3973202132, 'Thorn')
    outbreak = Exotic(400096939, 'Outbreak Perfected')
    lumina = Exotic(3512014804, 'Lumina')
    juju = Exotic(2816212794, 'Bad Juju')
    monte = Exotic(4068264807, 'Monte Carlo')
    bastion = Exotic(2415517654, 'Bastion')
    witherhoard = Exotic(2357297366, 'Witherhoard')
    chosen = Exotic(1853180924, "Traveler's Chosen")
    hawkmoon = Exotic(3856705927, 'Hawkmoon')
    notime = Exotic(1594120904, 'No Time to Explain')
    deadmans = Exotic(3654674561, "Dead Man's Tale")
    cryo = Exotic(603721696, 'Cryosthethesia 77K')
    agers = Exotic(1833195496, "Ager's Scepter")
    forerunner = Exotic(2179048386, 'Forerunner')
    osteo = Exotic(46524085, 'Osteo Striga')
    touch = Exotic(1802135586, 'Touch of Malice')
    quicksilver = Exotic(4293613902, 'Quicksilver Storm')
    revision = Exotic(1473821207, 'Revision Zero')
    warning = Exotic(3121540812, 'Final Warning')
    finality = Exotic(3371017761, 'Conditional Finality')
    verglas = Exotic(3659414143, 'Verglas Curve')
    wicked = Exotic(940371471, 'Wicked Implement')
    navigator = Exotic(1441805468, 'The Navigator')
    coldheart = Exotic(1345867571, 'Coldheart')
    merciless = Exotic(4190156464, 'Merciless')
    fighting = Exotic(3549153978, 'Fighting Lion')
    sunshot = Exotic(2907129557, 'Sunshot')
    graviton = Exotic(3628991658, 'Graviton Lance')
    skyburner = Exotic(4255268456, "Skyburner's Oath")
    bore = Exotic(3141979347, 'Borealis')
    riskrunner = Exotic(3089417789, 'Riskrunner')
    hardlight = Exotic(4124984448, 'Hard Light')
    prometheus = Exotic(19024058, 'Prometheus Lens')
    telesto = Exotic(2208405142, 'Telesto')
    polaris = Exotic(3413074534, 'Polaris Lance')
    trinity = Exotic(814876685, 'Trinity Ghoul')
    wavesplit = Exotic(1852863732, 'Wavesplitter')
    lordofwolves = Exotic(3413860063, 'Lord of Wolves')
    lemon = Exotic(3588934839, 'Le Monarque')
    jotunn = Exotic(417164956, 'Jötunn')
    tarrabah = Exotic(3110698812, 'Tarrabah')
    eriana = Exotic(3524313097, "Eriana's Vow")
    divinity = Exotic(4103414242, 'Divinity')
    symmetry = Exotic(4017959782, 'Symmetry')
    devil = Exotic(3824106094, "Devil's Ruin")
    tommys = Exotic(776191470, "Tommy's Matchbook")
    fourthhorse = Exotic(1665952087, "The Fourth Horseman")
    ruinous = Exotic(1363238943, 'Ruinous Effigy')
    duality = Exotic(3460576091, 'Duality')
    cloudstrike = Exotic(2603483885, 'Cloudstrike')
    ticuu = Exotic(3260753130, "Ticuu's Divination")
    mythoclast = Exotic(4289226715, 'Vex Mythoclast')
    driver = Exotic(3761898871, 'Lorentz Driver')
    intent = Exotic(14194600, 'Edge of Intent')
    messenger = Exotic(2812324401, 'Dead Messenger')
    obligation = Exotic(3505113722, 'Collective Obligation')
    delicate = Exotic(374573733, 'Delicate Tomb')
    trespass = Exotic(1234150730, 'The Trespasser')
    manticore = Exotic(219145368, 'The Manticore')
    hierarchy = Exotic(4174431791, 'Hierarchy of Needs')
    vexcal = Exotic(3118061005, 'Vexcalibur')
    centrifuse = Exotic(1912669214, 'Centrifuse')
    wardcliff = Exotic(1508896098, 'Wardcliff Coil')
    tractor = Exotic(358090458, 'Tractor Cannon')
    acrius = Exotic(3580904580, 'Legend of Acrius')
    darci = Exotic(3141979346, 'D.A.R.C.I')
    colony = Exotic(3899270607, 'The Colony')
    worldline = Exotic(1864563948, 'Worldline Zero')
    sleeper = Exotic(4036115577, 'Sleeper Simulant')
    thousand = Exotic(2069224589, 'One Thousand Voices')
    twotailed = Exotic(2694576561, 'Two-Tailed Fox')
    black = Exotic(3766045777, 'Black Talon')
    queenbreak = Exotic(2044500762, 'The Queenbreaker')
    thunderlord = Exotic(3325463374, 'Thunderlord')
    anarchy = Exotic(2376481550, 'Anarchy')
    leviathan = Exotic(2591746970, "Leviathan's Breath")
    xeno = Exotic(1395261499, 'Xenopahge')
    deathbringer = Exotic(2232171099, 'Deathbringer')
    heir = Exotic(2084878005, 'Heir Apparent')
    salvation = Exotic(370712896, "Salvation's Grip")
    eyesof = Exotic(2399110176, 'Eyes of Tomorrow')
    lament = Exotic(3487253372, 'Lament')
    gjallar = Exotic(1363886209, 'Gjallarhorn')
    parasite = Exotic(2812324400, 'Parasite')
    overture = Exotic(1763584999, 'Grand Overture')
    heartshadow = Exotic(3664831848, 'Heartshadow')
    determine = Exotic(449318888, 'Deterministic Chaos')
    winterbite = Exotic(3118061004, 'Winterbite')
    truth = Exotic(1201830623, 'Truth')
    whisper = Exotic(1891561814, 'Whisper of the Worm')

    with open('Exotics.json') as f:
        data1 = json.load(f)
    with open('Exotics_1.json') as f:
        data2 = json.load(f)
    with open('Exotics_2.json') as f:
        data3 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]

    connorExotics = {"Response": []}

    connorExotics['Response'].append(items1)
    connorExotics["Response"].append(items2)
    connorExotics["Response"].append(items3)

    with open('connorExotics.json', "w") as f:
        f.write(json.dumps(connorExotics, indent=2))

    exotic_len_1 = len(connorExotics["Response"][0]['weapons'])
    exotic_len_2 = len(connorExotics["Response"][1]['weapons'])
    exotic_len_3 = len(connorExotics["Response"][2]['weapons'])

    Exotic = {"Exotic": []}
    Kills = {"Kills": []}
    Precision = {"Precision Kills": []}

    for number in range(0, exotic_len_1):
        Name_1 = connorExotics["Response"][0]["weapons"][number]["referenceId"]
        Kills_1 = connorExotics["Response"][0]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_1 = \
            connorExotics["Response"][0]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_1)
        Kills['Kills'].append(Kills_1)
        Precision['Precision Kills'].append(Precision_1)
    for number in range(0, exotic_len_2):
        Name_2 = connorExotics["Response"][1]["weapons"][number]["referenceId"]
        Kills_2 = connorExotics["Response"][1]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_2 = \
            connorExotics["Response"][1]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_2)
        Kills['Kills'].append(Kills_2)
        Precision['Precision Kills'].append(Precision_2)
    for number in range(0, exotic_len_3):
        Name_3 = connorExotics["Response"][2]["weapons"][number]["referenceId"]
        Kills_3 = connorExotics["Response"][2]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_3 = \
            connorExotics["Response"][2]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
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
            telesto.weaponData(Kills, Precision)
        elif ID == 2232171099:
            deathbringer.weaponData(Kills, Precision)
        elif ID == 2357297366:
            witherhoard.weaponData(Kills, Precision)
        elif ID == 2591746970:
            leviathan.weaponData(Kills, Precision)
        elif ID == 2694576561:
            twotailed.weaponData(Kills, Precision)
        elif ID == 2812324400:
            parasite.weaponData(Kills, Precision)
        elif ID == 2812324401:
            messenger.weaponData(Kills, Precision)
        elif ID == 2816212794:
            juju.weaponData(Kills, Precision)
        elif ID == 2856683562:
            suros.weaponData(Kills, Precision)
        elif ID == 2907129557:
            sunshot.weaponData(Kills, Precision)
        elif ID == 3089417789:
            riskrunner.weaponData(Kills, Precision)
        elif ID == 3118061005:
            vexcal.weaponData(Kills, Precision)
        elif ID == 3141979346:
            darci.weaponData(Kills, Precision)
        elif ID == 3260753130:
            ticuu.weaponData(Kills, Precision)
        elif ID == 3325463374:
            thunderlord.weaponData(Kills, Precision)
        elif ID == 3413074534:
            polaris.weaponData(Kills, Precision)
        elif ID == 3413860062:
            chaperone.weaponData(Kills, Precision)
        elif ID == 3413860063:
            lordofwolves.weaponData(Kills, Precision)
        elif ID == 3437746471:
            crimson.weaponData(Kills, Precision)
        elif ID == 3460576091:
            duality.weaponData(Kills, Precision)
        elif ID == 3487253372:
            lament.weaponData(Kills, Precision)
        elif ID == 3524313097:
            eriana.weaponData(Kills, Precision)
        elif ID == 3580904581:
            tractor.weaponData(Kills, Precision)
        elif ID == 3588934839:
            lemon.weaponData(Kills, Precision)
        elif ID == 3628991658:
            graviton.weaponData(Kills, Precision)
        elif ID == 3628991659:
            vigilance.weaponData(Kills, Precision)
        elif ID == 3654674561:
            deadmans.weaponData(Kills, Precision)
        elif ID == 3659414143:
            verglas.weaponData(Kills, Precision)
        elif ID == 3664831848:
            heartshadow.weaponData(Kills, Precision)
        elif ID == 3973202132:
            thorn.weaponData(Kills, Precision)
        elif ID == 4017959782:
            symmetry.weaponData(Kills, Precision)
        elif ID == 4036115577:
            sleeper.weaponData(Kills, Precision)
        elif ID == 4068264807:
            monte.weaponData(Kills, Precision)
        elif ID == 4124984448:
            hardlight.weaponData(Kills, Precision)
        elif ID == 4255268456:
            skyburner.weaponData(Kills, Precision)
        elif ID == 4293613902:
            quicksilver.weaponData(Kills, Precision)
        elif ID == 19024058:
            prometheus.weaponData(Kills, Precision)
        elif ID == 46524085:
            osteo.weaponData(Kills, Precision)
        elif ID == 204878059:
            malfease.weaponData(Kills, Precision)
        elif ID == 370712896:
            salvation.weaponData(Kills, Precision)
        elif ID == 374573733:
            delicate.weaponData(Kills, Precision)
        elif ID == 400096939:
            outbreak.weaponData(Kills, Precision)
        elif ID == 417164956:
            jotunn.weaponData(Kills, Precision)
        elif ID == 449318888:
            determine.weaponData(Kills, Precision)
        elif ID == 776191470:
            tommys.weaponData(Kills, Precision)
        elif ID == 814876684:
            wish.weaponData(Kills, Precision)
        elif ID == 814876685:
            trinity.weaponData(Kills, Precision)
        elif ID == 1345867570:
            sweetBusiness.weaponData(Kills, Precision)
        elif ID == 1345867571:
            coldheart.weaponData(Kills, Precision)
        elif ID == 1363238943:
            ruinous.weaponData(Kills, Precision)
        elif ID == 1363886209:
            gjallar.weaponData(Kills, Precision)
        elif ID == 1395261499:
            xeno.weaponData(Kills, Precision)
        elif ID == 1441805468:
            navigator.weaponData(Kills, Precision)
        elif ID == 1473821207:
            revision.weaponData(Kills, Precision)
        elif ID == 1508896098:
            wardcliff.weaponData(Kills, Precision)
        elif ID == 1594120904:
            notime.weaponData(Kills, Precision)
        elif ID == 1665952087:
            fourthhorse.weaponData(Kills, Precision)
        elif ID == 1763584999:
            overture.weaponData(Kills, Precision)
        elif ID == 1833195496:
            agers.weaponData(Kills, Precision)
        elif ID == 1912669214:
            centrifuse.weaponData(Kills, Precision)
        elif ID == 2044500762:
            queenbreak.weaponData(Kills, Precision)
        elif ID == 2130065553:
            arbalest.weaponData(Kills, Precision)
        elif ID == 2179048386:
            forerunner.weaponData(Kills, Precision)
        elif ID == 2286143274:
            huckle.weaponData(Kills, Precision)
        elif ID == 2362471601:
            ratKing.weaponData(Kills, Precision)
        elif ID == 2376481550:
            anarchy.weaponData(Kills, Precision)
        elif ID == 2399110176:
            eyesof.weaponData(Kills, Precision)
        elif ID == 2415517654:
            bastion.weaponData(Kills, Precision)
        elif ID == 2603483885:
            cloudstrike.weaponData(Kills, Precision)
        elif ID == 2907129556:
            strum.weaponData(Kills, Precision)
        elif ID == 3110698812:
            tarrabah.weaponData(Kills, Precision)
        elif ID == 3118061004:
            winterbite.weaponData(Kills, Precision)
        elif ID == 3121540812:
            warning.weaponData(Kills, Precision)
        elif ID == 3141979347:
            bore.weaponData(Kills, Precision)
        elif ID == 3211806999:
            izan.weaponData(Kills, Precision)
        elif ID == 3371017761:
            finality.weaponData(Kills, Precision)
        elif ID == 3505113722:
            obligation.weaponData(Kills, Precision)
        elif ID == 3512014804:
            lumina.weaponData(Kills, Precision)
        elif ID == 3580904580 or ID == 1744115122:
            acrius.weaponData(Kills, Precision)
        elif ID == 3761898871:
            driver.weaponData(Kills, Precision)
        elif ID == 3766045777:
            black.weaponData(Kills, Precision)
        elif ID == 3824106094:
            devil.weaponData(Kills, Precision)
        elif ID == 3844694310:
            rabbit.weaponData(Kills, Precision)
        elif ID == 3856705927:
            hawkmoon.weaponData(Kills, Precision)
        elif ID == 3899270607:
            colony.weaponData(Kills, Precision)
        elif ID == 4174431791:
            hierarchy.weaponData(Kills, Precision)
        elif ID == 4289226715:
            mythoclast.weaponData(Kills, Precision)
        elif ID == 14194600:
            intent.weaponData(Kills, Precision)
        elif ID == 219145368:
            manticore.weaponData(Kills, Precision)
        elif ID == 347366834:
            ace.weaponData(Kills, Precision)
        elif ID == 940371471:
            wicked.weaponData(Kills, Precision)
        elif ID == 1201830623:
            truth.weaponData(Kills, Precision)
        elif ID == 1234150730:
            trespass.weaponData(Kills, Precision)
        elif ID == 1331482397:
            mida.weaponData(Kills, Precision)
        elif ID == 1364093401:
            lastword.weaponData(Kills, Precision)
        elif ID == 1541131350:
            cerberus.weaponData(Kills, Precision)
        elif ID == 1802135586:
            touch.weaponData(Kills, Precision)
        elif ID == 1852863732:
            wavesplit.weaponData(Kills, Precision)
        elif ID == 1853180924:
            chosen.weaponData(Kills, Precision)
        elif ID == 1864563948:
            worldline.weaponData(Kills, Precision)
        elif ID == 1891561814:
            whisper.weaponData(Kills, Precision)
        elif ID == 2069224589:
            thousand.weaponData(Kills, Precision)
        elif ID == 2084878005:
            heir.weaponData(Kills, Precision)
        elif ID == 4103414242:
            divinity.weaponData(Kills, Precision)
        elif ID == 603721696:
            cryo.weaponData(Kills, Precision)
        elif ID == 4190156464:
            merciless.weaponData(Kills, Precision)
        elif ID == 3549153978:
            fighting.weaponData(Kills, Precision)

    Full = PrettyTable()
    Full.add_column("Exotic", ["Sweet Business", "Strum", "Vigilance Wing", "Rat King", "MIDA Multi-Tool", "Crimson",
                               "The Jade Rabbit", "The Huckleberry", "SUROS Regime", "Cerberus+1", "Wish-Ender",
                               "Malfeasance", "Ace of Spades", "The Last Word", "Thorn", "Outbreak Perfected",
                               "Lumina", "Bad Juju", "Monte Carlo", "Traveler's Chosen", "Hawkmoon",
                               "No Time to Explain", "Dead Man's Tale", "Cryosthethesia 77K", "Osteo Striga",
                               "Touch of Malice",
                               "Quicksilver Storm", "Revision Zero", "Final Warning", "Verglas Curve",
                               "Wicked Implement", "Fighting Lion", "Sunshot", "Skyburner's Oath", 'Graviton Lance',
                               "Riskrunner", "Hard Light",
                               "Polaris Lance", "Trinity Ghoul", "Le Monarque", "Tarrabah", "Symmetry", "Devil's Ruin",
                               "Tommy's Matchbook", "Ticuu's Divination", "Vex Mythoclast", "Collective Obligation",
                               "Trespasser",
                               "The Manticore", "Hierarchy of Needs", "Centrifuse", "The Chaperone", "Izanagi's Burden",
                               "Arbalest", "Bastion", "Witherhoard", "Ager's Scepter",
                               "Forerunner", "Conditional Finality", "The Navigator", "Coldheart", "Merciless",
                               "Borealis", "Prometheus Lens", "Telesto", "Wavesplitter", "Lord of Wolves", "Jötunn",
                               "Eriana's Vow",
                               "Divinity", "The Fourth Horseman", "Ruinous Effigy", "Duality", "Cloudstrike",
                               "Lorentz Driver", "Edge of Intent",
                               "Dead Messenger", "Delicate Tomb", "Vexcalibur",
                               "The Wardcliff Coil", "Tractor Cannon", "Legend of Acrius", "D.A.R.C.I.",
                               "The Colony", "Worldline Zero", "Sleeper Simulant", "One Thousand Voices",
                               "Two-Tailed Fox", "Black Talon", "The Queenbreaker", "Thunderlord", "Anarchy",
                               "Leviathan's Breath",
                               "Xenophage", "Deathbringer", "Heir Apparent", "Salvation's Grip", "Eyes of Tomorrow",
                               "The Lament", "Gjallarhorn", "Parasite", "Grand Overture", "Heartshadow",
                               "Deterministic Chaos", "Winterbite", "Truth", "Whisper of the Worm"])
    Full.add_column("Kills",
                    [sweetBusiness.kills, strum.kills, vigilance.kills, ratKing.kills, mida.kills, crimson.kills,
                     rabbit.kills,
                     huckle.kills, suros.kills, cerberus.kills, wish.kills, malfease.kills, ace.kills,
                     lastword.kills, thorn.kills, outbreak.kills, lumina.kills, juju.kills, monte.kills, chosen.kills,
                     hawkmoon.kills, notime.kills, deadmans.kills, cryo.kills, osteo.kills, touch.kills,
                     quicksilver.kills,
                     revision.kills, warning.kills, verglas.kills, wicked.kills, fighting.kills, sunshot.kills,
                     skyburner.kills, graviton.kills, riskrunner.kills, hardlight.kills, polaris.kills, trinity.kills,
                     lemon.kills,
                     tarrabah.kills, symmetry.kills, devil.kills, tommys.kills, ticuu.kills, mythoclast.kills,
                     obligation.kills, trespass.kills, manticore.kills, hierarchy.kills, centrifuse.kills, chaperone.kills,
                     izan.kills, arbalest.kills, bastion.kills, witherhoard.kills, agers.kills, forerunner.kills,
                     finality.kills, navigator.kills, coldheart.kills, merciless.kills, bore.kills, prometheus.kills,
                     telesto.kills, wavesplit.kills, lordofwolves.kills, jotunn.kills, eriana.kills, divinity.kills,
                     fourthhorse.kills, ruinous.kills, duality.kills, cloudstrike.kills, driver.kills, intent.kills,
                     messenger.kills, delicate.kills, vexcal.kills,
                     wardcliff.kills, tractor.kills, acrius.kills, darci.kills, colony.kills, worldline.kills, sleeper.kills,
                     thousand.kills, twotailed.kills, black.kills, queenbreak.kills, thunderlord.kills, anarchy.kills,
                     leviathan.kills, xeno.kills, deathbringer.kills, heir.kills, salvation.kills, eyesof.kills, lament.kills,
                     gjallar.kills, parasite.kills, overture.kills, heartshadow.kills, determine.kills, winterbite.kills,
                     truth.kills, whisper.kills])
    Full.border = False
    Full.header = False
    Full.align['Exotic'] = 'c'
    Full.reversesort = True
    return Full.get_string(sortby="Kills", start=0, end=10, fields=['Exotic'])
