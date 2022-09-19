import json
import random

with open("./ELO.json", "r") as f:
    ELO = json.load(f)

def most_frequent(List): return max(set(List), key = List.count)
def leas_frequent(List): return min(set(List), key = List.count)

def predict_elo(team1_abbr, team2_abbr):

    TEAMS = [team1_abbr, team2_abbr]
    TEAMS[0] = { "ABBR": team1_abbr, "ELO": ELO[team1_abbr]["ELO"], "PROB": 0 }
    TEAMS[1] = { "ABBR": team2_abbr, "ELO": ELO[team2_abbr]["ELO"] + 68.3, "PROB": 0 } # Home Advantage: http://opisthokonta.net/?p=1387

    TEAMS[0]["PROB"] = (1 / (1+(20**((TEAMS[1]["ELO"] - TEAMS[0]["ELO"])/400)))) - 0.0683 # Away Disadvantage
    TEAMS[1]["PROB"] = (1 / (1+(20**((TEAMS[0]["ELO"] - TEAMS[1]["ELO"])/400)))) + 0.0683 # Home Advantage

    print(TEAMS[0]["ABBR"] + " @ " + TEAMS[1]["ABBR"])
    print(TEAMS[1]["ABBR"] + " (home) win probability: " + str(TEAMS[1]["PROB"]))
    print(TEAMS[0]["ABBR"] + " (away) win probability: " + str(TEAMS[0]["PROB"]))

    RESULTS = ( random.choices( [team1_abbr, team2_abbr], weights=(TEAMS[0]["PROB"], TEAMS[1]["PROB"]), k = 1_000_000 ) )
    return([most_frequent(RESULTS), leas_frequent(RESULTS)])