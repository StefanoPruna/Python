from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#filename = filedialog.askopenfilename()
#filename = filedialog.askdirectory()
from tkinter import messagebox
#messagebox.askyesno(message = "Are you ok?", icon = "question", title = "Question")

def clickButton(*args):
    print("Button clicked")

def notify(event):
    print("New selection: {0}".format(listbox.curselection()))

root = Tk()
frame = ttk.Frame(root, width = 800, height = 600, padding = 5)
frame.grid()
frame.configure(borderwidth = 5)
frame["relief"] = "groove"

label = ttk.Label(frame, text = "Test")
label.grid()
#label["text"] = "Ciao" to change the text in the label

variable = StringVar()
variable.set("Ciao")
label["textvariable"] = variable
variable.set(variable.get() + " \nThis is a new line")
label["justify"] = "center"

image = PhotoImage(file = "")
#imagelabel["image"] = image
label["compound"] = "bottom" #it can be "right", "left", "center"...

button = ttk.Button(frame, text = "Ok", command = clickButton)
button.grid()
selected = StringVar()
checkbutton = ttk.Checkbutton(frame, text = "Click me", onvalue = "selected", offvalue = "not selected", variable = selected)
checkbutton.grid(row = 8)
#checkbutton.grid_remove()

firstRadio = ttk.Radiobutton(frame, variable = selected, text = "First", value = "first")
secondRadio = ttk.Radiobutton(frame, variable = selected, text = "Second", value = "second")
thirdRadio = ttk.Radiobutton(frame, variable = selected, text = "Third", value = "third")
firstRadio.grid(row = 2)
secondRadio.grid(row = 3)
thirdRadio.grid(row = 4)

variable4 = StringVar()
variable4.set("Ciao!What's your name?:")
questionEntry = ttk.Entry(frame, width = 40, textvariable = variable4)
questionEntry.grid(row = 5)
questionEntry["state"] = "!readonly"
#entry["show"] = "*" it won't show what we type, used for password

variable2 = StringVar()
variable2.set("What position are you?")
combobox = ttk.Combobox(frame, textvariable = variable2)
combobox["values"] = ("First", "Second", "Third")
combobox.grid(row = 6)

choices = ("First", "Second", "Third")
variable3 = StringVar(value = choices)
listbox = Listbox(frame, listvariable = variable3)
listbox.grid(column = 2, row = 1)
listbox["selectmode"] = "extended" #User can selct multiple items, with browse, can be selected only one item
listbox["justify"] = "center"

scrollbar = ttk.Scrollbar(frame, orient = VERTICAL, command = listbox.yview)
listbox["yscrollcommand"] = scrollbar.set
scrollbar.grid(column = 3, row = 1, sticky = (N, S))

for child in frame.winfo_children():
    child.grid_configure(padx = 15, pady = 10)

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
frame.columnconfigure(0, weight = 1)
frame.rowconfigure(2, weight = 3)

root.mainloop()