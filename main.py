from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("dark gray")

race_active = True
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-120, -70, -20, 30, 80, 130]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    race_active = True

while race_active:

    for turtle in turtles:
        if turtle.xcor() > 200:
            winner = turtle.pencolor()
            race_active = False
            if winner == user_bet:
                print(f"Congratulations! Your turtle ({winner}) won the race!")
            else:
                print(f"Sorry, you lost! The {winner} turtle won the race!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
