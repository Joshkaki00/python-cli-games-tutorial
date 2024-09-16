#import the json file module from python3
import json

#open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

#initialize total as the length of the cards array
total = len(data["cards"])
#initialize score as 0
score = 0

#for loop iterator to iterate all cards
for i in data["cards"]:
    guess = input(i["q"] + ">")
    print(guess)

    if guess.lower() == i["a"].lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")