import turtle
import time
import random

WIDTH, HEIGHT = 500,500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def turtle_number():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
        else:
            print('Please enter a valid number between 2-10!')
            continue

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
        


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        
    return turtles
    
    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')
    
    
racers = turtle_number()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print('The Winner is the',winner,'turtle!')
time.sleep(5)