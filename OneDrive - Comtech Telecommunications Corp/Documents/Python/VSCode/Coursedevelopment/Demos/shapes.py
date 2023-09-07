# Illustrate calling a turtle function 
# John Cigas, 2/10/2019

import turtle
from random import randint

def drawShape(t, sz, sides):
    # Creates the filled shape
    """Make turtle t draw a random shape of with side sz."""
    t.begin_fill()
    for _ in range(sides):
        t.forward(sz)
        t.left(360/sides)
    t.end_fill()

def moveTurtle(t):
    # Moves the turtle to a randomized location
    t.penup()
    t.right(randint(0,360))
    t.forward(randint(-200,200))
    t.pendown()

def main():
    # Creates turtle and brings together the other functions

    wn = turtle.Screen()         
    wn.bgcolor("lightgreen")
    alex = turtle.Turtle()  

    # draws a navy decagon
    alex.color('navy')    
    drawShape(alex, 50, 10)         

    # draws a larger, light blue hectagon
    moveTurtle(alex)
    alex.color('light blue')  
    drawShape(alex, 100, 7)  

    # draws a dark blue shape of a random size with a random number of sides
    moveTurtle(alex)
    alex.color('Darkblue')
    drawShape(alex, randint(10,200), randint(3,25))

    wn.exitonclick()
    
# Calls the main function
main()