import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

#square
t.color("#FF8200")
t.fillcolor("#FF8200")
t.begin_fill()

for x in range(4):
  t.fd(100)
  t.left(90)
  
t.end_fill()

#door
t.penup()
t.fd(33)
t.pendown()

t.color("#000000")
t.fillcolor("#000000")
t.begin_fill()

for x in range(1, 5):
  if x % 2 == 0:
    t.fd(60)
    t.left(90)
  else:
    t.fd(33)
    t.left(90)
    
t.end_fill()
t.penup()
t.fd(67)

#rectangle
t.pendown()
t.color("#FFC000")
t.fillcolor("#FFC000")
t.begin_fill()

for x in range(1,5):
  if x % 2 == 0:
    t.fd(100)
    t.left(90)
  else:
    t.fd(200)
    t.left(90)
    
t.end_fill()

#window 1
t.penup()
t.fd(20)
t.left(90)
t.fd(40)
t.pendown()

t.color("#000000")
t.fillcolor("#000000")
t.begin_fill()

for x in range(1, 5):
  if x % 2 == 0:
    t.fd(60)
    t.right(90)
  else:
    t.fd(30)
    t.right(90)
    
t.end_fill()

#window 2
t.penup()
t.right(90)
t.fd(100)
t.left(90)
t.pendown()

t.begin_fill()
for x in range(1, 5):
  if x % 2 == 0:
    t.fd(60)
    t.right(90)
  else:
    t.fd(30)
    t.right(90)
    
t.end_fill()

#triangle
t.penup()
t.left(90)
t.fd(120)
t.right(90)
t.fd(60)
t.left(-90)

t.pendown()
t.color("#C0504D")
t.fillcolor("#C0504D")
t.begin_fill()

for x in range(3):
  t.left(120)
  t.fd(100)
  
t.end_fill()

#roof
t.color("#C00000")
t.fillcolor("#C00000")
t.begin_fill()

t.fd(200)
t.left(120)
t.fd(100)
t.left(60)
t.fd(200)

t.end_fill()

