#Bhaskara's formula

import math

#Data to be entered by the user

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

#Equation

delta = ((b ** 2) - (4 * a * c))

#Results

if delta < 0:
    print("This equation has no real roots")
elif delta == 0:
    x0 = -b / (2 * a)
    print("The root of this equation is",x0)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 <= x2:
        print(f"The roots of the equation are {x1} e {x2}.")
        print(f"And delta is equal to {delta}.")
    else:
        print(f"The roots of the equation are {x2} e {x1}.")
        print(f"And delta is equal to {delta}.")