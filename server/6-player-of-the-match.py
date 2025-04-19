from csvToJSon import csvToJson
import json

matches = csvToJson("../data/matches.csv")


def getPlayerOfTheMatchBySeason():

    result={}
    allPlayersOfTheMatchBySeason={}

    for match in matches:
        season = match.get("season")
        playerOfTheMatch = match.get("player_of_match")

        if not season in allPlayersOfTheMatchBySeason:
            allPlayersOfTheMatchBySeason[season]={}
        if not playerOfTheMatch in allPlayersOfTheMatchBySeason[season]:
            allPlayersOfTheMatchBySeason[season][playerOfTheMatch] = 0
        allPlayersOfTheMatchBySeason[season][playerOfTheMatch] += 1 

    allPlayersOfTheMatchBySeason = list(allPlayersOfTheMatchBySeason.items())

    for item in allPlayersOfTheMatchBySeason:
        listOfPlayers = list(item[1].items())
        listOfPlayers.sort(key= lambda player: player[1],reverse=True)
       
        result[item[0]] =  dict(listOfPlayers[:1])    
      
    with open("../public/player-of-the-match.json","w") as file:
     json.dump(result,file,indent=4)
 
    
   

getPlayerOfTheMatchBySeason()