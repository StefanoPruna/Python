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
            break                           #THE PROGRAM DOESN'T STOP - IT NEEDS TO BE FIXED
        except (TypeError, ValueError):
            print("It has to be an integer")
        except AssertionError:
            print("X and Y must be positive numbers")
        

"""
def isValidPositiveIntegerInput(value):
    try:
        assert value > 0
        return True
        print("it's true")
    except ValueError:
        print("Number of branches must be at least 1: ")
        return False
        print("it's false")
"""
calculatestrangevalue()
#isValidPositiveIntegerInput(4)

if __name__ == "__main__":
    calculatestrangevalue()