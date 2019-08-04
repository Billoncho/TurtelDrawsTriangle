# TurtleDrawsTriangle.py
# Billy Ridgeway
# Creates a beautiful triangle.

import turtle                   # Imports turtle library.
t = turtle.Turtle()             # Creates a new pen called t.
t.getscreen().bgcolor("black")  # Sets the background to black.
t.pencolor("yellow")            # Sets the pen's color to yellow.
t.width(2)                      # Sets the pen's width to 2.
t.shape("turtle")               # Sets the shape of the pen to a turtle.

for x in range(100):            # Sets the range of x to 100.
    t.forward(3*x^2)            # Moves the pen forward 3 times the value of x squared.
    t.left(120)                 # Turns the pen left 120 degrees.

