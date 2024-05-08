"""
https://www.reddit.com/r/learnpython/comments/8cwmjm/comment/dxirh6d
"""

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Feet to Meters")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding=4)
mainframe.columnconfigure(2, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.grid(column=0, row=0, sticky="nsew")

feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky="nsew")

# feet_entry.focus()

root.mainloop()
