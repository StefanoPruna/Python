from tkinter.constants import N
from typing import Sequence


def countWord(text):
    #returns the number of words in the string parameter
    try:
        text = " hello "
        assert(" hello ")
    except ValueError:
        print("the word is not a string")


print(countWord("hello "))

#
mess = "hello_world"
print(mess[2:5])

#
def sequence(a, b, c):
    if a< b <= c:
        return a+b+c
    else:
        return 0

print(sequence(9,10,10))

#
# numbers = [1,2,3]
# numbers[3]=1
# print(numbers) it will give an error, because there is not the index n.3

#
d={}
d["a"]=1
d["a"]=2
#d["a"]=3
print(d["a"])

#
s="report #{0:.2f}: {1}".format(123, 'delayed')
print(s)

#
orderDetails={}
orderDetails["quantity"]=1
orderDetails["item"]=1124
orderDetails["quantity"]=2
print(orderDetails)

#
x = -1
print(match.sqrt(x) if x>= 0 else 0)

#
def func(n):
    if n<1:
        #return n
        print(n)
    else:
        return print(func(n/2 -1))

func(9)

#
def test(k, m):
    if k < 0:
        return 1
    elif k + m > 5:
        return test(k, m-1)
    else:
        return k * test(m-1, k+1)
        

print(test(4, 3))

