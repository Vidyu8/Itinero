import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser

def explore_places():
    # Simulate loading popular destinations
    messagebox.showinfo("Explore", "Top destinations for solo travelers:\n\n1. Gokarna, Karnataka\n2. Varanasi, Uttar Pradesh\n3. Panjim, Goa\n4. Shillong, Assam\n5. Munnar, Canada")

def book_journey():
    # Simulate booking process
    response = messagebox.askyesno("Book Journey", "Would you like to search for flights and hotels?")
    if response:
        webbrowser.open("https://www.tripadvisor.com/")

def view_reviews():
    # Simulate showing reviews
    messagebox.showinfo("Travel Reviews", "Recent traveler reviews:\n\n\"Gokarna was amazing for solo travel!\" - Sarah ★★★★★\n\n\"Varanasi's temples are breathtaking\" - Mayithri ★★★★☆")

def show_travel_tips():
    messagebox.showinfo("Travel Tips", "Solo Travel Tips:\n\n1. Stay in hostels to meet people\n2. Learn basic local phrases\n3. Always have backup copies of documents\n4. Trust your instincts\n5. Pack light!")

def update_background(event=None):
    try:
        width = root.winfo_width()
        height = root.winfo_height()
        
        if width > 0 and height > 0:
            bg_image_resized = bg_image_original.resize((width, height), Image.Resampling.LANCZOS)
            bg_photo_resized = ImageTk.PhotoImage(bg_image_resized)
            
            canvas.itemconfig(background_image, image=bg_photo_resized)
            canvas.image = bg_photo_resized
    except:
        pass

# Main window
root = tk.Tk()
root.title("Itinero")
root.geometry("1000x700")
root.minsize(800, 600)
root.configure(bg="#f5f5f5")

# Try to load background image, use solid color if not found
try:
    bg_image_original = Image.open("background.jpeg")
    use_bg_image = True
except:
    use_bg_image = False
    bg_color = "#00aa6c"  

# Create main container
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(fill="both", expand=True)

if use_bg_image:
    canvas = tk.Canvas(main_frame, width=1000, height=700)
    canvas.pack(fill="both", expand=True)
    bg_image_resized = bg_image_original.resize((1000, 700), Image.Resampling.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(bg_image_resized)
    background_image = canvas.create_image(0, 0, anchor="nw", image=bg_photo_resized)
    root.bind("<Configure>", update_background)
    content_bg = "white"
else:
    canvas = tk.Canvas(main_frame, width=1000, height=700, bg=bg_color)
    canvas.pack(fill="both", expand=True)
    content_bg = "white"

header_frame = tk.Frame(canvas, bg="#003580", height=60)
header_frame.pack(fill="x", side="top")

logo_label = tk.Label(header_frame, text="Itinero", font=("Arial", 24, "bold"), 
                     fg="white", bg="#003580")
logo_label.pack(side="left", padx=20, pady=10)

nav_frame = tk.Frame(header_frame, bg="#003580")
nav_frame.pack(side="right", padx=20)

nav_buttons = ["Home", "Destinations", "Hotels", "Flights", "Things to Do"]
for btn_text in nav_buttons:
    btn = tk.Button(nav_frame, text=btn_text, font=("Arial", 10), 
                   bg="#003580", fg="white", bd=0, activebackground="#003580", 
                   activeforeground="white", relief="flat")
    btn.pack(side="left", padx=5)

# Search bar (TripAdvisor style)
search_frame = tk.Frame(canvas, bg="#f5f5f5", padx=20, pady=10)
search_frame.pack(fill="x", pady=(20, 10))

search_label = tk.Label(search_frame, text="Where to?", font=("Arial", 16), bg="#f5f5f5")
search_label.pack(side="left", padx=(0, 10))

search_entry = tk.Entry(search_frame, font=("Arial", 14), width=40, bd=2, relief="groove")
search_entry.pack(side="left", fill="x", expand=True)

search_button = tk.Button(search_frame, text="Search", font=("Arial", 12), 
                         bg="#00aa6c", fg="white", bd=0, padx=15)
search_button.pack(side="left", padx=(10, 0))

# Main content
content_frame = tk.Frame(canvas, bg=content_bg, padx=20, pady=20)
content_frame.pack(fill="both", expand=True)

# Heading with TripAdvisor style
heading_label = tk.Label(content_frame, 
                        text="Plan Your Perfect Solo Adventure", 
                        font=("Arial", 24, "bold"), 
                        bg=content_bg, fg="#003580")
heading_label.pack(pady=(0, 20))

# Button container
button_frame = tk.Frame(content_frame, bg=content_bg)
button_frame.pack(fill="both", expand=True)

# Custom styled buttons with TripAdvisor colors
def create_tripadvisor_button(parent, text, command, icon=None):
    btn_frame = tk.Frame(parent, bg=content_bg)
    btn_frame.pack(pady=10, fill="x")
    
    btn = tk.Button(btn_frame, text=text, font=("Arial", 14, "bold"), 
                   bg="#00aa6c", fg="white", bd=0, padx=20, pady=10,
                   command=command, relief="flat")
    btn.pack(fill="x")
    
    # Hover effects
    def on_enter(e):
        btn.config(bg="#008659")
    
    def on_leave(e):
        btn.config(bg="#00aa6c")
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    return btn

explore_btn = create_tripadvisor_button(button_frame, "🌍 Explore Popular Destinations", explore_places)
book_btn = create_tripadvisor_button(button_frame, "✈️ Book Flights & Hotels", book_journey)
reviews_btn = create_tripadvisor_button(button_frame, "⭐ Read Traveler Reviews", view_reviews)
tips_btn = create_tripadvisor_button(button_frame, "💡 Get Solo Travel Tips", show_travel_tips)

# Featured destinations (simulated)
destinations_frame = tk.Frame(content_frame, bg=content_bg)
destinations_frame.pack(fill="x", pady=(30, 10))

dest_label = tk.Label(destinations_frame, text="Featured Solo Destinations", 
                     font=("Arial", 16, "bold"), bg=content_bg, fg="#003580")
dest_label.pack(anchor="w")

# Destination cards
cards_frame = tk.Frame(destinations_frame, bg=content_bg)
cards_frame.pack(fill="x", pady=10)

destinations = [
    {"name": "Gokarna, Karnataka", "type": "Beach retreat"},
    {"name": "Varanasi, Uttar Pradesh", "type": "Temple Town"},
    {"name": "Shillong, Assam", "type": "Hilly City"},
    {"name": "Panjim, Goa", "type": "Party Capital"}
]

for dest in destinations:
    card = tk.Frame(cards_frame, bg="white", padx=10, pady=10, relief="groove", bd=1)
    card.pack(side="left", padx=10, fill="y")
    
    tk.Label(card, text=dest["name"], font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
    tk.Label(card, text=dest["type"], font=("Arial", 10), bg="white", fg="#666").pack(anchor="w")
    
    # Simulated rating (stars)
    rating_frame = tk.Frame(card, bg="white")
    rating_frame.pack(anchor="w", pady=5)
    
    for i in range(5):
        tk.Label(rating_frame, text="★", font=("Arial", 12), 
                bg="white", fg="gold" if i < 4 else "lightgray").pack(side="left")

# Footer (TripAdvisor style)
footer_frame = tk.Frame(canvas, bg="#003580", height=40)
footer_frame.pack(fill="x", side="bottom")

footer_text = tk.Label(footer_frame, text="© 2025 Itinero", 
                      font=("Arial", 10), fg="white", bg="#003580")
footer_text.pack(pady=10)

# Main loop
root.mainloop()