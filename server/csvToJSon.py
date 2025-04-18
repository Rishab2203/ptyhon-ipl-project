
##  Function to convert CSV to JSON


def csvToJson(filepath):
   
   listOfDict = []
   
   file = open(filepath)
   data = list(file.readlines())
   headColumn = data[0].replace("\n","").split(",")
   rows= data[1:]
   for row in rows:
     match = dict(zip(headColumn,row.replace("\n","").split(",")))
     listOfDict.append(match)
   
   file.close()

   return listOfDict 
   


# csvToJson("../data/matches.csv")   