import json
import random

with open("./ELO.json", "r") as f:
    ELO = json.load(f)

def most_frequent(List): return max(set(List), key = List.count)
def leas_frequent(List): return min(set(List), key = List.count)

def predict_elo(team1_abbr, team2_abbr):

    TEAMS = [team1_abbr, team2_abbr]
    TEAMS[0] = { "ABBR": team1_abbr, "ELO": ELO[team1_abbr]["ELO"], "PROB": 0 }
    TEAMS[1] = { "ABBR": team2_abbr, "ELO": ELO[team2_abbr]["ELO"], "PROB": 0 }

    TEAMS[0]["PROB"] = 1 / (1+(20**((TEAMS[1]["ELO"] - TEAMS[0]["ELO"])/400)))
    TEAMS[1]["PROB"] = 1 / (1+(20**((TEAMS[0]["ELO"] - TEAMS[1]["ELO"])/400)))

    RESULTS = ( random.choices( [team1_abbr, team2_abbr], weights=(TEAMS[0]["PROB"], TEAMS[1]["PROB"]), k = 1000000 ) )
    return([most_frequent(RESULTS), leas_frequent(RESULTS)])