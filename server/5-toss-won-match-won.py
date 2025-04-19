from csvToJSon import csvToJson
import json

matches = csvToJson("../data/matches.csv")

def wonTossWonMatch():
    result = {}
    wonTossWonMatch = list(filter(lambda match : match["toss_winner"]== match["winner"], matches))
    
    for match in wonTossWonMatch:
       team = match.get("toss_winner")
       if not team in result:
           result[team]= 0
       result[team] += 1    

    with open("../public/won-toss-won-match.json","w") as file:
     json.dump(result,file,indent=4)


wonTossWonMatch()