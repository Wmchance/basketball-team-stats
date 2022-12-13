from constants import *

def clean_data(players_data):
    cleaned_players = []

    for player in players_data:
        fixed = {}

        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == "YES":
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(player['height'].split(" ")[0])
        print(type(fixed['height']))
        
        cleaned_players.append(fixed)
    return cleaned_players


if __name__ == "__main__":
    print(clean_data(PLAYERS))