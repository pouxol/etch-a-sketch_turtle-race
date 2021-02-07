import turtle as t
import random

race_is_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet.", prompt=f"Which turtle will win the race? Enter a color: {colors} ")

for i in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=-125 + i * 50)
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
