print("Welcome to my computer game")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! lets play :) ")
score = 0

answer1 = input("What does CPU stand for? ")
if answer1.lower() == "central processing unit":
     print("Correct!")
     score+=1
else:
    print("Incorrect!")

answer2 = input("What does GPU stand for? ")
if answer2.lower() == "graphics processing unit":
     print("Correct!")
     score+=1
else:
    print("Incorrect!")

answer3 = input("What does RAM stand for? ")
if answer3.lower() == "random access memory":
     print("Correct!")
     score+=1
else:
    print("Incorrect!")

answer4 = input("What does SSD stand for? ")
if answer4.lower() == "solid state drive":
     print("Correct!")
     score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 4. Well done! ")