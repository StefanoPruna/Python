#Insertion Sort method
def insertionSort(toBeSorted):
    for i in range(1, len(toBeSorted)):
        j = i
        while j > 0 and toBeSorted[j] < toBeSorted[j - 1]:
            toBeSorted[j - 1], toBeSorted[j] = toBeSorted[j], toBeSorted[j-1]
            j = j -1
    return toBeSorted

toBeSorted = [13, 21, 7, 42, 18, 12, -5]
print(insertionSort(toBeSorted))