from constants import *
import copy

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
        
        cleaned_players.append(fixed)

    return cleaned_players

def balance_teams(clean_players_data, teams):
    experienced_players = []
    inexperienced_players = []
    num_of_teams = len(teams)
    
    for player in clean_players_data:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    # add try & Exception incase the numbers are not even and an int is not possible. ints are needed so that the new_team calc can be made
    exp_players_per_team = int(len(experienced_players)/num_of_teams)
    inexp_players_per_team = int(len(inexperienced_players)/num_of_teams)
    
    balanced_teams = []
    for index, team in enumerate(teams):
        new_team = {}
        new_team['team_name'] = team
        new_team['experienced_players'] = experienced_players[index*exp_players_per_team:(index*exp_players_per_team)+exp_players_per_team]
        new_team['inexperienced_players'] = inexperienced_players[index*inexp_players_per_team:(index*inexp_players_per_team)+inexp_players_per_team]
        balanced_teams.append(new_team)

    return balanced_teams


if __name__ == "__main__":
    clean_players = clean_data(PLAYERS)
    teams_copy = copy.deepcopy(TEAMS)
    
    balanced_teams = balance_teams(clean_players, teams_copy)
    # print(balanced_teams[0], '\n')
    