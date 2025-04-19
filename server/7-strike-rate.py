from csvToJSon import csvToJson
from functools import reduce
import json

deliveries = csvToJson("../data/deliveries.csv")
matches = csvToJson("../data/matches.csv")

def strikeRateBySeason(playerName):
    result = {}
    matchIds= {}

    for match in matches:
        season = match.get("season")
        id = match.get("id")
        if not id in matchIds:
            matchIds[id] = season
           
    # print(matchIds)
    deliveriesForPlayer = list(filter(lambda delivery: delivery["batsman"]== playerName, deliveries))

    for delivery in deliveriesForPlayer:
        batsmanRuns = int(delivery["batsman_runs"])
        matchId = delivery["match_id"]
        season = matchIds[matchId]
        if not season in result:
            result[season] = {"runs":0,"balls":0}
        result[season]["runs"] += batsmanRuns
        result[season]["balls"] += 1   
    
    runsAndBalls_list = list(result.items())
    finaResult={}

    for item in runsAndBalls_list:
        season,runsAndBalls = item
        finaResult[season] = runsAndBalls["runs"]/runsAndBalls["balls"]

    with open("../public/strike-rate.json","w") as file:
     json.dump(finaResult,file,indent=4)  


   

strikeRateBySeason("DA Warner")    

