# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-7-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at character triumph scores data.

import json
from prettytable import PrettyTable

def profileData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    score = metric_json["Response"][0]["profileRecords"]['data']['score']
    activeScore = metric_json["Response"][0]["profileRecords"]['data']['activeScore']
    legacyScore = metric_json["Response"][0]["profileRecords"]['data']['legacyScore']
    lifetimeScore = metric_json["Response"][0]["profileRecords"]['data']['lifetimeScore']

    print(f'Triumph Score: {score}\nActive Triumph Score: {activeScore}\nLegacy Triumph Score: '
          f'{legacyScore}\nLifetime Triumph Score: {lifetimeScore}')