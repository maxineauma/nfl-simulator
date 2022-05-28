import nfl_predict 
import json
from sportsipy.nfl.boxscore import Boxscores

with open("./ELO.json", "r") as f:
    ELO = json.load(f)

def simulate_week(W):
    week = Boxscores(W, 2021)
    for g in (week.games[str(W)+"-2021"]):
        r = (nfl_predict.predict_elo(g["away_abbr"].upper(), g["home_abbr"].upper()))

        TEMP_ELO_W_OLD = ELO[r[0]]["ELO"]
        TEMP_ELO_L_OLD = ELO[r[1]]["ELO"]

        ELO[r[0]]["W"] = ELO[r[0]]["W"] + 1
        ELO[r[0]]["ELO"] = ELO[r[0]]["ELO"] + 20*(1 - (1/(1+10**((TEMP_ELO_L_OLD - TEMP_ELO_W_OLD)/400))))


        ELO[r[1]]["L"] = ELO[r[1]]["L"] + 1
        ELO[r[1]]["ELO"] = ELO[r[1]]["ELO"] + 20*(0 - (1/(1+10**((TEMP_ELO_W_OLD - TEMP_ELO_L_OLD)/400))))