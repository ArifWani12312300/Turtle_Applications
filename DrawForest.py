import turtle
import random

# Set up the screen
win = turtle.Screen()
win.bgcolor("sky blue")
win.title("Beautiful Forest")

# Create a turtle to draw the tree trunk
trunk = turtle.Turtle()
trunk.shape("turtle")
trunk.speed(10)

# Create a turtle to draw the tree leaves
leaves = turtle.Turtle()
leaves.shape("turtle")
leaves.speed(10)

# Function to draw the tree trunk
def draw_trunk(x, y):
    trunk.penup()
    trunk.goto(x, y)
    trunk.pendown()
    trunk.color("saddle brown")
    trunk.begin_fill()
    
    # Draw a rectangle for the tree trunk
    for _ in range(2):
        trunk.forward(20)  # Trunk width
        trunk.left(90)
        trunk.forward(50)  # Trunk height
        trunk.left(90)
    
    trunk.end_fill()

# Function to draw the tree leaves
def draw_leaves(x, y):
    leaves.penup()
    leaves.goto(x + 10, y + 50)  # Start at the top of the trunk
    leaves.pendown()
    leaves.color("forest green")
    leaves.begin_fill()
    
    # Draw a triangle for the tree leaves
    leaves.circle(40)
    
    leaves.end_fill()

# Function to draw a tree
def draw_tree(x, y):
    draw_trunk(x, y)
    draw_leaves(x, y)

# Draw multiple trees to represent a forest
def draw_forest():
    positions = [
        (-250, -200), (-200, -150), (-150, -200), (-100, -150),
        (-50, -200), (0, -150), (50, -200), (100, -150),
        (150, -200), (200, -150), (250, -200)
    ]
    for pos in positions:
        x, y = pos
        draw_tree(x, y)

# Draw the forest
draw_forest()

# Hide turtles after drawing
trunk.hideturtle()
leaves.hideturtle()

# Keep the window open
win.mainloop()
