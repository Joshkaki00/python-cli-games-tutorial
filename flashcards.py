#import the json file module from python3
import json

#open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

#for loop iterator to iterate all cards
for i in data["cards"]:
    print(i)