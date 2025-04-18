from csvToJSon import csvToJson


matches = csvToJson("../data/matches.csv")

def matchesPerYear():
    result= {}

    for match in matches:
        season = match.get("season")
        if season in result:
           result[season] += 1
        else:
            result[season] = 1

    return result

matchesPerYear()