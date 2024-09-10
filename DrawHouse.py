import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle object for drawing
pen = turtle.Turtle()
pen.speed(5)

# Function to draw a square (used for walls, windows, and door)
def draw_square(size, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

# Function to draw the base of the house
def draw_house_base():
    pen.penup()
    pen.goto(-150, -150)
    pen.pendown()
    draw_square(300, "lightyellow")  # Base of the house

# Function to draw the roof of the house
def draw_roof():
    pen.penup()
    pen.goto(-150, 150)
    pen.pendown()
    pen.fillcolor("brown")
    pen.begin_fill()
    for _ in range(3):  # Roof is a triangle
        pen.forward(300)
        pen.left(120)
    pen.end_fill()

# Function to draw the door
def draw_door():
    pen.penup()
    pen.goto(-50, -150)
    pen.pendown()
    draw_square(100, "brown")  # Door is a square

# Function to draw windows
def draw_window(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    draw_square(50, "skyblue")  # Windows are squares

# Function to draw the chimney
def draw_chimney():
    pen.penup()
    pen.goto(50, 100)
    pen.setheading(90)
    pen.pendown()
    draw_square(40, "gray")  # Chimney

# Drawing the house
draw_house_base()
draw_roof()
draw_door()
draw_window(-125, 0)  # Left window
draw_window(25, 0)    # Right window
draw_chimney()

# Hide the turtle cursor after drawing
pen.hideturtle()

# Keeps the window open
turtle.done()
