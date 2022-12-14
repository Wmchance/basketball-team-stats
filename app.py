from constants import *
import copy
from functions import *


if __name__ == "__main__":
    clean_players = clean_data(PLAYERS)
    teams_copy = copy.deepcopy(TEAMS)
    
    balanced_teams = balance_teams(clean_players, teams_copy)

    print('\n')
    print("\U0001f3C0 Welcome to the basketball team stats tool \U0001f3C0 \n")
    stats_tool(balanced_teams)
    