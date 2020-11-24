""" Check if the first letter is any lower case letter, otherwise returns False """
def any_lowercase1(s):
        for c in s: 
         if c.islower():
          return True
         else:
          return False

#print(any_lowercase1("hello"))
#print(any_lowercase1("HeLLo"))

""" Check if the letter in the appendix is lower (return true) or upper case (return false) """
def any_lowercase2(s):
        for c in s:
         if 'c'.islower():
          return 'True'
         else:
          return'False'

#print(any_lowercase2("HELLO")) #Even if I assign a value here, it won't consider it

""" If the last character is lower case, it will return True, otherwise it wil return False """
def any_lowercase3(s):
  for c in s:
    flag = c.islower()
  return flag

#print(any_lowercase3("HELLO"))
#print(any_lowercase3("HELLo"))

""" Check if there is at least one lowercase character """
def any_lowercase4(s):
  flag = False
  for c in s:
    flag = flag or c.islower()
  return flag

  print(any_lowercase4("Hello"))
  print(any_lowercase4("HELLO"))
  print(any_lowercase4("hello"))
  

""" If they are all lower case, it will return True, otherwise False """
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5("Hello"))
print(any_lowercase5("HELLO"))
print(any_lowercase5("hello"))


weight = {"pencil": 10, "pen": 20, "paper": 4, "eraser": 80}
available = {"pen": 3, "pencil": 5, "eraser": 2, "paper": 10}
overall_weight = 0
for count in weight:
  if count in available:
    overall_weight += available[count] * weight[count]

print("Overall weight: ", overall_weight)   