#Exam of 2016
def countWords(text):
    count = 0
    whiteSpace = " "
    for i in text:
        if i in text and i != whiteSpace:
            count +=1
    print(count)

countWords("   Hello how  ")

#
#Exam of 2017
def isPalindrome(word):
    for i in word:
        if len(word) <= 1:
            #return True
            print("true " + word)
        elif word[0] != word[-1]:
            #return False
            print("False " + word)
        else:
            print(word[1:-1])


def palindromeLength(word):
    if isPalindrome:
        print(word)
    else:
        print(-1)


isPalindrome("abba")
isPalindrome("a")
isPalindrome("university")
palindromeLength("colleague")