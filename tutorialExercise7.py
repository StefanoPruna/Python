from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Chatter")
content = ttk.Frame(root, padding = (3, 1, 15, 15))
frame = ttk.Frame(content, borderwidth = 5, relief = "groove", width = 200, height = 80)

output = Text(content)

testoLabel = ttk.Label(content, text = "gary: did you see the latest?\nhelen: Not yet - what's it about")
testoLabel["justify"] = "left"

scrollbar = ttk.Scrollbar(content, orient = VERTICAL, command = output.yview)
output["yscrollcommand"] = scrollbar.set

subTestoLabel = ttk.Label(content, text = "bob:")

subTestoLabel["justify"] = "center"

variable2 = StringVar()
variable2.set("It'd basically be making maths")
bobTextEntry = ttk.Entry(content, textvariable = variable2)
bobTextEntry["state"] = "readonly"

sendButton = ttk.Button(content, text = "Send")

names = ("alice", "bob", "charlie", "dianne", "ethan")
variable = StringVar(value = names)
listbox = Listbox(content, listvariable = variable)
listbox["selectmode"] = "extended" #User can selct multiple items, with browse, can be selected only one item
listbox["justify"] = "left"

content.grid(sticky = (N, S, W, E))
frame.grid(column = 0, row = 0, columnspan = 3, rowspan = 2)
testoLabel.grid(column = 1, row = 1, columnspan = 2, sticky = (N, S, W, E))
subTestoLabel.grid(column = 1, row = 2, sticky = E)
scrollbar.grid(column = 3, row = 1, sticky = (N, S))
sendButton.grid(column = 4, row = 2, columnspan = 2, sticky = W, pady = 10)
listbox.grid(column = 4, row = 1, sticky = (N, S))
bobTextEntry.grid(column = 2, row = 2, sticky = W)

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

content.columnconfigure(1, weight = 1)
content.columnconfigure(2, weight = 5)
content.columnconfigure(3, weight = 1)
content.columnconfigure(4, weight = 3)
content.rowconfigure(2, weight = 5)

for child in frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)


root.mainloop()