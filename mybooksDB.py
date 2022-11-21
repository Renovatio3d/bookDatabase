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
# position first row to the left for the above label
title__label.grid(row=0, column=0, sticky=W)
# Book Title string des, string or char
title__text = StringVar()
# title__entry-store entry user input, text variable stores enter value
title__entry = ttk.Entry(window, width=20, textvariable=title__text)
# Same label different column
title__entry.grid(row=0, column=1, sticky=W)

# author
author__label = ttk.Label(window, text='Author', background='light blue', font=('TkDefaultFont', 12))
author__label.grid(row=0, column=2, sticky=W)
author__text = StringVar()
author__entry = ttk.Entry(window, width=20, textvariable=title__text)
author__entry.grid(row=0, column=3, sticky=W)

# ISBN
isbn__label = ttk.Label(window, text='ISBN', background='light blue', font=('TkDefaultFont', 12))
isbn__label.grid(row=0, column=4, sticky=W)
isbn__text = StringVar()
isbn__entry = ttk.Entry(window, width=20, textvariable=title__text)
isbn__entry.grid(row=0, column=5, sticky=W)

window.mainloop()  # Runs the app
