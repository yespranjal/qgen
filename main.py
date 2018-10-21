import math
import json
import random

#print('Hello')
json_data = open('Structure.json','r').read()

#print(json_data);

jsonObject = json.loads(json_data)

AOEvalues = [30,45,60];

highObjects =   [];
groundObjects = [];

#print(jsonObject)

for object in jsonObject["objects"]:
    #print(object)
    if object["type"] == "HighObject":
        highObjects.append(object)
    elif object["type"] == "GroundObject":
        groundObjects.append(object)

# print("High Objects");
# print("");
#
# for object in highObjects:
#     print (object["name"]);
#
# print("Ground Objects");
# print("");
#
# for object in groundObjects:
#     print(object["name"]);

for questionNumber in range(1,11):
    highindex = random.randint(0,len(highObjects)-1);
    groundindex = random.randint(0,len(groundObjects)-1);
    AOE = AOEvalues[random.randint(0,len(AOEvalues)-1)];

    # print("High Object Selected: " + highObjects[highindex]["name"]);
    # print("Ground Object Selected: " + groundObjects[groundindex]["name"]);

    highvalue = random.randint(highObjects[highindex]["lowerLimit"]["value"],highObjects[highindex]["upperLimit"]["value"]);
    groundvalue = highvalue/math.tan(math.radians(AOE));

    # print(AOE);
    # print(highvalue);
    # print(groundvalue);

    highObjectAssertion = highObjects[highindex]["assertTemplates"][random.randint(0,1)].replace("{objectName}",highObjects[highindex]["name"]);
    highObjectAssertion = highObjectAssertion.replace("{objectValue}",str(highvalue) + " Metre");


    AOEAssertion = "The angle of elevation from " + groundObjects[groundindex]["name"] + " is " + str(AOE) + " degrees.";
    questionPart = groundObjects[groundindex]["questionTemplates"][random.randint(0,1)].replace("{objectName}",groundObjects[groundindex]["name"]);

    print(str(questionNumber) + ".");
    print(highObjectAssertion);
    print(AOEAssertion);
    print(questionPart);
    print();
    print("Ans: " + str(groundvalue) + " Metres");
    print();

    #question = highObjects[highindex]["assertTemplates"]


