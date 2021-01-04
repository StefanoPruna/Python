square = []
for x in range(10):
    square.append(x*x)
    print(square)

#Another way to run the program is, but in this case it will show the result all in one row only:
squares = [x * x for x in range(10)]
print(square)

#more complex way to write command in one line
[(x, y) for x in range(3) for y in [2, 4, 1] if x != y]
#print(x, y) gives me an error on y is not defined

a = 3
listA = [0]
listB = listA
listB.append(a)
print(listA, listB)