__author__ = 'dbabcock'

# Load TurtleWorld functions
from TurtleWorld import *
from math import *


# Function to draw a square CCW
def square(t, x):
    pd(t)
    fd(t, x)
    lt(t, 90)
    fd(t, x)
    lt(t, 90)
    fd(t, x)
    lt(t, 90)
    fd(t, x)
    lt(t, 90)
    pu(t)


def main():
    # Create TurtleWorld object
    world = TurtleWorld()
    # Create Turtle object
    crush = Turtle()
    crush.delay = 0.001

    # Draw graphics
    square(crush, 10)
    lt(crush, 45)
    fd(crush, sqrt(2) * 10)
    rt(crush, 45)
    square(crush, 20)
    lt(crush, 45)
    fd(crush, sqrt(2) * 20)
    rt(crush, 45)
    square(crush, 30)
    lt(crush, 45)
    fd(crush, sqrt(2) * 30)
    rt(crush, 45)

    # Press enter to exit
    key = input('Press enter to exit')
    world.destroy()

main()

