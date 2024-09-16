#import the json file module from python3
import json

#open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

#for loop iterator to iterate all cards
for i in data["cards"]:
    guess = input(i["q"] + ">")
    print(guess)

    if guess == i["a"]:
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", i["a"])