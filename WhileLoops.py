n = 10
while n > 10:
    print(n)
    n -= 1
print("Program finish")

while True:
    line = input("Do you want to finish? ")
    if line == 'Y' or line == 'y':
        break