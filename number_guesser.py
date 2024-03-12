import random

top_range = input("Type a number: ")
guess_count = 0

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Please enter a number larger than 0 next time. ")
        quit()
else:
    print("Please type a number next Time. ")
    quit()
    
random_num = random.randint(0,top_range)

while True:
    user_guess = input("Make a guess: ")
    guess_count+=1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number. ")
        continue
    
    if user_guess  == random_num:
        print("Correct")
        break      
    elif user_guess > random_num:
        print("Guess lower ")
    else:
        print("guess higher ")

print("You got it in",guess_count,"guesses")