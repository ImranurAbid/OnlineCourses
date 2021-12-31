import math

def area_of_equilateral_triangle(side):
    equation = math.sqrt(3) * side ** 2 / 4
    return equation
    
print("Area of an equilateral triangle with sides 2 is", area_of_equilateral_triangle(2))
print("Area of an equilateral triangle with sides 5 is", area_of_equilateral_triangle(5))

#OUTPUT:
        # Area of an equilateral triangle with sides 2 is 1.732050807568877
        # Area of an equilateral triangle with sides 5 is 10.82531754730548