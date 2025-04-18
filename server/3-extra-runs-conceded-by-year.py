from csvToJSon import csvToJson


deliveries = csvToJson("../data/deliveries.csv")
matches = csvToJson("../data/matches.csv")



def getExtraRunsConcededByYear(year):
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

    for delivery in deliveries:
        matchId = delivery.get("match_id")
       
        if matchId in matchIdsForYear:
            bowlingTeam = delivery.get("bowling_team")
            extraRuns = int(delivery.get("extra_runs"))
            if bowlingTeam in result:
                result[bowlingTeam] += extraRuns
            else:
                  result[bowlingTeam] =  extraRuns
    return result

getExtraRunsConcededByYear(2016)    