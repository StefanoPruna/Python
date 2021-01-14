#The following method is called selection sort, linear search, check one item in the list at the time
def indexSmallest(toBeSorted, lower, upper):
    minIndex = lower
    for i in range(lower +1, upper):
        if toBeSorted[i] < toBeSorted[minIndex]:
            minIndex = i
    return minIndex

def selectionsort(toBeSorted):
    for i in range(len(toBeSorted) - 1):
        j = indexSmallest(toBeSorted, i , len(toBeSorted) - 1)
        toBeSorted[i], toBeSorted[j] = toBeSorted[j], toBeSorted[i]
    return toBeSorted

toBeSorted = [13, 21, 7, 42, 18, 12, -5]
toBeSorted.append(-3)
print(selectionsort(toBeSorted))

#The easiest and faster way to sort though, is the following:
# toBeSorted.sort(reverse=True)
# print(toBeSorted)