def rightJustify():
    inputString = input("Insert the string: ")
    if (len(inputString) > 10):
        print(len(inputString))
    elif (len(inputString) == 7):
        print("This is long enough")
    elif (len(inputString) == 8):
        print("This is long enough again")            
    else:
        print("the string is too short")
    
rightJustify()

def drawGrid():
    width = input("Insert the width: ")
    height = input("Insert the height: ")
    print(width, height)

drawGrid()

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total) ** 2
    return square

x =1
y = x + 1
print(c(x, y + 3, x + y))

def hasDuplicates(myList):
    myName = input("Insert your name: ")
    myNickname = input("insert your nickname: ")
    myFavouriteName = input("Insert how you want to be called: ")
    myList = [myName, myNickname, myFavouriteName]
    check = []
    for item in myList:
        if item == check:
            print("you have a duplicate")
        else:
            print("You don't have duplicate")
    print(myList)

hasDuplicates(myList)

def factorial(n):
    product = 1
    while n > 0:
        product = product * n
        n = n - 1
    return product
