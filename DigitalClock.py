import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Digital Clock")

# Create a turtle for displaying the time
clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()  # Hide the turtle pointer
clock_turtle.color("white")
clock_turtle.penup()
clock_turtle.goto(0, 0)
clock_turtle.speed(0)

# Function to display the time
def display_time():
    while True:
        # Get the current time in hour, minute, second format (HH:MM:SS)
        current_time = time.strftime("%H:%M:%S %p")
        
        # Clear the previous time from the screen
        clock_turtle.clear()

        # Display the updated time
        clock_turtle.write(current_time, align="center", font=("Courier", 48, "bold"))

        # Pause for 1 second before updating the time again
        time.sleep(1)

# Start the clock
display_time()

# Keep the window open
screen.mainloop()
