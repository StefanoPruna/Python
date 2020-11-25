
""" Asking the question until the input isn't: 0, a negative or not a number"""
while True:
    try:
        branches = int(input("Enter the number of branches of the main library: "))
        assert branches > 0 #Check if it's true
        break
    except (ValueError, TypeError): #Check if the input is not a number
        print("Number of branches must be an integer: ")
    except AssertionError: #Check if the input is 0 or negative
        print("Number of branches must be at least 1: ")

bookCategories = ["Computer", "Physics", "Chemistry", "Biology", "Arts"]


