from math import pi


def rectangleArea(length, width):
    return length * width


def cylinderVolume(radius, height):
    return pi * radius**2 * height


rectangleLength = float(input("enter the length of the rectangle: "))
rectangleWidth = float(input("enter the width of the rectange: "))
print(f" the area of the rectangle is {rectangleArea(rectangleLength, rectangleWidth):.2f}cm\u00b2")


cylinderRadius = float(input("enter the radius of the cylinder: "))
cylinderHeight= float(input("enter the height of the cylinder: "))
print(f" the volume of the cylinder is {cylinderVolume(cylinderRadius, cylinderHeight):.2f}cm\u00b3")

