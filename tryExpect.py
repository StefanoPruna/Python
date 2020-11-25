def divide():
    try:
        x = int(input("insert the first number: "))
        y = int(input("insert the second number: "))
        result = x / y
        raise TypeError("Expected integer")
    except ZeroDivisionError:
        print("Divide by zero")
    else:
        print("Result is ", result)
    finally:
        print("all done")

divide()
