# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-7-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at the commendation score, as well as a breakdown of all of the cards given.

import json
from prettytable import PrettyTable

def commendationData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    # Commendation Score by Types
    allyScore = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScore = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScore = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScore = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']
    # Commendation Percentage by Types
    allyPercent = metric_json["Response"][0]['profileCommendations']['data']['commendationNodePercentagesByHash']['154475713']
    funPercent = metric_json["Response"][0]['profileCommendations']['data']['commendationNodePercentagesByHash']['1341823550']
    leadershipPercent = metric_json["Response"][0]['profileCommendations']['data']['commendationNodePercentagesByHash']['1390663518']
    masteryPercent = metric_json["Response"][0]['profileCommendations']['data']['commendationNodePercentagesByHash']['4180748446']
    # Specific Commendation Cards
    selflessScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']

    commendationTable = PrettyTable()
    commendationTable.field_names = ['Commendation Category', 'Score', 'Percentage']
    commendationTable.add_rows(
        [
            ['Ally', allyScore, allyPercent],
            ['Fun', funScore, funPercent],
            ['Leadership', leadershipScore, leadershipPercent],
            ['Mastery', masteryScore, masteryPercent]
        ]
    )
    commendationTable.reversesort = True
    print(commendationTable.get_string(sortby='Score'))

    commendationCardTable = PrettyTable()
    commendationCardTable.field_names = ['Commendation Card', 'Category', 'Score']
    commendationCardTable.add_rows(
        [
            ['Perceptive', 'Leadership', perceptiveScore],
            ['Knowledgeable', 'Leadership', knowledgeableScore],
            ['Joy Bringer', 'Fun', joyBringerScore],
            ['Level-headed', 'Fun', levelHeadedScore],
            ['Best Dressed', 'Fun', bestDressedScore],
            ['Playmaker', 'Mastery', playmakerScore],
            ['Primeval Instinct', 'Mastery', primevalInstinctScore],
            ['Heroic', 'Mastery', heroicScore],
            ['Indispensable', 'Ally', indispensableScore],
            ['Selfless', 'Ally', selflessScore],
            ['Thoughtful', 'Ally', thoughfulScore],
            ['Patience and Consideration', 'Ally', patientConsiderateScore]
        ]
    )
    commendationCardTable.reversesort = True
    print(commendationCardTable.get_string(sortby='Score'))