import random
from turtle import Turtle, Screen
from tkinter import messagebox

screen = Screen()
is_race_on = False
screen.setup(width=500, height=600)
choice = screen.textinput(title="choose_turtle", prompt="Enter the color of the turtle you want to win: ")

if choice:
    is_race_on = True

colors = ["red", "green", "blue", "yellow", "purple", "pink", "black"]
racing_turtles = {}
y = -160

for num in range(len(colors)):
    racing_turtles[f"t{num}"] = Turtle(shape="turtle")
    racing_turtles[f"t{num}"].color(colors[num])
    racing_turtles[f"t{num}"].penup()
    racing_turtles[f"t{num}"].goto(x=-230,y=y)
    y += 65

while is_race_on:

    for turtle in racing_turtles.values():
        if turtle.xcor() < 222:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        else:
            is_race_on = False
            messagebox.showinfo("result", f"The winning color of the turtle is {turtle.fillcolor()}")
            if choice == turtle.fillcolor():
                messagebox.showinfo("Winner", "You won!")
            else:
                messagebox.showinfo("Lost", "You lost!")

screen.exitonclick()