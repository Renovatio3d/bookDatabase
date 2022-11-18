# Tk,Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
# Tk-app window, Button-ButtonElement,Label-LabelElement,Scrollbar-EnableScroll,Listbox-Listbox,
# StringVar-Type of data store input string, Entry-Creating entry widget and position W,E,N,S,End-end of things
from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
# Modules Themed Library
from tkinter import ttk
# Display message
from tkinter import messagebox

window = Tk()  # Application window interface
# GUI frontEnd
# Title, BG-Color, Size-restriction in app window
window.title('My Books Database App')
window.configure(background='light blue')
window.geometry('960x540')
window.resizable(width=False, height=False)

# variable title__label Stores label with parameters from ttk
title__label = ttk.Label(window, text='Title', background='light blue', font=('TkDefaultFont', 12))
# position first row to the left
title__label.grid(row=0, column=0, sticky=W)
# Book Title string des
title__text = StringVar()
# title__entry-store entry for storing
title__entry = ttk.Entry(window, width=24, textvariable=title__text)
title__entry.grid(row=0, column=1, sticky=W)

window.mainloop()  # Runs the app
