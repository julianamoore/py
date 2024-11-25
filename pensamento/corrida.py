import turtle
import random
turtle.hideturtle()

#creating the screen
screen = turtle.Screen()
screen.title("Turtle Gambling Race! :3")
screen.bgcolor("misty rose")

#turtle
t = turtle.Turtle()
t.shape("blank")
t.hideturtle()
t.penup()
t.setpos(0, 300)
t.color("brown")
t.write("Turtle Race!",False,"center",font=("Times New Roman", 20, "bold"))

#finish line
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

#screen input
user_color = screen.textinput("Choose your turtle!", "Welcome to turtle gambling! We have pink, rosy brown, pale violet red, indian red, or salmon. ")
colors = ["pink", "rosy brown", "pale violet red", "indian red", "salmon"]

#initial positions
x = -150
y = 150

#list for the turtles
turtles = []

for color in colors:
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.speed(random.randint(1, 10))
    new_turtle.setpos(x, y)
    y -= 50
    turtles.append(new_turtle)

turtle.hideturtle()

#the race
win = False
win_color = ""

while not win:
    for racer in turtles:
        racer.fd((random.randint(1, 10)))
        position = turtle.pos()
    
        #checking if a turtle won
        if racer.xcor() >= 150:
            win_color = racer.color()[0]
            win = True

#result turtle for text
result_t = turtle.Turtle()
result_t.shape("blank")
result_t.penup()
result_t.hideturtle()
result_t.setpos(0, -200) 

#checking if user won
if win_color == user_color:
    result_t.color("hot pink")
    result_t.write(f"Congratulations! Your {user_color} colored turtle won! :)",False,"center",font=("Times New Roman", 15, "bold"))

else:
    result_t.color("crimson")
    result_t.write(f"Sorry! Your {user_color} colored turtle did not win :(",False,"center",font=("Times New Roman", 15, "bold"))

turtle.done()