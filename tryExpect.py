def divide():
    while True:
        try:
            x = int(input("insert the first number: "))
            y = int(input("insert the second number: "))
            result = x / y
            assert x > 0
            assert y > 0
            #raise TypeError("Expected integer")
        except (ValueError, TypeError):
            print("It must be an integer")
        except ZeroDivisionError:
            print("Divide by zero")
        except AssertionError:
            print(" Expected integer")
        else:
            print("Result is ", result)
            break
        finally:
            print("all done")
            

divide()
