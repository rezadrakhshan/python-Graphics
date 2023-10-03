import turtle

app = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
col = ('white','orange','red','yellow','green','blue','cyan')
app.speed(0)

for i in range(200):
    app.forward(i*4)
    app.right(94)
    app.color(col[i%7])
    for b in range(3):
        app.forward(i*4)
        app.right(91)
        