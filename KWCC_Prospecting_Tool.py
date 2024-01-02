# import time
# import googlemaps # pip install googlemaps
# import pandas as pd # pip install pandas
# import re

 # GUI import
import tkinter as tk


<<<<<<< HEAD
class ProspectingTool:
=======
## Google API Key is unique to all google API platform users, and is used in
##  reference to the GCP account and billing
API_KEY = 'API KEY INSERT HERE'
map_client = googlemaps.Client(API_KEY)
>>>>>>> 3b870166f56d49faeafcf222164f89e0f29c89a3

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.root.mainloop()

ProspectingTool()