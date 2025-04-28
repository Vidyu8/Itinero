from tkinter import ttk
def apply_styles(root):
    style = ttk.Style()
    style.configure("TFrame", background="#F0F8FF")
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("TLabel", font=("Arial", 12))
    root.configure(bg="#F0F8FF")
