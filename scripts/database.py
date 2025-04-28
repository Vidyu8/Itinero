import json

DB_FILE = "database.json"

# Load data from JSON file
def load_data():
    with open(DB_FILE, "r") as file:
        return json.load(file)

# Save data to JSON file
def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new city
def add_city(city_name):
    data = load_data()
    if city_name not in data:
        data[city_name] = {"places": []}
        save_data(data)

# Add a new place
def add_place(city_name, place_name, info):
    data = load_data()
    if city_name in data:
        data[city_name]["places"].append({"name": place_name, "info": info, "reviews": []})
        save_data(data)

# Add a review
def add_review(city_name, place_name, review_text):
    data = load_data()
    for place in data.get(city_name, {}).get("places", []):
        if place["name"] == place_name:
            place["reviews"].append(review_text)
            save_data(data)
            return
