import json

myObjDict = dict()
myObjDict["A"] = {"A1":2, "BSAD" : 5}
myObjDict["B"] = 35

#convert to JSON string
jsonStr = json.dumps(myObjDict)

#print json string
print(jsonStr)