#This has been modified from the original submission

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

phil.penup()
phil.goto(-50, 0)
phil.pendown()

choice = input("What pallet would you like? type 'cool', 'primary', 'gray' or 'choose my own' \n")
if choice.lower() == 'primary':
    color_list = ['red', 'orange', 'green', 'yellow']
elif choice.lower() == 'cool':
    color_list = ['magenta', 'violet', 'maroon', 'navy']
elif choice.lower() == 'gray':
    color_list = ['Gainsboro', 'AliceBlue', 'LightSlateGray', 'dimgray']
else:
    t_colors = ['red', 'orange', 'yellow', 'green', 'purple', 'pink', 'brown', 'gray', 'gold']
    color_list = []
    for _ in range(4):
        for a_color in t_colors: print(a_color)
        user_color = input('Please choose a color from the list above. \n')
        color_list.append(user_color)
# The loop for Phil to create an octagon
for color in color_list:
    # Start to fill the shape Phil makes before beginning the loop to create the shape.
    phil.begin_fill()
    for _ in range(8):
        phil.color(color)
        phil.forward(75)
        phil.left(45)
    # End the fill after the shape is complete
    phil.end_fill()
    phil.penup()
    phil.forward(40)
    phil.right(90)
    phil.forward(40)
    phil.pendown()


    # Hide Phil so there isn't a bump in the shape
    phil.ht()

# Exit the window when it is clicked. 
turtle.Screen().exitonclick() 