'''
Jennifer Williams
August 29, 2023
CS152 Week 3 Assignment 2
Circles and Triangles

'''


import turtle
import math
from random import choice

def drawFilledCircle(t,rad):
    # Draws a filled circle
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

def drawEquilateralTriangle(t,side):
    # Draws an equilateral triangle
    for _ in range(3):
        t.forward(side)
        t.right(120)

def getSide(len,wid):
    # Gets the length of the side when the size of a triangle is known
    return math.sqrt(len*wid*4/math.sqrt(3))
    # called with the statement tri_side = getSide(length,width)

def getRad(length,width):
    # Gets the radius of a circle when the length and width are known
    return math.sqrt(length*width/math.pi)
    # called with the statement radius = getRad(length,width)

def moveTurtle(t,location):
    # Moves the turtle to a defined position without making a line
    t.penup()
    t.goto(location)
    t.pendown()

def changeColor():
    # Chooses two random colors from the color list
    color_list = ['beige', 'blue', 'DarkRed', 'gold', 'green', 'navy', 'gray', 'CadetBlue', 'BlanchedAlmond', 'DarkOliveGreen1', 'DarkSlateBlue', 'DarkSalmon', 'LemonChiffon', 'orchid1', 'NavajoWhite4', 'purple4', 'turquoise', 'VioletRed4']
    color1 = choice(color_list)
    color_list.remove(color1)
    color2 = choice(color_list)
    return color1,color2
    
# define global variable
ted = turtle.Turtle()

# Creates the main function
def main():
  
    #define local variables
    tri_side = getSide(47, 102)
    radius = getRad(40,70)
    color1,color2 = changeColor()
   
    # Draw beige triangle with blue triangle inside
    ted.color(color1)
    ted.begin_fill()
    drawEquilateralTriangle(ted,tri_side)
    ted.end_fill()

    ted.color(color2)
    ted.begin_fill()
    drawEquilateralTriangle(ted,tri_side/2)
    ted.end_fill()

    # Draw a blue circle with a beige circle inside
    drawFilledCircle(ted,radius)
    ted.color(color1)
    drawFilledCircle(ted,radius/2)

    ted.hideturtle()

# Put the triangle and circles in different places
moveTurtle(ted,(90,70))
main()
moveTurtle(ted,(0,0))
main()
moveTurtle(ted,(-90,-70))
main()


turtle.Screen().exitonclick() 

