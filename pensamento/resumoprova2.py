import turtle
t = turtle.Turtle()

t.color("hot pink")
t.speed(0)

t.begin_fill()

#square
for x in range(4):
    t.fd(100)
    t.left(90)

t.end_fill()

#triangle
for x in range(3):
    t.fd(100)
    t.left(120)

turtle.done()