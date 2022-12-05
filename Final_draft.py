import tkinter as tk
from tkinter import messagebox
class MYGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.profile = 'Unknown'
        self.root.geometry('800x500')
        self.label = tk.Label(self.root, text= 'Landing Page', font=('Arial', 15))
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text= 'Jaden', font=('Arial', 10))
        self.button.place(x=5, y=10, height=60, width= 120)

        self.button2 = tk.Button(self.root, text= 'Roan', font=('Arial', 10))
        self.button2.place(x=5, y=80, height=60, width= 120)

        self.button3 = tk.Button(self.root, text= 'Keith', font=('Arial', 10))
        self.button3.place(x=5, y=150, height=60, width= 120)

        self.root.mainloop()

meeee = MYGUI()