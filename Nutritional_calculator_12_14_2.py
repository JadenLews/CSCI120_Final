import tkinter as tk
from Nutri_info_Python_class import Nutri_info 

class Main():

    def __init__(self) -> None: 
        self.root = tk.Tk() 
        self.root.geometry("600x600") 
        self.root.title("Nutritional Calculator") 
        label = tk.Label(self.root, text = "My first nutritional calculator", font = ('Times New Roman', 16)) 
        label.pack(padx = 40, pady = 40)
        button_frame = tk.Frame(self.root) 
        button_frame.columnconfigure(0, weight = 1) 
        button_frame.columnconfigure(1, weight = 1) 
        button_frame.columnconfigure(2, weight = 1) 

        bttn_1 = tk.Button(button_frame, text = "Height", font = ('Times New Roman', 16)) 
        bttn_1.grid(row = 5, column = 3, sticky = tk.W + tk.E) 

        bttn_1_a = tk.Button(self.root, text = "I close the Height button", command = self.New_window)  
        bttn_1_a.place(x = 0, y = 105)

        bttn_2 = tk.Button(button_frame, text = "Weight", font = ('Times New Roman', 16))
        bttn_2.grid(row = 7, column = 3, sticky = tk.W + tk.E) 

        bttn_2_a = tk.Button(self.root, text = "I close the Weight button", command = self.New_window) 
        bttn_2_a.place(x = 0, y = 135)

        bttn_3 = tk.Button(button_frame, text = "Waist Circumference", font = ('Times New Roman', 16))
        bttn_3.grid(row = 9, column = 3, sticky = tk.W + tk.E)

        bttn_3_a = tk.Button(self.root, text = "I close the Waist Circumference button", command = self.New_window)
        bttn_3_a.place(x = 0, y = 166)

        button_frame.pack(fill = 'x') 

        fourth_bttn = tk.Button(self.root, text = "Age", font = ('Times New Roman', 16))
        fourth_bttn.place(x = 428, y = 194, height = 30, width = 172)

        fourth_bttn_a = tk.Button(self.root, text = "I close the Age button", command = self.New_window)
        fourth_bttn_a.place(x = 0, y = 195)

        self.root.mainloop() 

    def get_values(self):
        age = int(self.age_input.get()) 
        height = float(self.height_input.get())
        wc = float(self.wc_input.get()) 
        weight = float(self.weight_input.get()) 

        person = Nutri_info(height, weight, age, wc) 
        output_text = ''
        output_text += str(person.BMI()) + ' ' + '(BMI)' + ' \n' 
        output_text += str(person.skeletal_muscle_mass()) + ' ' + '(Skeletal Muscle Mass)' + '\n' 
        output_text += str(person.body_adiposity_index()) + ' ' + '(Body Adiposity Index)' + ' \n' 
        output_text += str(person.age_method()) + ' ' + '(Age Method result)' + ' \n' 

        self.output_box.config(text = output_text) 

    def New_window(self):
        self.root.destroy() 
        self.root.frame = tk.Tk() 
        self.root.frame.geometry("600x600")
        input_frame = tk.Frame(self.root.frame) 
        input_frame.grid(row=0, column=0, sticky="wn")
    
        age_txt = tk.Label(input_frame ,text = "Age").grid(row = 0,column = 0, sticky='w') 
        height_txt = tk.Label(input_frame ,text = "Height (in meters)").grid(row = 1,column = 0, sticky='w') 
        wc_txt = tk.Label(input_frame ,text = "Waist Circumference (in centimeters)").grid(row = 2,column = 0, sticky='w') 
        weight_txt = tk.Label(input_frame, text = "Weight (in kilograms)").grid(row = 3, column = 0, sticky = 'w') 

        self.age_input = tk.Entry(input_frame) 
        self.age_input.grid(row = 0, column = 1, sticky='w') 

        self.height_input = tk.Entry(input_frame) 
        self.height_input.grid(row = 1, column = 1, sticky='w')

        self.wc_input = tk.Entry(input_frame) 
        self.wc_input.grid(row = 2, column = 1, sticky='w')

        self.weight_input = tk.Entry(input_frame) 
        self.weight_input.grid(row = 3, column = 1, sticky='w')
        
        # Submit button
        btn_submit = tk.Button(input_frame, text="Submit", command = self.get_values).grid(row = 4, column = 0, sticky='nw') 
        
        self.output_box = tk.Label(input_frame, height=5, width=30, bg="WHITE") 
        self.output_box.grid(row = 5, column = 0, pady=5, sticky='se') 

new_app = Main() 
