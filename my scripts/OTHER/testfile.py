import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class RadioButtons(ttk.Frame):
    def __init__(self, master, radio_var):
        super().__init__(master)
        
        self.radio_var = radio_var
        
        self.create_widgets()

    def create_widgets(self):
        self.radio_var.set("Option 1")
        
        self.radio_button1 = ttk.Radiobutton(self, text="Option 1", value="Option 1", variable=self.radio_var)
        self.radio_button1.pack(side="left")
        
        self.radio_button2 = ttk.Radiobutton(self, text="Option 2", value="Option 2", variable=self.radio_var)
        self.radio_button2.pack(side="left")
        
        self.radio_button3 = ttk.Radiobutton(self, text="Option 3", value="Option 3", variable=self.radio_var)
        self.radio_button3.pack(side="left")

class ImageLabel(ttk.Frame):
    def __init__(self, master, image_path):
        super().__init__(master)
        
        self.create_widgets(image_path)

    def create_widgets(self, image_path):
        self.image = Image.open(image_path).resize((100, 100))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = ttk.Label(self, image=self.image)
        self.image_label.pack()

class CheckBoxes(ttk.Frame):
    def __init__(self, master, check_var1, check_var2, check_var3):
        super().__init__(master)
        
        self.check_var1 = check_var1
        self.check_var2 = check_var2
        self.check_var3 = check_var3
        
        self.create_widgets()

    def create_widgets(self):
        self.check1 = ttk.Checkbutton(self, text="Option 1", variable=self.check_var1)
        self.check1.pack(side="left")
        
        self.check2 = ttk.Checkbutton(self, text="Option 2", variable=self.check_var2)
        self.check2.pack(side="left")
        
        self.check3 = ttk.Checkbutton(self, text="Option 3", variable=self.check_var3)
        self.check3.pack(side="left")

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("CustomTkinter Example")
        self.master.geometry("500x400")
        
        self.radio_var = tk.StringVar()
        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()
        self.check_var3 = tk.IntVar()
        
        self.create_widgets()

    def create_widgets(self):
        self.radio_buttons = RadioButtons(self.master, self.radio_var)
        self.radio_buttons.pack(pady=10)
        
        self.image_label = ImageLabel(self.master, "logo.jpeg")
        self.image_label.pack(pady=10)
        
        self.check_boxes = CheckBoxes(self.master, self.check_var1, self.check_var2, self.check_var3)
        self.check_boxes.pack(pady=10)

app = App()
app.mainloop()