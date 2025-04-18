from csvToJSon import csvToJson
from functools import reduce

deliveries = csvToJson("../data/deliveries.csv")
matches = csvToJson("../data/matches.csv")


def getTopEconomicBowlersByYear(year):
    result = {}
# match ids by seaoson
    matchIds = {}
    for match in matches:
        season = match.get("season")
        matchId = match.get("id")
        if season in matchIds:
            matchIds[season].add(matchId)
       
        else:
        
            matchIds[season] = {matchId}
           
    matchIdsForYear = matchIds.get(str(year))

  # runs given and deliveries  
    runsAndDeliveriesByBowler = {}

    for delivery in deliveries:
        matchId = delivery.get("match_id")
       
        if matchId in matchIdsForYear:
            bowler = delivery["bowler"]
            runs = int(delivery["batsman_runs"])
            if bowler in runsAndDeliveriesByBowler:
                runsAndDeliveriesByBowler[bowler]["runs"] += runs
                runsAndDeliveriesByBowler[bowler]["balls"] += 1
            else:
                runsAndDeliveriesByBowler[bowler] = {"runs":runs,"balls":1}
         

    new_list = list(runsAndDeliveriesByBowler.items())

    econmoies = list(map(lambda item: (item[0], item[1]["runs"]/item[1]["balls"]),new_list))
   
    econmoies.sort(key= lambda bowler: bowler[1] )
    return econmoies[:10]

getTopEconomicBowlersByYear(2016)