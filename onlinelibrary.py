""" Function 1: Asking the question until the input isn't: 0, a negative or not a number """
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
            return branches
            break

#Fucntion 2: Ask for the number of books for each category for each branch 
def checkBooks():
    while True:
        try:
            computer = int(input("Enter the number of books for Computer of branch " + nBranch + ":"))
            physics = int(input("Enter the number of books for Physics of branch " + nBranch + ":" ))
            chemistry = int(input("Enter the number of books for Chemistry of branch " + nBranch + ": "))
            biology = int(input("Enter the number of books for Biology of branch " + nBranch + ": "))
            arts = int(input("Enter the number of books for Arts of branch " + nBranch + ": "))    
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
            return bookCategories
            break

def checkTotalBooks():
    nBranch = 1
    checkBranches()
    checkBooks()
    while True:
        for book in bookCategories:
            if nBranch in bookCategories:
                nBranch += 1
                checkBooks()
            else:
                total = sum(bookCategories.values())
                print(branches, total, bookCategories)
                break

checkTotalBooks()
        
        # Alternative way to sum the total
        # result = {}
        # #bookCategories = ["Computer", "Physics", "Chemistry", "Biology", "Arts"]
        # for book in bookCategories:
        #     if book in bookCategories:
        #         result[book] = result.get(countTotal, 0) + 1
        # return result
       




