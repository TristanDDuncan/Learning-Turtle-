import turtle

turtle.speed(0)
turtle.bgcolor("cyan")

for i in range (5):
    for colours in ["red", "green","blue", "yellow", "purple", "cyan", "orange"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

