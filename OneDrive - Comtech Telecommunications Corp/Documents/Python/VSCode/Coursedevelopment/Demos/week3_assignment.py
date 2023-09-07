#This has been modified from the original submission

'''
Jennifer Williams
August 29, 2023
CS152 Week 3 assignment 1
smaller octagons

'''

import turtle
import random

# Define function for creating random colors from the hardcoded list. 
def rand_color():
    return t_colors[random.randint(0,14)]

# define the color list
t_colors = ['red', 'orange', 'yellow', 'green', 'purple', 'pink', 'brown', 'gray', 'gold', 'bisque', 'AntiqueWhite', 'Medium Aquamarine', 'DarkOliveGreen', 'MediumOrchid', 'MidnightBlue']
random_location = -random.randrange(0,150)

# Create the window
wn = turtle.Screen()
wn.bgcolor('bisque')

# Create Phil the turtle
pen_size = random.randint(1,10) #This needed to be a variable to compare it in the while loop
phil = turtle.Turtle()
phil.color(rand_color())
phil.pensize(pen_size)
phil.shape('turtle')

# get phil in position
phil.penup()
phil.goto(0, random_location)
phil.pendown()

# Create the color lists to be used
color_list= []
choice = input("What pallet would you like? type 'cool', 'primary', 'gray', 'choose my own' or 'surprise me' \n")
if choice.lower() == 'primary':
    color_list = ['red', 'orange', 'green', 'yellow']
elif choice.lower() == 'cool':
    color_list = ['magenta', 'violet', 'maroon', 'navy']
elif choice.lower() == 'gray':
    color_list = ['Gainsboro', 'AliceBlue', 'LightSlateGray', 'dimgray']
elif choice.lower() == 'surprise me':
    for _ in range(4):
        color_list.append(rand_color())
elif choice.lower() == 'choose my own':
    print(t_colors)
    for _ in range(4):
        
        user_color = input('Please choose a color from the list above. \n')
        color_list.append(user_color)

# The loop for Phil to create octagons in 4 colors beginning with a random size and getting progressively smaller. 
side = random.randrange(90,200,2)
keep_going = 'yes'
while keep_going == 'yes':
    # Phil's speed changes with each color set
    phil.speed(random.randrange(0,11))

    for color in color_list:
        # Start to fill the shape Phil makes before beginning the loop to create the shape, limited to even numbered side lengths.
        phil.begin_fill()
        
        for _ in range(8):
            phil.fillcolor(color)
            phil.left(45)
            phil.forward(side)
            # I added the dot to each corner because I used many methods already. 
            phil.dot()
        # The octagon gets porportionately smaller each time. 
        side -= side * (.25)
        # End the fill after the shape is complete
        phil.end_fill()
        phil.penup()
        phil.goto(0,random_location)
        phil.pendown()


        # Hide Phil so there isn't a bump in the shape
        phil.ht()
    if side > pen_size: 
        keep_going = 'yes'
    else:
        print("I can no longer continue")
        break

# Exit the window when it is clicked. 
turtle.Screen().exitonclick() 