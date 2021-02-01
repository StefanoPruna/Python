from tkinter import * #Import Graphical User Interfaces
from tkinter import ttk #ttk is the newer graphic/style
from tkinter import messagebox as mbox
import os
import tkinter  

#We collect all the data and with * we take any arguments and we sum the total
def takeInput(*args):
    try:
        varComputer = int(computer.get())
        varPhysics = int(physics.get())
        varChemistry = int(chemistry.get())
        varBiology = int(biology.get())
        varArts = int(arts.get())
        total.set(varComputer + varPhysics + varChemistry + varBiology + varArts)
        average.set((varComputer + varPhysics + varChemistry + varBiology + varArts) / 5)
    except (ValueError, TypeError): #Check if the input is not a number
        mbox.showerror("Python Error Message", "Error: Number of books must be an integer and at least 1")

#For this function the same as above, but we average the total
def takeAverage(*args):
    try:
        varComputer = int(computer.get())
        varPhysics = int(physics.get())
        varChemistry = int(chemistry.get())
        varBiology = int(biology.get())
        varArts = int(arts.get())     
        average.set((varComputer + varPhysics + varChemistry + varBiology + varArts) / 5)   
    except (ValueError, TypeError): #Check if the input is not a number
        mbox.showerror("Python Error Message", "Error: Number of books must be an integer and at least 1")
    
#Create the window
root = Tk() 
root.title("Online Library GUI")
frame = ttk.Frame(root, padding = "3 3 12 12")
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame["relief"] = "sunken"
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

for col in range(1, 3):
    frame.columnconfigure(col, weight = 1)

for row in range(1, 7):
    frame.rowconfigure(row, weight = 1)

computer = StringVar()
physics = StringVar()
chemistry = StringVar()
biology = StringVar()
arts = StringVar()
total = StringVar()
average = StringVar()


#Creates the design of the GUI
computerLabel = ttk.Label(frame, text = "Computer:", padding = "0 0 30 0")
computerLabel.grid(column = 1, row = 1, sticky = (W, E))
computerEntry = ttk.Entry(frame, width = 15, textvariable = computer)
computerEntry.grid(column = 2, row = 1, sticky = (W, E))

physicsLabel = ttk.Label(frame, text = "Physics:", padding = "0 0 30 0")
physicsLabel.grid(column = 1, row = 2, sticky = (W, E))
physicsEntry = ttk.Entry(frame, width = 15, textvariable = physics)
physicsEntry.grid(column = 2, row = 2, sticky = (W, E))

chemistryLabel = ttk.Label(frame, text = "Chemistry:", padding = "0 0 30 0")
chemistryLabel.grid(column = 1, row = 3, sticky = (W, E))
chemistryEntry = ttk.Entry(frame, width = 15, textvariable = chemistry)
chemistryEntry.grid(column = 2, row = 3, sticky = (W, E))

biologyLabel = ttk.Label(frame, text = "Biology:", padding = "0 0 30 0")
biologyLabel.grid(column = 1, row = 4, sticky = (W, E))
biologyEntry = ttk.Entry(frame, width = 15, textvariable = biology)
biologyEntry.grid(column = 2, row = 4, sticky = (W, E))

artsLabel = ttk.Label(frame, text = "Arts:", padding = "0 0 30 0")
artsLabel.grid(column = 1, row = 5, sticky = (W, E))
artsEntry = ttk.Entry(frame, width = 15, textvariable = arts)
artsEntry.grid(column = 2, row = 5, sticky = (W, E))

booksLabel = ttk.Label(frame, text = "Books")
booksLabel.grid(column = 3, row = 1, sticky = (W, E))
booksLabel = ttk.Label(frame, text = "Books")
booksLabel.grid(column = 3, row = 2, sticky = (W, E))
booksLabel = ttk.Label(frame, text = "Books")
booksLabel.grid(column = 3, row = 3, sticky = (W, E))
booksLabel = ttk.Label(frame, text = "Books")
booksLabel.grid(column = 3, row = 4, sticky = (W, E))
booksLabel = ttk.Label(frame, text = "Books")
booksLabel.grid(column = 3, row = 5, sticky = (W, E))

#Creates the buttons
totalButton = ttk.Button(frame, text = "Calculate Total", command = takeInput)
totalButton.grid(column = 1, row = 6, sticky = (W, E))
totalLabel = ttk.Label(frame, text = "Total: ")
totalLabel.grid(column = 1, row = 7, sticky = (W))
totAmountLabel = ttk.Label(frame, textvariable = total)
totAmountLabel.grid(column = 1, row = 7, sticky = (E))

averageButton = ttk.Button(frame, text = "Calculate Average", command = takeAverage)
averageButton.grid(column = 2, row = 6, sticky = (W, E))
averageLabel = ttk.Label(frame, text = "Average: ")
averageLabel.grid(column = 2, row = 7, sticky = (W))
aveAmountLabel = ttk.Label(frame, textvariable = average)
aveAmountLabel.grid(column = 2, row = 7, sticky = (E))


root.mainloop() #without this line of command, the window will disappear