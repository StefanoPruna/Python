def add(x, y):
    result = x + y
    print(result)

def sub(x, y):
    result2 = y - x
    print(result2)

def mul(x, y):
    result3 = x * y
    print(result3)

def div(x, y):
    result4 = x / y
    print(result4)

add(2,3)
sub(5, 2)
mul(5, 5)
div(6,2)

#THE FUNCTION CALCULATESTRANGEVALUE() DOESN'T STOP - IT NEEDS TO BE FIXED - IT'S MY WAY
def calculatestrangevalue():       
    while True:
        try:
            x = int(input("Enter the value of x: "))
            y = int(input("Enter the value of y: "))
            assert x and y > 0
            if y > x:
                return mul(x, y) * add(x,y)
            elif x > y:
                return div(x, y) * sub(x, y)
            else:
                return 1                               
        except (TypeError, ValueError):
            print("It has to be an integer")
        except AssertionError:
            print("X and Y must be positive numbers")
            break

"""
HERE BELOW IT'S HOW THE TUTOR HAS DONE IT, but it's not working
def calculateValue():
    if y > x:
        return mul(x, y) * add(x, y)
    elif x > y:
        return div(x, y) * sub(x, y)
    else:
        return 1

def checkIfInteger(value):
    if not isinstance(value, (str, int)):
        print("X and Y must be positive numbers")
    try:
        value = int(value)
    except (TypeError, ValueError):
        print("It has to be an integer")
    return value > 0

def askForInput():
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    while not checkIfInteger(x, y):
        x = int("Enter a positive integer: ")
        y = int("Enter a positive integer: ")
    x = int(x)
    y = int(y)

"""
calculatestrangevalue()

#print(calculateValue())

if __name__ == "__main__":
    calculatestrangevalue()
    #askForInput()