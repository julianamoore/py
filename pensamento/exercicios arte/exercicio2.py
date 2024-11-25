import turtle
import random
turtle.hideturtle()

#creating the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Line Art!")

#turtle
t = turtle.Turtle()
t.shape("blank")
t.hideturtle()
t.speed(0)

#line creator
def line_create(color):
    t.penup()
    x_coor = (random.randint(-250, 250))
    y_coor = (random.randint(-250, 250))
    t.goto(x_coor, y_coor)

    t.pendown()
    t.color(color)
    t.fillcolor(color)

    #random orientation and forward ammount
    t.right(random.randint(-360, 360))
    t.fd(random.randint(10, 500))

#how many lines
user_lines = screen.textinput("How many lines", "How many lines would you like in your art piece?")
user_lines = int(user_lines)

#if lines are less than 0
while True:
    user_lines = int(user_lines)
    if user_lines > 0:
        break
    user_lines = screen.textinput("Invalid Amount", "How many lines would you like in your art piece?")

#what color
user_color = screen.textinput("Choose your color", "Would you like to use random colors? (y/n)")
#random color palette with rainbow pastels
random_color_palette = ["#fbf8cc", "#fde4cf", "#ffcfd2", "#f1c0e8", "#cfbaf0", "#a3c4f3", "#90dbf4", "#8eecf5", "#98f5e1", "#b9fbc0"]

#if the input isnt valid
while True:
    if user_color in ["y", "n"]:
        break

    user_color = screen.textinput("Invalid Color", "Would you like to use random colors? (y/n)")

#if user chose random colors
if user_color == "y":
    for x in range(user_lines):
        random_color = random.choice(random_color_palette)
        line_create(random_color)

#if user chose no random colors
elif user_color == "n":
    for x in range(user_lines):
        line_create("black")
    
#so the window doesnt close at the end
turtle.done()