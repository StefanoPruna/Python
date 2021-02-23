# start = input("Enter a value: ")
# n = int(start)
# while n != 1:
#     print(n)
#     if n % 2 == 0: # n even
#         n = n // 2 #ignore the decimals 5:2= 2 only
#     else: # n odd
#         n = 3 * n + 1


c = 1 < 2 and 1 + 1 < 3
print(c)

m = [1,2,3,4]
for i in range(len(m)):
    m[i]+=1
    print(m)
    if i<2:
        m[i] += m[i+1]

print(m)

#TRUE OR FALSE
# n=1 

# n ==2 or 2<3

# n ==2 and 2<3

# not(n==2 and 2<3)

# not n==2 and 2<3

# n==1 or n==2 and n>=3

# n==1 or n==2 and 2>=3

# n==1 or n==2 and 2 >= 3

# n==1 or n==2 and 2 <= 3

# n==1 or n==2 and 2 = 3

# n==1 or n==2 and 2 = 3


#list Slices
numbers = [2,4,6,8,10]
print(numbers[1:3]) #print from the index 1 util index 2, avoid the third index

print(numbers[:3]) #print from index 0 before the index 3

print(numbers[1:]) #pring from index 1

numbersCopy = numbers[:]
numbersCopy[1]=3 #copy the list numbers, but substitute the number in the index 1 with the number 3
print(numbers, numbersCopy)

numbers[1:3] = [3,5] #substitute the numbers from the index 1 to 2 with 3 and 5
print(numbers)

numbers.append(6) #add 6 to the list exitat the end

#
m = [1,2,3,4] 
for i in range(len(m)): # index i is = 0,1,2,3
    m[i] *=2 #multiply the first index number by 2 which is 2, then go to the if; second turn mulitply the second index by 2 which is 4; then 3*2=6;then 4*4=8
    print(m)
    if i<2:
        m[i] -= m[i+1] #the index i is 0, so substruct the first index result with the second 2-2=0, then start from the beginning; now the index i is 1, 
                       #so substruct the second result m[i] 4 with 3, =1; third time i is 3,
                       #which is not less than 2, thus 6 2
                       #and so restart; then 8 is not less than 2 and finish the for in loop and log to the console the new m list 0,1,6,8
        #print(m)
print(m)

#
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c,0) +1 #print one letter at the time according to the parameters provided plus the number 1
        #print(c) #without this print, it will only print 1
    return d 

print(histogram("hello, world")[" "]) #it will only print 1 unless we put a print in the for in loop

#
for x in range(3, 9,2): #print in from 3 to 8 every second number
    print("x=",x)

for x in range(3, 9): #print from 3 to 8 each number
    print("x=",x)

# 
s = "{0}% of {1} is {2:.2}".format(1.5, 25, 0.375) #the last data will print the number round up from hundreth/centesimi, 0.38
print(s)
s = "{0}% of {1} is {2:.1}".format(1.5, 25, 0.375) #the last data will print the number round up from decimal, 0.4
print(s)
s = "{0}% of {1} is {2:.3}".format(1.5, 25, 0.374) #the last data will print the number from thousandt/millesimo, 0.374
print(s)

#
n=[1,2,3]
m = 3 if 3==len(n)else 4 #print (m)3 if 3 is the length of the list n
print(m)

#
def func(n):
    if n<1:
        return n
    return func(n/2)
print(func(9))

#
def factorial(n):
    result=1
    while n<0:
        n -= 1
        result = result * n
    return result

print(factorial(5))