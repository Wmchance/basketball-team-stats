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

def stats_tool(teams):
    print("Would you like to:\n A. Display a team's stats \n B. Quit the tool \n")
    user_choice = input("Please enter your choice('A' or 'B'): ")

    if user_choice.lower() == 'a':
        print('\n')
        print('OK, here are the current teams: \n')
        total_teams_index = []
        for index, team in enumerate(teams, 1):
            print(f"{index}. {team['team_name']}")
            total_teams_index.append(index)
        try:
            team_choice = int(input("\nPlease enter the number of the team you would like to see: "))
            if team_choice not in total_teams_index:
                raise Exception
        except Exception:
            print("Sorry, that isn't an available choice. Please only enter one of the shown numbers\n")
            stats_tool(balanced_teams)
        print('\n')

        num_total_players = len(teams[team_choice-1]['experienced_players']) + len(teams[team_choice-1]['inexperienced_players'])
        num_exp_players = len(teams[team_choice-1]['experienced_players'])
        teams[team_choice-1]['num_experienced_players'] = num_exp_players
        num_inexp_players = len(teams[team_choice-1]['inexperienced_players'])
        teams[team_choice-1]['num_inexperienced_players'] = num_inexp_players
        
        all_heights = []
        for player in teams[team_choice-1]['experienced_players']:
            all_heights.append(player['height'])
        for player in teams[team_choice-1]['inexperienced_players']:
            all_heights.append(player['height'])
        avg_height = sum(all_heights)/len(all_heights)
        teams[team_choice-1]['avg_height'] = avg_height
        
        all_players = []
        for player in teams[team_choice-1]['experienced_players']:
            all_players.append(player)
        for player in teams[team_choice-1]['inexperienced_players']:
            all_players.append(player)
        # https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
        all_players_sorted_by_height = sorted(all_players, key=lambda i: i['height'])
        all_players_names = []
        for player in all_players_sorted_by_height:
            all_players_names.append(player['name'])
        
        all_guardians_names = []
        for player in teams[team_choice-1]['experienced_players']:
            all_guardians_names.append(player['guardians'])
        for player in teams[team_choice-1]['inexperienced_players']:
            all_guardians_names.append(player['guardians'])

        print(f"{teams[team_choice-1]['team_name']}' stats: \n----------------")
        print(f"Total players: {num_total_players}")
        print(f"Experienced players: {num_exp_players}")
        print(f"Inexperienced players: {num_inexp_players}")
        print(f"Avg player height: {round(avg_height,2)} inches \n")
        print(f"Players by ascending height: \n{', '.join(all_players_names)} \n")
        print(f"Guardians: \n{', '.join(sum(all_guardians_names, []))} \n")
        input("Press any key to continue: \n")
        stats_tool(balanced_teams)
    elif user_choice.lower() == 'b':
        exit("\nSee you next time! \U0001f44b\n")
    else:
        print("Please choose either 'A' to see a team's stats or 'B' to quit\n")
        stats_tool(balanced_teams)


if __name__ == "__main__":
    clean_players = clean_data(PLAYERS)
    teams_copy = copy.deepcopy(TEAMS)
    
    balanced_teams = balance_teams(clean_players, teams_copy)

    print('\n')
    print("\U0001f3C0 Welcome to the basketball team stats tool \U0001f3C0 \n")
    stats_tool(balanced_teams)
    