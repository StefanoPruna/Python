#The following method is called selection sort, checks the lowest value in the list and moves it in front and so on
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
# toBeSorted.sort(reverse=True) #Method, not function
# print(toBeSorted)