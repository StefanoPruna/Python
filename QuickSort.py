def rotatedAround(toSort, a , b):
    p = toSort[(a + b) // 2]
    i, j = a - 1, b + 1 #i and j are elements in the toBeSorted list, i starts from 0 while j starts from the last element 6
    while True:
        i, j = i + 1, j - 1
        while toSort[i] < p:
            i += 1
        while toSort[j] > p:
            j -= 1
        if i >= j:
            return(i)
        toSort[i], toSort[j] = toSort[j], toSort[i]
        i-= 1 #swap the elements around
        
def quicksort(toSort, a, b):
    if a < b:
        p = rotatedAround(toSort, a, b)
        quicksort(toSort, a, p - 1)
        quicksort(toSort, p + 1, b)
    return(toSort)

def qs(toSort):
    return quicksort(toSort, 0, len(toSort) -1)

toBeSorted = [13, 21, 7, 42, 18, 12, -5]
print(qs(toBeSorted))