import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break
        
    if user_input not in options: 
        continue
    
    random_num = random.randint(0,2)
    #Rock = 0, Paper = 1, Scissors = 2
    comp_guess = options[random_num]
    print("Computer picked:",comp_guess + ".")

    if user_input == "rock" and comp_guess == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and comp_guess == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and comp_guess == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == comp_guess:
        print("It's a Tie!")
    else:
        print("You lost!")
        comp_wins += 1
    
print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times")
print("Goodbye!")