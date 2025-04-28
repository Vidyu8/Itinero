from tkinter import ttk, messagebox
from database import Database

class AuthManager:
    def __init__(self):
        self.db = Database()

    def create_registration_page(self, parent, show_page_callback):
        frame = ttk.Frame(parent)
        ttk.Label(frame, text="User Registration", font=("Garamond", 16, "bold")).pack(pady=10)
        
        username_entry = ttk.Entry(frame)
        password_entry = ttk.Entry(frame, show="*")
        ttk.Label(frame, text="Username:").pack()
        username_entry.pack()
        ttk.Label(frame, text="Password:").pack()
        password_entry.pack()
        
        def register():
            if self.db.add_user(username_entry.get(), password_entry.get()):
                messagebox.showinfo("Success", "Registration successful!")
                show_page_callback("Home")
            else:
                messagebox.showerror("Error", "User already exists.")
        
        ttk.Button(frame, text="Register", command=register).pack(pady=10)
        return frame

    def create_login_page(self, parent, show_page_callback, show_city_callback):
        frame = ttk.Frame(parent)
        ttk.Label(frame, text="User Login", font=("Garamond", 16, "bold")).pack(pady=10)
        
        username_entry = ttk.Entry(frame)
        password_entry = ttk.Entry(frame, show="*")
        ttk.Label(frame, text="Username:").pack()
        username_entry.pack()
        ttk.Label(frame, text="Password:").pack()
        password_entry.pack()
        
        def login():
            if self.db.authenticate_user(username_entry.get(), password_entry.get()):
                messagebox.showinfo("Success", "Login successful!")
                show_city_callback()
            else:
                messagebox.showerror("Error", "Invalid credentials.")
        
        ttk.Button(frame, text="Login", command=login).pack(pady=10)
        return frame

