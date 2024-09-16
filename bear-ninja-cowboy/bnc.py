player = False

while player == False:
# Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

# Compare computer and player role
if computer == player:
    print("DRAW!")
elif computer == "Cowboy":
    if player == "Bear":
        print(f"You lose! {player} is shot by {computer}")
    else:
        print(f"You win! {player} defeats {computer}")
elif computer == "Bear":
    if player == "Cowboy":
        print(f"You win! {player} shoots {computer}")
    else:
        print (f"You lose! {player} is eaten by {computer}")
elif computer == "Ninja":
    if player == "Cowboy":
        print(f"You lose! {player} is defeated by {computer}")
    else:
        print(f"You win! {player} eats {computer}")
    
    play_again = input("Would you like to play again (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0,2)]
    else:
        print("Thanks for playing!")
        exit()