#Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

radius = int(input("Enter circle radius: "))
area = radius**2 * math.pi

print(f"Area = {area}")
