from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [0, 25, -25, -50, -75, -100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Hooray, your bet was on point, {winning_color} turtle won!!")
            else:
                print(f"HA!!! Your turtle lost the race, {winning_color} turtle won")
                break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




#tom = Turtle(shape="turtle")
#tom.penup()
#tom.goto(x=-240, y=-25)
#tom.color("orange")
#
#tum = Turtle(shape="turtle")
#tum.penup()
#tum.goto(x=-240, y=0)
#tum.color("yellow")
#
#tam = Turtle(shape="turtle")
#tam.penup()
#tam.goto(x=-240, y=-75)
#tam.color("green")
#
#tem = Turtle(shape="turtle")
#tem.penup()
#tem.goto(x=-240, y=-50)
#tem.color("blue")
#
#tammy = Turtle(shape="turtle")
#tammy.penup()
#tammy.goto(x=-240, y=25)
#tammy.color("purple")


screen.exitonclick()













