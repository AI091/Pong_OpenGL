from numpy import pi 
from random import random

def line_collesion(left_1, right_1, left_2, right_2):
    if left_2 <= right_1 and left_1 <= right_2:
        return True
    return False

def generate_angle(min , max):
    theta = (random() -0.5 ) * pi # Generates a random angle between 90 and -90 
    while abs(theta) > max or abs(theta) < min: 
        theta = (random() -0.5 ) * pi

    return theta

