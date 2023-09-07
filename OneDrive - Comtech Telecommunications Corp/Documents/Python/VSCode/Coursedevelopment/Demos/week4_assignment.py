import random
import turtle
from time import sleep

# Returns whether or not the turtle is still inbounds. 
def isInScreen(win,turt):
    stillIn = True
    if float(turt.xcor()) > win.window_width() / 2 or float(turt.xcor()) < -win.window_width() / 2:
        stillIn = False
    if float(turt.ycor()) > win.window_height() / 2 or float(turt.ycor()) < -win.window_height() / 2:
        stillIn = False
    return stillIn

# Moves a turtle randomly using parameters for the turtle and whether or not it will be half the distance
def moveRandomly(t,half):
        coin = random.randrange(0, 2)
        if coin == 0:
            t.left(90)
        else:
            t.right(90)
        if half == False:
            t.forward(50)
        else:
            t.forward(25)

def main():
    wn = turtle.Screen()
    # Turtles defined
    june = turtle.Turtle()
    june.shape('turtle')

    fred = turtle.Turtle()
    fred.shape('turtle')
    fred.color('purple')
    fred.penup()
    fred.goto(100,0)
    fred.pendown()
    # While statement for moving turtles
    counter = 0
    while isInScreen(wn,june):
        # True and False statements so Fred is only moved 1/2 the distance of June
        moveRandomly(june,False)
        # Counter to move Fred once for every 5 of June's moves
        counter += 1
        if counter % 5 == 0:
             moveRandomly(fred,True)
    # Makes it easier to see which turtle is where at the end. 
    sleep(5)
    # Compares y coordinates to see which turtle is higher then stamps the lower turtle and moves it to the middle for writing. 
    if june.ycor() > fred.ycor():
        fred.stamp()
        fred.penup()
        fred.goto(0,0)
        fred.pendown()
        fred.ht()
        fred.write("Fast turtle was on top")
        
    else:
        june.stamp()
        june.penup()
        june.goto(0,0)
        june.pendown()
        june.ht()
        june.write("Slow turtle was on top")

    wn.exitonclick()

main()
