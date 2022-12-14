import tkinter as tk
from tkinter import ttk # module eases () the use of Tk-themed widget sets
from Nutri_info_Python_class import Nutri_info # IMPORT class from a module

class Main():

    def __init__(self) -> None: # once one has passed the value self to this constructor, it outputs Self@Main
        self.root = tk.Tk() # ESTABLISHES a new Toplevel Tk widget with a new Tcl interpreter 
        self.root.geometry("600x600") # DEFINES geometric dimensions
        self.root.title("Nutritional Calculator") # title
        label = tk.Label(self.root, text = "My first nutritional calculator", font = ('Times New Roman', 16)) # a label
        label.pack(padx = 40, pady = 40) #internal padding, with padx (in the direction of the x-axis) set as 40 and pady (in direction of the y-axis) also. 
        button_frame = tk.Frame(self.root) # creates a FRAME widget without clear borders or relief
        button_frame.columnconfigure(0, weight = 1) # configures column index at index 0, propogate additional space of 1 screen unit to this column
        button_frame.columnconfigure(1, weight = 1) # as above, but at index 1 
        button_frame.columnconfigure(2, weight = 1) # as above, but at index 2 

        bttn_1 = tk.Button(button_frame, text = "Height", font = ('Times New Roman', 16)) # with button_frame, a new FRAME (within a widget) is devised
        bttn_1.grid(row = 5, column = 1, sticky = tk.W + tk.E) #first button at row 0 column 0 

        bttn_1_a = tk.Button(self.root, text = "I close the Height button", command = self.New_window)  # same as below, command is applied to the master widget
        bttn_1_a.pack(padx = 10, pady = 10) # button to deactivate (terminate) current widget

        bttn_2 = tk.Button(button_frame, text = "Weight", font = ('Times New Roman', 16))
        bttn_2.grid(row = 7, column = 1, sticky = tk.W + tk.E) # same as bttn_1 

        bttn_2_a = tk.Button(self.root, text = "I close the Weight window", command = self.New_window) # invokes (conjures) the method New_window
        bttn_2_a.pack(padx = 10, pady = 10) #same as bttn_1_a

        bttn_3 = tk.Button(button_frame, text = "Waist Circumference", font = ('Times New Roman', 16))
        bttn_3.grid(row = 9, column = 1, sticky = tk.W + tk.E)

        bttn_3_a = tk.Button(self.root, text = "I close the Waist Circumference", command = self.New_window)
        bttn_3_a.pack(padx = 10, pady = 10)

        button_frame.pack(fill = 'x') 

        fourth_bttn = tk.Button(self.root, text = "Age", font = ('Times New Roman', 16))
        fourth_bttn.place(x = 142, y = 384, height = 30, width = 314)

        fourth_bttn_a = tk.Button(self.root, text = "I close the Age window", command = self.New_window)
        fourth_bttn_a.pack(padx = 10, pady = 10)

        self.root.mainloop() 

    def get_values(self):
        age = int(self.age_input.get()) # convert to an integer, the value after applying the get method to self.age_input
        height = float(self.height_input.get()) # as above, but convert to float
        wc = float(self.wc_input.get()) # as above
        weight = float(self.weight_input.get()) # as above

        person = Nutri_info(height, weight, age, wc) # instantiate an instance of a class 
        output_text = ''
        output_text += str(person.BMI()) + ' ' + '(BMI)' + ' \n' # convert an instance of a given method to a string and annex both an empty string and a newline to it
        output_text += str(person.skeletal_muscle_mass()) + ' ' + '(Skeletal Muscle Mass)' + '\n' # as above
        output_text += str(person.body_adiposity_index()) + ' ' + '(Body Adiposity Index)' + ' \n' # as above 
        output_text += str(person.age_method()) + ' ' + '(Age Method result)' + ' \n' # as above

        self.output_box.config(text = output_text) # configure resources for the widget output_box defined below

    def New_window(self):
        self.root.destroy() # destroy previous widget (beget) its termination 
        self.root.frame = tk.Tk() # new widget 
        self.root.frame.geometry("600x600")
        input_frame = tk.Frame(self.root.frame) # new frame within widget 
        input_frame.grid(row=0, column=0, sticky="wn") # position of frame in a grid
    
        age_txt = tk.Label(input_frame ,text = "Age").grid(row = 0,column = 0, sticky='w') # text labels, pass the new frame as a parameter and MOVE to the position of label
        height_txt = tk.Label(input_frame ,text = "Height").grid(row = 1,column = 0, sticky='w') # as above
        wc_txt = tk.Label(input_frame ,text = "wc").grid(row = 2,column = 0, sticky='w') # as above
        weight_txt = tk.Label(input_frame, text = "weight").grid(row = 3, column = 0, sticky = 'w') # as above

        self.age_input = tk.Entry(input_frame) # entry widget for age_input
        self.age_input.grid(row = 0, column = 1, sticky='w') # position in a grid 

        self.height_input = tk.Entry(input_frame) # as above 
        self.height_input.grid(row = 1, column = 1, sticky='w')

        self.wc_input = tk.Entry(input_frame) # as above
        self.wc_input.grid(row = 2, column = 1, sticky='w')

        self.weight_input = tk.Entry(input_frame) # as above
        self.weight_input.grid(row = 3, column = 1, sticky='w')
        
        # Submit button
        btn_submit = tk.Button(input_frame, text="Submit", command = self.get_values).grid(row = 4, column = 0, sticky='nw') # first creates a button containing the command "get values" then places it in a grid
        
        self.output_box = tk.Label(input_frame, height=5, width=30, bg="WHITE") # label for the output box and set dimensions
        self.output_box.grid(row = 5, column = 0, pady=5, sticky='se') # in a grid 

new_app = Main() # invoke (inaugurate) an instance of this class 
