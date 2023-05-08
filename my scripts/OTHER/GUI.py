import tkinter as tk
from tkinter import ttk


class CustomUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title
        self.title("Custom UI")

        # Set window size and position
        self.geometry("500x300+200+200")

        # Create header label
        header_label = ttk.Label(self, text="FEDERALE POLITIE")
        header_label.config(font=("Courier", 20))
        header_label.place(x=50, y=20)

        # # Create image label
        # img = tk.PhotoImage(file="path/to/image.png")
        # img_label = ttk.Label(self, image=img)
        # img_label.image = img  # To prevent garbage collection of the image object
        # img_label.place(x=10, y=10)

        # Create checkboxes
        self.option1_var = tk.BooleanVar()
        self.option2_var = tk.BooleanVar()
        self.option3_var = tk.BooleanVar()

        option1_checkbox = ttk.Checkbutton(
            self, text="Option 1", variable=self.option1_var, onvalue=True, offvalue=False, class_="RADIO")
        option1_checkbox.place(x=50, y=80)

        option2_checkbox = ttk.Checkbutton(
            self, text="Option 2", variable=self.option2_var, onvalue=True, offvalue=False, class_="RADIO")
        option2_checkbox.place(x=50, y=110)

        option3_checkbox = ttk.Checkbutton(
            self, text="Option 3", variable=self.option3_var, onvalue=True, offvalue=False, class_="RADIO")
        option3_checkbox.place(x=50, y=140)

        # Create input fields
        api_id_label = ttk.Label(self, text="API ID:")
        api_id_label.place(x=50, y=180)

        self.api_id_entry = ttk.Entry(self, width=20)
        self.api_id_entry.place(x=100, y=180)

        api_hash_label = ttk.Label(self, text="API Hash:")
        api_hash_label.place(x=220, y=180)

        self.api_hash_entry = ttk.Entry(self, width=20)
        self.api_hash_entry.place(x=290, y=180)

        # Create submit button
        submit_button = ttk.Button(self, text="Submit", command=self.submit)
        submit_button.place(x=220, y=220)

        # Create output field
        self.output_field = tk.Text(self, height=5, width=50)
        self.output_field.place(x=50, y=260)

    def submit(self):
        # Get the selected checkbox values
        option1_value = self.option1_var.get()
        option2_value = self.option2_var.get()
        option3_value = self.option3_var.get()

        # Get the API ID and API hash values
        api_id = self.api_id_entry.get()
        api_hash = self.api_hash_entry.get()

        self.output_field.insert(
            tk.END, f"Option 1 selected: {option1_value}\n")
        self.output_field.insert(
            tk.END, f"Option 2 selected: {option2_value}\n")
        self.output_field.insert(
            tk.END, f"Option 3 selected: {option3_value}\n")

        # You can also output the API ID and API hash values if needed
        self.output_field.insert(tk.END, f"API ID: {api_id}\n")
        self.output_field.insert(tk.END, f"API ID: {api_hash}\n")
        # self.output_field.insert(tk.END,


if __name__ == "__main__":
    app = CustomUI()
    app.mainloop()
