total_cost = 0
cost_of_nail = 1

for horse_foot in range(4):
    for nail in range(6):
        # TODO: Add price of current nail to total_cost and determine the cost of the next nail
        cost_of_nail *= 2 
        print(cost_of_nail)

total_cost = cost_of_nail - 1
print("The total cost to shoe the horse would be ${0:.2f}".format(total_cost / 100))

#Order of growth: 2 - 4 - 1 - 3 = they are all n3
#(n2 +5)(67n3 +93) = O(n2 * n3) = O(n5)

# def findTarget(tosort, k):
#     index = hash(k) % len(tosort)
#     return tosort[index]

def linear(toBeSorted, target):
    # toBeSorted = findTarget(tosort, target)
    for i in toBeSorted:
        if i == target: #print(get(map, 2))
            return target #this is a linear search to go through all items in the list
    raise TypeError("the number is not in the list")

# def bisection(toBeSorted, target):
#     #Note: the list has to be sorted to be used
#     lower = 0
#     upper = len(toBeSorted) - 1

toBeSorted = [13, 21, 7, 42, 18, 12, -5]
print(linear(toBeSorted, toBeSorted[4]))
#print(bisection(toBeSorted))
# toBeSorted = tosort
# print(linear(toBeSorted, toSort[4]))