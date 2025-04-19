from csvToJSon import csvToJson
import json


matches = csvToJson("../data/matches.csv")

def matchesPerYear():
    result= {}

    for match in matches:
        season = match.get("season")
        if season in result:
           result[season] += 1
        else:
            result[season] = 1
    with open("../public/matches-per-year.json","w") as file:
     json.dump(result,file,indent=4)

matchesPerYear()

