import turtle
import random

turtle.hideturtle()

# Creating the screen
screen = turtle.Screen()
screen.title("Turtle Gambling Race! :3")
screen.bgcolor("misty rose")

# Turtle for title
t = turtle.Turtle()
t.shape("blank")
t.hideturtle()
t.penup()
t.setpos(0, 300)
t.color("purple")
t.write("Turtle Race!", False, "center", font=("Comic Sans MS", 24, "bold", "italic"))

# Finish line
t.setpos(150, 170)
t.right(90)
t.pendown()
t.color("black")
t.fillcolor("black")
t.begin_fill()
t.fd(250)
t.end_fill()
t.penup()

t.setpos(0, 300)

# Screen input with some prompt customization
user_color = screen.textinput("Color", "Welcome to Turtle Gambling! Choose a color for your turtle: pink, rosy brown, pale violet red, indian red, or salmon. Good luck! :)")
colors = ["pink", "rosy brown", "pale violet red", "indian red", "salmon"]

# Initial positions
x = -150
y = 150

# List for the turtles
turtles = []

for color in colors:
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.speed(random.randint(2, 8))  # Speed adjusted for smoother race
    new_turtle.setpos(x, y)
    y -= 50
    turtles.append(new_turtle)

turtle.hideturtle()

# The race
win = False
win_color = ""

while not win:
    for racer in turtles:
        racer.fd(random.randint(1, 10))
        position = racer.pos()

        # Checking if a turtle won
        if racer.xcor() >= 150:
            win_color = racer.color()[0]
            win = True

# Result turtle for text display
result_t = turtle.Turtle()
result_t.shape("blank")
result_t.penup()
result_t.hideturtle()
result_t.setpos(0, -200)

# Displaying the result with some emotion
if win_color == user_color:
    result_t.color("green")
    result_t.write(f"🎉 Congratulations! Your {user_color} turtle won! 🎉", False, "center", font=("Comic Sans MS", 18, "bold"))
else:
    result_t.color("red")
    result_t.write(f"😢 Sorry! Your {user_color} turtle did not win. Better luck next time! 😢", False, "center", font=("Comic Sans MS", 18, "bold"))

turtle.done()
