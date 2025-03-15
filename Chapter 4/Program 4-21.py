# concentric_circles.py

import turtle

# Named constants
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

# Setup the turtle.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Set the radius of the first circle
radius = STARTING_RADIUS

# Draw the circles
for count in range(NUM_CIRCLES):
    #Draw the circle.
    turtle.circle(radius)

    # Get the coordinates for the next circvle
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    # Calculate the radius for the next circle
    radius = radius +  OFFSET

    # Position the turtlle for the next cirecle
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

