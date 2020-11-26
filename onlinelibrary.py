
""" Function 1: Asking the question until the input isn't: 0, a negative or not a number"""
while True:
    try:
        branches = int(input("Enter the number of branches of the main library: "))
        assert branches > 0 #Check if it's at least 1
        break
    except (ValueError, TypeError): #Check if the input is not a number
        print("Number of branches must be an integer: ")
    except AssertionError: #Check if the input is 0 or negative
        print("Number of branches must be at least 1: ")

""" Fucntion 2: Ask for the number of books for each category for each branch """
while True:
    try:
        computer = int(input("Enter the number of books for Computer of branch" + ": "))

        bookCategories += bookCategories * branches
bookCategories = ["Computer", "Physics", "Chemistry", "Biology", "Arts"]
for book in bookCategories:
    if book in bookCategories:



