import turtle
t = turtle.Turtle()

t.shape("arrow")
t.color("black")

for x in range(9):
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()

t.fd(10)

turtle.done()