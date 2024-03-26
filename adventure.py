name = input("Type your name: ")

print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can either go left or right. What do you choose? ").lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around or swim to swim across: ").lower()
    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer =='walk':
        print("You walked for many miles, ran out of water and died of dehydration.")
    else:
        print(answer,"Not a valid option. You lose.")
        
elif answer == 'right':
    answer = input("You come to a bridge, it looks unstable, do you want to cross it or go back (cross/back) ").lower()
    if answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()
        if answer == 'yes':
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == 'no':
            print("You ignore the stranger and offend them. They shoot you in the back and you lose.")    
        else:
            print("Not a valid option. You lose.")
            
    elif answer =='back':
        print("You go back and lose")
    else:
        print("Not a valid option. You lose.")
    
else:
    print("Not a valid option. You lose.")