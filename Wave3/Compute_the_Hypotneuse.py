from math import sqrt

def pythagorean(a, b):
    return sqrt(a**2 + b**2)

a = float(input("a:"))
b = float(input("b:"))

print("Result:", pythagorean(a, b))