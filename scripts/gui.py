import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from auth import AuthManager
from city import CityManager
from styles import apply_styles

class TravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Explorer")
        self.root.geometry("700x500")
        apply_styles(self.root)

        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.auth_manager = AuthManager()
        self.city_manager = CityManager()

        self.pages = {}
        self.create_home_page()
        self.show_page("Home")

    def create_home_page(self):
        home_page = ttk.Frame(self.container)
        label = ttk.Label(home_page, text="Welcome to Travel Explorer", font=("Garamond", 18, "bold"))
        label.pack(pady=20)

        register_button = ttk.Button(home_page, text="Register", command=self.show_registration_page)
        login_button = ttk.Button(home_page, text="Login", command=self.show_login_page)
        register_button.pack(pady=10)
        login_button.pack(pady=10)

        self.pages["Home"] = home_page

    def show_registration_page(self):
        self.pages["Registration"] = self.auth_manager.create_registration_page(self.container, self.show_page)
        self.show_page("Registration")

    def show_login_page(self):
        self.pages["Login"] = self.auth_manager.create_login_page(self.container, self.show_page, self.show_city_page)
        self.show_page("Login")

    def show_city_page(self):
        self.pages["Cities"] = self.city_manager.create_city_page(self.container)
        self.show_page("Cities")

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)
