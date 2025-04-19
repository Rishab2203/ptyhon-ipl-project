from csvToJSon import csvToJson
import json


deliveries = csvToJson("../data/deliveries.csv")


def getHighestDismissal():
   playerAndBowlers = {}
   dismissalDeliveries = list(filter(lambda delivery: delivery["player_dismissed"] != '' and delivery["dismissal_kind"] != 'run out' ,deliveries))

   for delivery in dismissalDeliveries:
      playerDismissed = delivery["player_dismissed"]
      bowler = delivery["bowler"]
      if not  playerDismissed in playerAndBowlers:
         playerAndBowlers[playerDismissed] = {}
      if not bowler  in  playerAndBowlers[playerDismissed]:       
         playerAndBowlers[playerDismissed][bowler] = 1
      else:
         playerAndBowlers[playerDismissed][bowler] += 1

    #   print(playerAndBowlers)
   playerAndBowlers_list = list(playerAndBowlers.items())
   finalResult= {}

   for player in playerAndBowlers_list:
      playerName,bowlerAndWickets = player
      bowlerAndWickets_list = list(bowlerAndWickets.items())
      bowlerAndWickets_list.sort(key = lambda item : item[1],reverse= True)
      finalResult[playerName] = dict(bowlerAndWickets_list[:1])

   with open("../public/highest-dismissal.json","w") as file:
     json.dump(finalResult,file,indent=4)
    

getHighestDismissal()