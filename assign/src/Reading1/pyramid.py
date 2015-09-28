__author__ = 'djhake2'
# Load TurtleWorld functions
from TurtleWorld import *
from math import *

# Function to have turtle 't' draw a square of size 'x' CCW
def square(t,x):
	pd(t)
	i = 4
	while i > 0:
		fd(t,x)
		lt(t,90)
		i = i - 1
	pu(t)

# Function to have turtle 't' draw a row of 'x' blocks (squares) of a fixed size (20)
def row(t,x):
	i = x
	while i > 0:
		square(t, 20)
		fd(t,20)
		i = i - 1
	bk(t,x * 20)

# Function to have turtle 't' draw a pyramid of 'x' rows using blocks (squares) of size relative to length of row
# TODO: add pyramid function here,




def main():
	# Create TurtleWorld object
	world = TurtleWorld()
	# Create Turtle object
	t = Turtle()
	t.delay = 0.001

	# Draw graphics
	pyramid(t,5)

	# Press enter to exit
	key = input('Press enter to exit')
	world.destroy()

main()