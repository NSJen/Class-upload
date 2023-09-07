import turtle

# Create the window
wn = turtle.Screen()
wn.bgcolor('blue')

# Create Phil the turtle
phil = turtle.Turtle()
phil.color("white")
phil.pensize(9)
phil.shape('turtle')

# Start to fill the shape Phil makes before beginning the loop to create the shape.
phil.begin_fill()

# The loop for Phil to create an octagon
for _ in range(8):
    phil.forward(75)
    phil.left(45)

# End the fill after the shape is complete
phil.color('red')
phil.end_fill()
phil.color('white')

phil.penup()
phil.left(123)
phil.forward(65)
phil.pendown()
phil.write("STOP", font=("Arial", 42, "normal"))

# Hide Phil so there isn't a bump in the shape
phil.ht()

# Exit the window when it is clicked.
turtle.Screen().exitonclick()