# Implement a graphical user interface from the onlilibrary_list program
# Create the readme.md
# Check if it works in linux
# Submit them as a4.tgz
from tkinter import * #Import Graphical User Interfaces
from tkinter import ttk #ttk is the newer graphic/style
import os

#We collect all the data and with * we take any arguments
class OnlineLibrary(Frame):
    def __init__(self, computer, physics, chemistry, biology, arts):
        try:
            self.computer = float(computer.get())
            self.physics = float(physics.get())
            self.chemistry = float(chemistry.get())
            self.biology = float(biology.get())
            self.arts = float(arts.get())
        except (ValueError, TypeError): #Check if the input is not a number
            print("Number of books must be an integer")
        except AssertionError: #Check if the input is 0 or negative
            print("Number of books must be at least 1") 

    def totalCount(self, total):
        self.total = total.set(varComputer + varPhysics + varChemistry + varBiology + varArts)
    
    def averageCount(self, average):
        self.average = average.set((varComputer + varPhysics + varChemistry + varBiology + varArts) / 5)


#Creates a new window
root = Tk() 
root.title("Online Library GUI")
frame = ttk.Frame(root, padding = "3 3 12 12")
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame.columnconfigure(0, weight = 1)
frame.rowconfigure(0, weight = 1)

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
totalButton = ttk.Button(frame, text = "Calculate Total", command = totalCount)
totalButton.grid(column = 1, row = 6, sticky = (W, E))
totalLabel = ttk.Label(frame, text = "Total: ")
totalLabel.grid(column = 1, row = 7, sticky = (W))
totAmountLabel = ttk.Label(frame, textvariable = total)
totAmountLabel.grid(column = 1, row = 7, sticky = (E))

averageButton = ttk.Button(frame, text = "Calculate Average", command = self.averageCount)
averageButton.grid(column = 2, row = 6, sticky = (W, E))
averageLabel = ttk.Label(frame, text = "Average: ")
averageLabel.grid(column = 2, row = 7, sticky = (W))
aveAmountLabel = ttk.Label(frame, textvariable = average)
aveAmountLabel.grid(column = 2, row = 7, sticky = (E))

root.mainloop() #without this line of command, the window will disappear