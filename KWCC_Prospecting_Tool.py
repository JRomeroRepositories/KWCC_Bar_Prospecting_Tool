# import time
# import googlemaps # pip install googlemaps
# import pandas as pd # pip install pandas
# import re

 # GUI import
import tkinter as tk


class ProspectingTool:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.root.mainloop()

ProspectingTool()