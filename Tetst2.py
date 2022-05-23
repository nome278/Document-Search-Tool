from tkinter import *
from tkinter import filedialog
from openpyxl import workbook

ws = Tk() # Make window
#Format the window/add instructions
ws.title('Document Search Tool') # Make Title for window
frame= Frame(ws)
instruction = Label(text="Please first add the file you would like to search.")
instruction.pack()

#Define the open file and print it as a label on the window
def openfile():
    global filename
    #filetypes = ('excel', '*.xls', '*.csv')
    filename =filedialog.askopenfilename(title="Open File")

    pathlabel.config(text=filename)


def printfile():
    print(filename)
pathlabel=Label(ws)
pathlabel.pack()
filename=""
browsebtn= Button(text="Browse...", command = lambda:openfile())
browsebtn.pack(side = BOTTOM)

def on_entry_click(event):
    if entry.get() == 'Search...':
       entry.delete(0, "end")
       entry.insert(0, '')
       entry.config(fg = 'black')
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Search...')
        entry.config(fg = 'grey')

label = Label(ws, text="Search file for: ")
label.pack(side = 'left')
entry = Entry(ws, bd=1)
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(fg='grey')
entry.pack(side = 'left')

#inputtxt = Entry(ws)
#inputtxt.configure(wrap=None)
#inputtxt.pack()

def filesearch():
    inp = entry.get("1.0","end-1c")
    entry.pack()
    file = open(filename)
    readfile = file.read()
    if inp in readfile:
        print(inp, 'is found in File')
    else:
        print('Not Found')
searchbtn = Button(text = "Search", command = filesearch)
searchbtn.pack(side = BOTTOM)
ws.bind('<Return>',lambda event:filesearch())
ws.mainloop()
