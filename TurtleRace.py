# Turtle Race Game
from turtle import Turtle, Screen
import random

# screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make ur bet", prompt="which turtle will win the race? Enter a color(red, orange, yellow, green : ")
print(user_bet)

# creating 4 turtles
all_turtles = []
turtle_colors = ["red", "orange", "yellow", "green"]
turtle_ypositions  = [-70, -40, -10, 20]
for turtle_index in range(4):
    tim = Turtle(shape="turtle")
    tim.color(turtle_colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=turtle_ypositions[turtle_index])
    all_turtles.append(tim)

is_game_on =False
if user_bet:
    is_game_on = True
    

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color  = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won!. {winning_color} turtle is the winner")
            else:
                print(f"You have lost!. {winning_color} turtle is the winner")
            is_game_on = False
        turtle.forward(random.randint(0,10))





screen.exitonclick()

