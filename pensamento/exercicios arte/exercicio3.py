import turtle
import random
turtle.hideturtle()

#creating the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Circle Art!")

#turtle
t = turtle.Turtle()
t.shape("blank")
t.hideturtle()
t.speed(0)

#function for circle
def draw_circle():
    colors = ["#f8f9fa", "#e9ecef", "#dee2e6", "#ced4da", "#adb5bd", "#6c757d", "#495057", "#343a40", "#212529"]
    random_color = random.choice(colors)
    t.color(random_color)

    t.penup()
    x_coor = (random.randint(-250, 250))
    y_coor = (random.randint(-250, 250))
    t.goto(x_coor, y_coor)

    t.pendown()
    t.circle(random.randint(10, 100))

#how many circles
user_circles = screen.textinput("How many circles", "How many circles would you like in your art piece?")

#if amount of circles isnt valid
while True:
    user_circles = int(user_circles)
    if user_circles > 0:
        break

    user_circles = screen.textinput("Invalid Amount", "How many circles would you like in your art piece?")

for x in range(user_circles):
    draw_circle()
    
#so the window doesnt close at the end
turtle.done()