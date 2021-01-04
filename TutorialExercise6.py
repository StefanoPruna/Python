#Iterative method
def isPalindrome(word):
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

# Recursion method
# def isPalindrome(word):
#     if len(word) < 1:
#         return True
#     else:
#         if word[0] == word[-1]:
#             return isPalindrome(word[1:-1])
#         else:
#             return False
      
while True:
    possiblePalindrome = input("Enter a word/phrase to check: ")
    if isPalindrome(possiblePalindrome):
        print(possiblePalindrome, "is a palindrome")
        break
    else:
        print(possiblePalindrome, "is not a palindrome")