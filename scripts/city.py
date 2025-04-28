from tkinter import ttk
from database import Database

class CityManager:
    def __init__(self):
        self.db = Database()

    def create_city_page(self, parent):
        frame = ttk.Frame(parent)
        ttk.Label(frame, text="Select a City", font=("Garamond", 16, "bold")).pack(pady=10)
        
        city_var = ttk.Combobox(frame, values=self.db.get_cities(), state="readonly")
        city_var.pack()
        places_list = ttk.Label(frame, text="")
        places_list.pack()
        
        def update_places(event):
            places = self.db.get_places(city_var.get())
            places_list.config(text="\n".join(places))
        
        city_var.bind("<<ComboboxSelected>>", update_places)
        return frame
