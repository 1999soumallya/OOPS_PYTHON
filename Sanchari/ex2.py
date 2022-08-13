import math


def ex2(radius, height):
    Quantity = ((math.pow(radius, 2)) * ((2 * radius) + height))
    print("Total quantity is:", Quantity)


radius = int(input("Enter the radius:"))
height = int(input("Enter the height: "))
ex2(radius, height)
