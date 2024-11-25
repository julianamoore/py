import turtle
import random
turtle.hideturtle()

#creating the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Art")

#turtle
t = turtle.Turtle()
t.shape("blank")
t.hideturtle()
t.speed(0)

#function for triangles
def draw_triangle():
    colors = ["#e7e6f7", "#e3d0d8", "#aea3b0", "#827081", "#c6d2ed"]
    random_color = random.choice(colors)
    t.color(random_color)
    t.fillcolor(random_color)
    t.begin_fill()

    forward = (random.randint(100, 150))
    for _ in range(3):
        t.forward(forward)
        t.left(120)
    
    t.end_fill()
    t.penup()
    t.right(10)
    t.pendown()

#function for circle
def draw_circle():
    colors = ["#bee9e8", "#62b6cb", "#1b4965", "#cae9ff", "#5fa8d3"]
    random_color = random.choice(colors)
    t.color(random_color)
    t.fillcolor(random_color)
    t.begin_fill()
    t.circle(random.randint(50, 70))
    t.end_fill()
    t.penup()
    t.right(10)
    t.pendown()

#function for square
def draw_square():
    colors = ["#461220", "#8c2f39", "#b23a48", "#fcb9b2", "#fed0bb"]
    random_color = random.choice(colors)
    t.color(random_color)
    t.fillcolor(random_color)
    t.begin_fill()
    forward = (random.randint(100, 150))

    for x in range(4):
        t.fd(forward)
        t.right(90)

    t.end_fill()
    t.penup()
    t.right(10)
    t.pendown()

while True:
    #shape chosen by user
    shape = screen.textinput("Art Piece Shape", "Choose a shape for your art piece: square, circle, triangle.")

    if shape in ["square", "circle", "triangle"]:
        break

    else:
        shape = screen.textinput("Invalid Shape", "Choose your shape: square, circle, triangle.")

for x in range(31):
    if shape == "square":
        draw_square()

    elif shape == "circle":
        draw_circle()

    elif shape == "triangle":
        draw_triangle()

#so the window doesnt close at the end
turtle.done()