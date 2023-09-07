'''
Jennifer Williams
August 21, 2023
CS152 Assignment 2
Pinwheel made from 4 octagons
'''
import turtle
# Create the window
wn = turtle.Screen()
wn.bgcolor('blue')
# Create Phil the turtle
phil = turtle.Turtle()
phil.color("magenta")
phil.pensize(3)
phil.shape('turtle')
forty = phil.forward(40)
# The loop for Phil to create an octagon
for color in ['magenta', 'violet', 'maroon', 'navy']:
    # Start to fill the shape Phil makes before beginning the loop to create the
    #shape.
    phil.begin_fill()
    for _ in range(8):
        phil.color(color)
        phil.forward(75)
        phil.left(45)
    # End the fill after the shape is complete
    phil.end_fill()
    phil.penup()
    forty
    phil.right(90)
    forty
    phil.pendown()
        # Hide Phil so there isn't a bump in the shape
    phil.ht()
# Exit the window when it is clicked.
turtle.Screen().exitonclick()
