from csvToJSon import csvToJson
import json

matches = csvToJson("../data/matches.csv")

def getMatchesWonByTeamsEachYear():
    result = {}

    for match in matches:
        winner= match.get("winner")
        season = match.get("season")
        if winner in result:
            if season in result[winner]:
                result[winner][season] += 1
            else:
               result[winner][season] = 1    

        else:
           result[winner] = {}
    with open("../public/matches-won-per-team-per-year.json","w") as file:
     json.dump(result,file,indent=4)     


getMatchesWonByTeamsEachYear()