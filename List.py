#LIST = they can be modified, while ARRAY are fixed

myList = ["Monday", "Tuesday", "Wednesday", 123, 54.4, [1, 2, 3]]
print(myList)
print(myList[3])
print(myList[-4]) #Python will start from the end of the array/list
print(myList[-1])
#print(mylist[7])

weekend = ["Saturday", "Sunday", "Monday"]
"Monday" in weekend #look for "Monday" in the weekend list, thus false
print(len(weekend))
for week in weekend:
    print(week)
weekend["Sunday"] = weekend["Tuesday"]
print(weekend)
for days in weekend:
    weekend[days] = weekend[days("Tuesday", "Wednesday")]
print(days)

numbers = [2, 4, 6, 8]
for i in range(len(numbers)):
    numbers[i] = numbers[i] // 2
print(numbers)
numbers[2] = numbers[2] + 1 #it modifies the third item in the list by adding 1 in the number
print(numbers)
print(numbers[1: 3]) #start to print from the second element in the list, print until the fourth element in the list
numbers.extend([6, 7]) # extend is to add item in the list
print(numbers)
numbers.pop(2) #pop is to remove item in the list
print(numbers)
#numbers.sort() is to sort numerically the numbers in a list from the lowest to the highest
