from tkinter import *
from tkinter import ttk

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

root = Tk() #creates a new window
root.title("Sorting the numbers from the list")

frame = ttk.Frame(root, width = 1600, height = 1600, padding = "3 3 12 12") #padding=left-right-top-bottom
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame.configure(borderwidth = 5)
root.columnconfigure(0, weight = 2)
root.rowconfigure(0, weight = 2)
frame["relief"] = "groove"

label = ttk.Label(frame)
label.grid(row = 1)
sort = StringVar()
sort.set("Numbers to be sorted from this list:\n13, 21, 7, 42, 18, 12, -5")
label["textvariable"] = sort
label["justify"] = "center"

toBeSorted = [13, 21, 7, 42, 18, 12, -5]
#print(qs(toBeSorted))

tosortButton = ttk.Button(frame, text = "Sort the numbers", command = qs(toBeSorted)) #when we press the Go button, run the calculate function
tosortButton.grid(row = 2)

sorted = StringVar()
sorted.set(qs(toBeSorted))
sortedLabel = ttk.Label(frame, textvariable = sorted)
sortedLabel.grid(row = 4)

for child in frame.winfo_children():
    child.grid_configure(padx = 15, pady = 10)

root.mainloop()