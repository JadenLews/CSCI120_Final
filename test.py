import tkinter as tk
import csv
from tkinter import messagebox
class profile:
    def __init__(self,dict=None):

        self.root2 = tk.Tk()
        self.root2.geometry('800x500')
        self.label = tk.Label(self.root2, text= 'Profile Creator', font=('Arial', 15))
        self.label.pack(padx=10, pady=10)


        self.name = 'Not defined'
        self.age = 'Not defined'
        self.height = 'Not defined'
        self.w_circ = 'Not defined'
        self.weight = 'Not defined'


        self.agel = tk.Label(self.root2, text= (f'Your age is: {self.age}'), font=('Arial', 12))
        self.agel.place(x=30, y=20)

        self.w_circl = tk.Label(self.root2, text= (f'Your waist circumference is: {self.w_circ}'), font=('Arial', 12))
        self.w_circl.place(x=30, y=50)

        self.heightl = tk.Label(self.root2, text= (f'Your height is: {self.height}'), font=('Arial', 12))
        self.heightl.place(x=30, y=80)

        self.weightl = tk.Label(self.root2, text= (f'Your weight is: {self.weight}'), font=('Arial', 12))
        self.weightl.place(x=30, y=110)

        self.namel = tk.Label(self.root2, text= (f'Your name is: {self.name}'), font=('Arial', 12))
        self.namel.place(x=30, y=140)

#
        self.agelabel = tk.Label(self.root2, text= ('name'), font=('Arial', 9))
        self.agelabel.place(x=145, y=230)

        self.w_circlabel = tk.Label(self.root2, text= ('waist circumference(inch)'), font=('Arial', 9))
        self.w_circlabel.place(x=205, y=230)

        self.heightlabel = tk.Label(self.root2, text= ('height(inch)'), font=('Arial', 9))
        self.heightlabel.place(x=360, y=230)

        self.weightlabel = tk.Label(self.root2, text= ('weight'), font=('Arial', 9))
        self.weightlabel.place(x=495, y=230)

        self.namelabel = tk.Label(self.root2, text= ('age'), font=('Arial', 9))
        self.namelabel.place(x=620, y=230)


        self.button = tk.Button(self.root2, text= 'Update Information', font=('Arial', 10), command= self.profileupdate)
        self.button.place(x=350, y=300, height=60, width= 120)


        self.ptextentry5n = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry5n.place(x=120, y=200, height=30, width= 80)

        self.ptextentry2w_ = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry2w_.place(x=240, y=200, height=30, width= 80)

        self.ptextentry3h = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry3h.place(x=360, y=200, height=30, width= 80)

        self.ptextentry4w = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry4w.place(x=480, y=200, height=30, width= 80)

        self.ptextentryage = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentryage.place(x=600, y=200, height=30, width= 80)
        self.ptextentry2w_.get('1.0', tk.END)
        
        self.root2.mainloop()
    def profileupdate(self):
        self.name = self.ptextentry5n.get('1.0', tk.END)
        self.age = self.ptextentryage.get('1.0', tk.END)
        self.w_circ = self.ptextentry2w_.get('1.0', tk.END)
        self.height = self.ptextentry3h.get('1.0', tk.END)
        self.weight = self.ptextentry4w.get('1.0', tk.END)
        self.namel.config(text=(f'Your name is: {self.name}'), font=('Arial', 12))
        self.w_circl.config(text=(f'Your waist circumference is: {self.w_circ}'), font=('Arial', 12))
        self.heightl.config(text=(f'Your height is: {self.height}'), font=('Arial', 12))
        self.agel.config(text=(f'Your age is: {self.age}'), font=('Arial', 12))
        self.weightl.config(text=(f'Your weight is: {self.weight}'), font=('Arial', 12))
        self.toCsv()


    def toCsv(self):
        name = self.name.lower().strip()
        filename = f'{name}.csv'
        with open(filename, mode='w') as profile_file:
            profile_writer = csv.writer(profile_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #Format: row is data name followed by data
            profile_writer.writerow(['age', self.age.strip()])
            #in inches
            #Format: row is data name followed by data        
            #in cm
            profile_writer.writerow(['w_circ', self.w_circ.strip()])
            #in cm, converted to meters in fromCsv
            profile_writer.writerow(['height', self.height.strip()])
            #in lbs
            #in kg
            profile_writer.writerow(['weight', self.weight.strip()])
blah = profile()