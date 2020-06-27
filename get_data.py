import requests

ENDPOINT = "https://www.fantasyfootballdatapros.com/api/players/2019/all"

def transform_json(player):
    data = {}
    for k, v in player.items():
        if k != 'stats':
            if k == 'player_name':
                #issues with players with apostrophes in their names such as Le'Veon Bell.
                #this line takes Le'veon Bell and outputs Leveon Bell
                v = v.replace("'", "")
            data[k] = v

    #remove nesting
    sub_stats = [player['stats']['rushing'], player['stats']['passing'], player['stats']['receiving']]
    for sub_stat in sub_stats:
        for k, v in sub_stat.items():
            data[k] = v

    return data

def get_player_data():
    json = requests.get(ENDPOINT).json()
    #reassign our json
    data = list(map(transform_json, json))
    return data
