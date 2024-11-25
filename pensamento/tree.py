import turtle

# Configuração inicial
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Árvore de Natal")

# Configuração da tartaruga
t = turtle.Turtle()
t.speed(0)

# Função para desenhar triângulos da árvore
def draw_triangle(color, size, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Função para desenhar bolinhas
def draw_circle(color, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# Desenhar o tronco da árvore
t.penup()
t.goto(-15, -100)
t.pendown()
t.color("brown")
t.fillcolor("brown")
t.begin_fill()
for _ in range(2):
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

# Cores alternadas para os triângulos
triangle_colors = ["dark green", "green"]

# Tamanhos e posições dos triângulos
sizes_positions = [(100, (-50, -60)), (90, (-45, -40)), (80, (-40, -20)), (70, (-35, 0)), (60, (-30, 20)), (50, (-25, 40))]

# Desenhar os triângulos
for i, (size, pos) in enumerate(sizes_positions):
    draw_triangle(triangle_colors[i % 2], size, pos)

# Cores das bolinhas por linha
ornament_colors = [
    ["red", "blue", "light green"],
    ["light blue", "orange", "purple"],
    ["purple", "red", "orange"],
    ["blue", "orange", "blue"],
    ["orange", "light blue", "red"]
]

# Posições das bolinhas ajustadas
ornament_positions = [
    [(-45, -55), (0, -55), (45, -55)],
    [(-40, -35), (0, -35), (40, -35)],
    [(-35, -15), (0, -15), (35, -15)],
    [(-30, 5), (0, 5), (30, 5)],
    [(-25, 25), (0, 25), (25, 25)]
]

# Desenhar as bolinhas
for colors, positions in zip(ornament_colors, ornament_positions):
    for color, pos in zip(colors, positions):
        draw_circle(color, pos[0], pos[1] - 10, 5)  # Ajustar a altura das bolinhas

# Desenhar a estrela no topo com preenchimento completo
t.penup()
t.goto(-10, 55)  # Ajuste de posição da estrela
t.pendown()
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
for _ in range(5):
    t.forward(30)
    t.right(144)
    t.forward(30)
    t.left(72)
t.end_fill()

# Esconder a tartaruga (seta)
t.hideturtle()

# Manter a janela aberta
turtle.done()
