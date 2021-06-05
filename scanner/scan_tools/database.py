import csv
import os

#######
# TEAMS
#######

teams = ['Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears',
         'Bengals', 'Browns', 'Cowboys', 'Broncos', 'Lions', 'Packers',
         'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Dolphins', 'Vikings',
         'Patriots', 'Saints', 'Giants', 'Jets', 'Raiders', 'Eagles',
         'Steelers', 'Chargers', '49ers', 'Seahawks', 'Rams', 'BUCCANEERS',
         'Titans', 'Washington']

TEAMS = [team.upper() for team in teams]

###########
# Positions
###########

offense = ['Center', 'Offensive guard', 'Offensive tackle', 'Quarterback',
           'Running back', 'Wide receiver', 'Tight end']
defense = ['Defensive tackle', 'Defensive end', 'Linebacker', 'Cornerback',
           'Safety']
special = ['Kicker', 'Kickoff specialist', 'Punter', 'Holder', 'Long snapper',
           'Kick returner', 'punt returner', 'Upback', 'Gunner', 'Jammer']

offense_upper = [item.upper() for item in offense]
defense_upper = [item.upper() for item in defense]
special_upper = [item.upper() for item in special]

POSITIONS = offense_upper + defense_upper + special_upper


#########
# Players
#########
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'players2020.csv')

with open(file_path, 'r') as players_file:
    headers = ["set", "number", "name", "team"]
    reader = csv.DictReader(players_file, fieldnames=headers)
    PLAYERS = list(reader)
