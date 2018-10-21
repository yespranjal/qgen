import json

print('Hello')
json_data = open('Structure.json','r').read()

print(json_data);
json_temp = {"papa":"Suneel",
             "beta":"Pranjal"}

jsonObject = json.loads(json_data)



#print(jsonObject)

for object in jsonObject["objects"]:
    print(object)
    if object["type"] == "HighObject":
        highObjects.append(object)

