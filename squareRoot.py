def getEstimate(x):
    return x / 2

value = input("Enter the value to calculate the square root: ")
a = float(value)
x = getEstimate(a)

for i in range(1, 100):
    x = (x + a / x) / 2

print("Square root is: " + str(x))