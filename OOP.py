#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
import copy
#Importing copy, i can assign the value/atributes of a var into another var

class myClass:
    x = 5

p1 = myClass()
print(p1.x)

#pointB = copy.copy(pointB)

class Point:
    pointA = 0
    #Represents a point in 2D space
    
class Rectangle:
    """Represents a rectangle.
    attributes: corner, width, height
    """

box = Rectangle()
box.width =10
box.height = 20
box.corner = Point()
box.corner.x = 5
box.corner.y = 4

def printPoint(p):
    print("({0}, {1})".format(p.x, p.y))

def findCentre(rectangle):
    p =Point()
    p.x = rectangle.corner.x + rectangle.width / 2
    p.y = rectangle.corner.y + rectangle.height / 2
    return p

pointC = findCentre(box)
printPoint(pointC)

pointA = Point()
pointA.x = 7.3
pointA.y = 9.3
pointB = copy.copy(pointA) #With import copy, It will assign all the pointA values to pointB until this line
pointA.x = 100
pointA.y = 3.4
pointB = copy.deepcopy(pointA)

printPoint(pointB)
printPoint(pointA)

pointA = Point()
type(pointA)

pointA.x = 0.0
pointA.y = 0.0
pointB = Point()
pointB.x =1.0
pointB.y = 2.5

def printPoint(p):
    print("({0}, {1})".format(p.x, p.y))


printPoint(pointA)
printPoint(pointB)