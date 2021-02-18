def countWord(text):
    #returns the number of words in the string parameter
    try:
        text = " hello "
        assert(" hello ")
    except ValueError:
        print("the word is not a string")


print(countWord("hello "))