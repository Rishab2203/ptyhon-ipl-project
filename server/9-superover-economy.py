from csvToJSon import csvToJson

import json

deliveries = csvToJson("../data/deliveries.csv")
matches = csvToJson("../data/matches.csv")


def getTopEconomicBowlersInSuperOver(year):
  


  # runs given and deliveries  
    runsAndDeliveriesByBowler = {}

    for delivery in deliveries:
     if delivery["is_super_over"] == "1":
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
    with open("../public/superover-top-economic-bowlers.json","w") as file:
     json.dump(econmoies[:10],file,indent=4)

getTopEconomicBowlersInSuperOver(2016)