import turtle

turtle.bgcolor("black")

squery = turtle.Turtle()
squery.speed(20)
squery.pencolor("blue")
for i in range(400):
    squery.forward(i)
    squery.left(91)

turtle.done()