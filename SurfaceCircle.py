# Write a program that takes the radius of circle as input and prints the surface of the circle
import math

rad = float (input ("input the radious of the circle "))

area = (math.pi * (rad ** 2))
print("The surface of the circle with radious " + str(rad) + " is " + str(area))