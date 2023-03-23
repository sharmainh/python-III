from math import pi
from math import floor

def calculate_sq_ft():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    return ("The square footage is {} sq.ft".format(area))


def circle_circumference():
    radius = int(input("Enter radius: "))
    circumference = floor(2*radius*pi)
    return ("The circumference is {} units".format(circumference)) 



