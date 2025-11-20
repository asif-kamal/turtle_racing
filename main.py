from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
choice = screen.textinput(title="choose_turtle", prompt="Enter the color of the turtle you want to win: ")

colors = ["red", "green", "blue", "yellow", "purple", "pink", "white"]
racing_turtles = {}
y = -160

for num in range(len(colors)):
    racing_turtles[f"t{num}"] = Turtle(shape="turtle")
    racing_turtles[f"t{num}"].color(colors[num])
    racing_turtles[f"t{num}"].penup()
    racing_turtles[f"t{num}"].goto(x=-230,y=y)
    y += 65

screen.exitonclick()