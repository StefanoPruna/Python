def hasDuplicates():
    myName = input("Insert your name: ")
    myNickname = input("insert your nickname: ")
    myFavouriteName = input("Insert how you want to be called: ")
    myList = [myName, myNickname, myFavouriteName]
    if len(myList) != len(set(myList)):
        print("you have a duplicate")
    else:
        print("You don't have duplicate")
    print(myList)

hasDuplicates()

def count():
        if word1 == word2:
            print("they are the same")
        else:
            print("they are different")

word1 = input("Insert the first word: ")
word2 = input("insert the second word: ")
count()