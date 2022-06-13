from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Mae your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "orange", "blue", "green", "purple"]
all_turtles = []

pos_y = 150
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=pos_y)
    all_turtles.append(new_turtle)
    pos_y -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} is the winner.")
                is_race_on = False
            else:
                print(f"You lost! {winning_color} is the winner.")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
