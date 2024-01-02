import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
# from G_maps_client import GoogleMapsClient

def open_link(url):
    webbrowser.open_new(url)

class PT_interface:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KWCC Prospecting Tool")
        self.root.configure(bg='white')
        self.root.geometry("1000x520")
        self.root.anchor("n")


        self.Title = tk.Label(self.root, text="Bar Prospecting Tool", font=('Arial', 28), background='white')
        self.Title.grid(row=0, column=1, columnspan=3, padx=10, pady=0)
        
        # Logo
        self.logo = Image.open("KWCC_Logo.png")
        resized_logo = self.logo.resize((185, 185), Image.LANCZOS)  # Resize the image
        self.photo = ImageTk.PhotoImage(resized_logo)
        self.image_label = tk.Label(self.root, image=self.photo, bg='white')
        self.image_label.grid(row=0, column=0,padx=10, pady=0)

        # Clickable text link for instructions
        self.instructions_link = tk.Label(self.root, text="How to?", fg="maroon", cursor="hand2", bg='white')
        self.instructions_link.grid(row=5,rowspan=3, column=3, padx=10, pady=0)
        self.instructions_link.bind("<Button-1>", self.show_instructions)

        # API key field
        self.API_label = tk.Label(self.root, text="Google API Key", font=('Arial', 12), bg='white')
        self.API_label.grid(row=1, column=0, padx=4, pady=10)
        self.API_KEY_FIELD = tk.Entry(self.root, width=80, font=('Arial', 12), bg='white')
        self.API_KEY_FIELD.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Lat/long field
        self.coordinates_label = tk.Label(self.root, text= "Query Point Coordinates (Latitude / Longitude)", font=('Arial', 12), bg='white')
        self.coordinates_label.grid(row=2, column=0, padx=4, pady=10)
        self.Lat_FIELD = tk.Entry(self.root, width=35, font=('Arial', 12))
        self.Lat_FIELD.grid(row=2, column=1, padx=0, pady=10)
        self.Slash = tk.Label(self.root, text= "/", font=('Arial', 12), bg='white')
        self.Slash.grid(row=2, column=2, padx=0, pady=10)
        self.Long_FIELD = tk.Entry(self.root, width=35, font=('Arial', 12))
        self.Long_FIELD.grid(row=2, column=3, padx=0, pady=10)
        
        # Radius field
        self.radius_label = tk.Label(self.root, text= "Radius (in kilometers) ", font=('Arial', 12), bg='white')
        self.radius_label.grid(row=3, column=0, padx=4, pady=4)
        self.radius_FIELD = tk.Entry(self.root, width=80, font=('Arial', 12))
        self.radius_FIELD.grid(row=3, column=1, columnspan=3, padx=0, pady=10)

        # Excel file name
        self.xslx_name_label = tk.Label(self.root, text= "List Name (.XLSX File Name)", font=('Arial', 12), bg='white')
        self.xslx_name_label.grid(row=4, column=0, padx=4, pady=4)
        self.xslx_name_FIELD = tk.Entry(self.root, width=80, font=('Arial', 12))
        self.xslx_name_FIELD.grid(row=4, column=1, columnspan=3, padx=0, pady=10)

        # Generate Button
        self.generate_button = tk.Button(self.root, text="Generate", font=('Arial', 30), command= self.Generate_Prospect_List, activeforeground="maroon")
        self.generate_button.grid(row=5, rowspan=4, column=1, columnspan=3, padx=10, pady=10)

        # Developed by J. Romero link
        self.link_label = tk.Label(self.root, text="Devleoped by J. Romero",font=('Arial', 10), fg="maroon", cursor="hand2", bg='white')
        self.link_label.grid(row=6, column=0, padx=0, pady=0)
        self.link_label.bind("<Button-1>", lambda e: open_link("https://github.com/JRomeroRepositories"))

        self.license = tk.Label(self.root, text="View License", fg="maroon", font=('Arial', 10), cursor="hand2", bg='white')
        self.license.grid(row=7, column=0, padx=0, pady=0)
        self.license.bind("<Button-1>", self.show_license)

        self.root.mainloop()

    def Generate_Prospect_List(self):
     API_KEY = self.API_KEY_FIELD.get()
     LAT = self.Lat_FIELD.get()
     LONG = self.Long_FIELD.get()
     RADIUS = self.radius_FIELD.get()
     FILE_NAME = self.xslx_name_FIELD.get()
     print(API_KEY, LAT, LONG, RADIUS, FILE_NAME)

    def show_instructions(self, event=None):
        # New window for displaying instructions
        instruction_window = tk.Toplevel()
        instruction_window.title("Instructions")

        # Instructional text
        instructions = "Here are the instructions for using this application. \n\n[Include detailed instructions here.]"

        # Label for displaying the instructions
        instruction_label = tk.Label(instruction_window, text=instructions, justify=tk.LEFT)
        instruction_label.pack(padx=10, pady=10)

    def show_license(self, event=None):
        # New window for displaying the license
        license_window = tk.Toplevel()
        license_window.title("MIT License")

        # License text
        license_text = """MIT License

Copyright (c) 2024 Jose Carlos Romero

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

        # Text widget for displaying the license
        text_widget = tk.Text(license_window, wrap="word", height=30, width=60)
        text_widget.pack(padx=10, pady=10)
        text_widget.insert("1.0", license_text)
        text_widget.config(state="disabled")  # Make the text widget read-only
        

PT_interface()