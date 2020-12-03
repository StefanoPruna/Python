""" Function 1: Calculate the total amount of books and the average number of books per category"""
def countTotal():
    total = sum(bookCategories.values())
    average = float(total / 5)
    print("The Books per category are: " + str(bookCategories) + ";")
    print("The total amount of books are: " + str(total) + ";")
    print("And the average of books is: " + str(average))


""" Function 2: Asking the question until the input isn't: 0, a negative or not a number """
def checkBranches():
    while True:
        try:
            branches = int(input("Enter the number of branches of the main library: "))
            assert branches > 0 #Check if it's at least 1
        except (ValueError, TypeError): #Check if the input is not a number
            print("Number of branches must be an integer: ")
        except AssertionError: #Check if the input is 0 or negative
            print("Number of branches must be at least 1: ")
        else:
            print("The branches are in total: " + str(branches))
            break
    

""" 
Fucntion 3: Ask for the number of books for each category for each branch 
Note: I'm not able to make it loop, I cannot find a solution, it only asks once
"""    
checkBranches()
while True:
    try:
        computer = int(input("Enter the number of books for Computer of branch: "))
        physics = int(input("Enter the number of books for Physics of branch: " ))
        chemistry = int(input("Enter the number of books for Chemistry of branch: "))
        biology = int(input("Enter the number of books for Biology of branch "))
        arts = int(input("Enter the number of books for Arts of branch: "))    
        bookCategories = {"Computer": computer, "Physics": physics, "Chemistry": chemistry, "Biology": biology, "Arts": arts} 
        assert computer > 0
        assert physics > 0
        assert chemistry > 0
        assert biology > 0
        assert arts > 0
    except (ValueError, TypeError):
        print("Number of books must be an integer: ")
    except AssertionError:
        print("Number of books must be non-negative: ")
    else:
        countTotal()
        break