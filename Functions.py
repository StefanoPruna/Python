type(2) # the return value is class int

def myFunction(): #to create a function we use def and has to be before we call it in the script
    a.sort()
    print(a)

a = int("5")
print(a)

a = [10, 5, 3, 1]
myFunction()

def addTogether(a, b):
    result = a + b
    return result

print(addTogether(1, 3))
print(addTogether("Ciao ", "Mondo"))

import math
math.sqrt(2)
math.factorial(3)

def calculateArea(radius):
    area = math.pi * radius * radius
    return area

circleArea = calculateArea(3)
print(circleArea)