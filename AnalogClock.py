import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Analog Clock")
screen.setup(width=600, height=600)

# Create a turtle for drawing the clock face
clock_face = turtle.Turtle()
clock_face.hideturtle()
clock_face.speed(0)
clock_face.pensize(3)

# Create turtles for the hands
second_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
hour_hand = turtle.Turtle()

# Configure the hands
for hand in [second_hand, minute_hand, hour_hand]:
    hand.shape("arrow")
    hand.shapesize(stretch_wid=0.5, stretch_len=6)
    hand.speed(0)
    hand.color("white")
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90)

second_hand.shapesize(stretch_wid=0.5, stretch_len=8)  # Longer for seconds
second_hand.color("red")  # Red color for seconds hand

# Draw the clock face
def draw_clock_face(radius):
    clock_face.penup()
    clock_face.goto(0, -radius)
    clock_face.pendown()
    clock_face.circle(radius)
    
    # Draw hour markers (12, 3, 6, 9)
    for angle in range(0, 360, 30):
        clock_face.penup()
        clock_face.goto(0, 0)
        clock_face.setheading(90 - angle)
        clock_face.forward(radius - 20)
        clock_face.pendown()
        clock_face.forward(10)
        
# Update the position of the clock hands based on the current time
def update_hands():
    current_time = time.localtime()
    
    # Extract hours, minutes, and seconds from the current time
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    # Calculate the angles for the hands
    second_angle = 6 * seconds
    minute_angle = 6 * minutes + seconds / 10
    hour_angle = 30 * (hours % 12) + minutes / 2
    
    # Move the hands to the calculated angles
    second_hand.setheading(90 - second_angle)
    minute_hand.setheading(90 - minute_angle)
    hour_hand.setheading(90 - hour_angle)
    
# Draw the clock face
draw_clock_face(250)

# Continuously update the hands to reflect the current time
while True:
    update_hands()
    screen.update()
    time.sleep(1)  # Update every second

# Keep the window open
screen.mainloop()
