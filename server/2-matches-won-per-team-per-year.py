from csvToJSon import csvToJson


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
    return result      


getMatchesWonByTeamsEachYear()