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

def calculatestrangevalue():
    while True:
        try:
            x = int(input("Enter the value of x: "))
            y = int(input("Enter the value of y: "))
            assert 
        if y > x:
            product = int(mul(3, 5) * add(5, 8))
            print(product)
        elif x > y:
            product2 = int(div(2, 4) * sub(5, 2))
            print(product2)
        break

def isValidPositiveIntegerInput(value):
    try:
        assert value > 0
        return True
    except ValueError:
        print("Number of branches must be at least 1: ")
        return False

add(2,3)
sub(5, 2)
mul(5, 5)
div(6,2)
calculatestrangevalue()
isValidPositiveIntegerInput(4)