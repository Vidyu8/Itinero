import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

class Review:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

class UserReview:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

class Place:
    def __init__(self, name, info, reviews=None):
        self.name = name
        self.info = info
        self.reviews = reviews if reviews else []
        self.user_reviews = []

    def add_review(self, rating, comment):
        review = Review(rating, comment)
        self.reviews.append(review)

    def add_user_review(self, rating, comment):
        user_review = UserReview(rating, comment)
        self.user_reviews.append(user_review)

    def get_place_reviews(self):
        return self.reviews

    def get_user_reviews(self):
        return self.user_reviews

class City:
    def __init__(self, name, places):
        self.name = name
        self.places = places

    def get_place_info(self, place_name):
        for place in self.places:
            if place.name == place_name:
                return place.info
        return None

    def get_place_reviews(self, place_name):
        for place in self.places:
            if place.name == place_name:
                return place.get_reviews()
        return None

    def get_place_user_reviews(self, place_name):
        for place in self.places:
            if place.name == place_name:
                return place.get_reviews()
        return None

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Database:
    def __init__(self):
        self.cities = []
        self.users = []

    def add_city(self, city):
        self.cities.append(city)

    def get_city(self, city_name):
        for city in self.cities:
            if city.name == city_name:
                return city
        return None
    
    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    def user_exists(self, username):
        return any(user.username == username for user in self.users)

class TravelApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Travel App")
        self.geometry("400x300")

        # Main container frame
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store pages
        self.pages = {}

        # Create pages
        self.create_home_page()
        self.create_registration_page()
        self.create_login_page()
        self.create_flight_booking_page()

        # Show home page by default
        self.show_page("Home")

    def create_home_page(self):
        """Create the home page."""
        home_page = ttk.Frame(self.container, style="Page.TFrame")
        home_page.pack(fill="both", expand=True)  # Ensure it's visible

        # Label and buttons
        label = ttk.Label(home_page, text="Welcome to the Travel App", font=("Garamond", 16, "bold"))
        register_button = ttk.Button(home_page, text="Register", command=lambda: self.show_page("Register"))
        login_button = ttk.Button(home_page, text="Login", command=lambda: self.show_page("Login"))

        # Layout
        label.pack(pady=10)
        register_button.pack(pady=5)
        login_button.pack(pady=5)

        # Add to pages
        self.pages["Home"] = home_page

    def create_registration_page(self):
        """Create the registration page."""
        reg_page = ttk.Frame(self.container, style="Page.TFrame")
        reg_page.pack(fill="both", expand=True)

        ttk.Label(reg_page, text="Register Here", font=("Garamond", 14, "bold")).pack(pady=10)
        ttk.Label(reg_page, text="Name:").pack()
        ttk.Entry(reg_page).pack()
        ttk.Label(reg_page, text="Email:").pack()
        ttk.Entry(reg_page).pack()
        ttk.Label(reg_page, text="Password:").pack()
        ttk.Entry(reg_page, show="*").pack()

        ttk.Button(reg_page, text="Submit", command=lambda: self.show_page("Home")).pack(pady=10)
        ttk.Button(reg_page, text="Back", command=lambda: self.show_page("Home")).pack()

        self.pages["Register"] = reg_page

    def create_login_page(self):
        """Create the login page."""
        login_page = ttk.Frame(self.container, style="Page.TFrame")
        login_page.pack(fill="both", expand=True)

        ttk.Label(login_page, text="Login", font=("Garamond", 14, "bold")).pack(pady=10)
        ttk.Label(login_page, text="Email:").pack()
        ttk.Entry(login_page).pack()
        ttk.Label(login_page, text="Password:").pack()
        ttk.Entry(login_page, show="*").pack()

        ttk.Button(login_page, text="Login", command=lambda: self.show_page("FlightBooking")).pack(pady=10)
        ttk.Button(login_page, text="Back", command=lambda: self.show_page("Home")).pack()

        self.pages["Login"] = login_page

    def create_flight_booking_page(self):
        """Create the flight booking page."""
        flight_page = ttk.Frame(self.container, style="Page.TFrame")
        flight_page.pack(fill="both", expand=True)

        ttk.Label(flight_page, text="Book a Flight", font=("Garamond", 14, "bold")).pack(pady=10)
        ttk.Label(flight_page, text="From:").pack()
        ttk.Entry(flight_page).pack()
        ttk.Label(flight_page, text="To:").pack()
        ttk.Entry(flight_page).pack()

        ttk.Button(flight_page, text="Search Flights").pack(pady=10)
        ttk.Button(flight_page, text="Back", command=lambda: self.show_page("Home")).pack()

        self.pages["FlightBooking"] = flight_page

    def show_page(self, page_name):
        """Show the requested page."""
        # Hide all pages first
        for page in self.pages.values():
            page.pack_forget()

        # Show the requested page
        self.pages[page_name].pack(fill="both", expand=True)


# Run the application
if __name__ == "__main__":
    app = TravelApp()
    app.mainloop()


if __name__ == "__main__":
    my_database = Database()

    city1 = City("Mumbai", [
        Place("1.Gateway Of India", "The Gateway of India in Mumbai is a major tourist attraction.It's a 16-meter-high monument that commemorates the 1911 visit of King George V and Queen Mary to Mumbai. The Gateway is a symbol of India's rich cultural heritage and colonial past. It's also known as the 'Taj Mahal of Mumbai'.Here are some reasons to visit the Gateway of India:\nArchitecture: The Gateway is a triumphal arch with intricate carvings.\nPanoramic views: The Gateway offers views of the Arabian Sea.\nCultural heritage: The Gateway is a reminder of India's colonial past.\nThe Gateway is very popular and can get crowded. Some recommend visiting in the mornings before 8 AM or late at night after 11 PM. To get a full view of the Gateway and the Taj Hotel, you can take a ferry ride.",[
            {"Rating":4.5,"Reviews":"\n\tPositive:An iconic landmark with stunning architecture. A must-visit spot for both locals and tourists. The view of the Arabian Sea is breathtaking.\nNegative: Can get crowded during peak hours, making it challenging to fully appreciate the beauty. Be cautious of street vendors who can be persistent."}
             ]),
        Place("2.Marine Drive", "Marine Drive is a 3 kilometre-long Promenade along the Netaji Subhash Chandra Bose Road in Mumbai, India.\nHere are some reasons to visit Marine Drive in Mumbai:\nViews: Marine Drive has views of the Arabian Sea, the city skyline, and the Queen's Necklace.\nPromenade: The curving pedestrian-only promenade is a great place to explore on foot.\nArt Deco buildings: The area has some of the finest Art Deco residential buildings facing the sea.\nStreet food: Try the delicious street food of Mumbai near the walkway and Chowpatty.\nEvents: Marine Drive hosts many popular events, including the Bombay Marathon, IAF Airshow, French Festival, and International Fleet Review.",[
            {"Rating":4.7,"Reviews":"\n\tPositive: A picturesque promenade with mesmerizing views of the sea and skyline. Perfect for a leisurely evening stroll or enjoying the sunset.\n\tNegative:Traffic congestion can be an issue, and the area may get crowded. It's advisable to visit during non-peak hours for a more peaceful experience."}
             ]),
        Place("3.Shree Siddhivinayak Temple","The Shree Siddhivinayak Ganapati Mandir Trust is a famous and popular temple in Mumbai. It's dedicated to Lord Ganesha and is considered one of the most heavily guarded sites in the city.\nThe temple was built on November 19, 1801. The original structure was a small brick building with a dome-shaped shikhara. The temple was built by Laxman Vithu Patil and funded by Deubai Patil.\nThe temple's name, 'Siddhivinayak', reflects the belief that Lord Ganesha grants success and accomplishments to his devotees.\nThe temple's idol is made from a single piece of black stone. It depicts Lord Ganesha with four hands, each holding a lotus, a small ax, a plate of modak, and a garland of holy beads.\nThe idol's trunk is tilted to the right, which is considered auspicious.\nThe temple is a six-story, multiangular structure with a gold-plated dome. It has three main entrances and is surrounded by small crowns made of gold and panchadhatu (five metals).\nThe temple offers free darshan for all devotees. VIP darshan tickets can be purchased at the temple counter for around Rs. 200 per person",[
            {"Rating":4.6,"Reviews":"\n\tPositive: A spiritually enriching experience with a divine atmosphere. The temple's architecture is captivating, and the positive energy is palpable.\n\tNegative: Weekends and festivals can lead to long queues, so plan your visit accordingly. Photography inside the temple is not allowed."}
             ]),
        Place("4.Bandra Worli Sea Link","The Bandra-Worli Sea Link, also known as the Rajiv Gandhi Sea Link, is a cable-stayed bridge that connects Bandra in the Western Suburbs of Mumbai with Worli in South Mumbai. The bridge is 5.6 kilometers long, has eight lanes, and is 126 meters high.\nHere are some reasons to visit the Bandra-Worli Sea Link:\nEngineering: Marvel at the bridge's design and engineering.\nScenic views: Take in the views of the Mumbai skyline and the scenic route during the day.\nLit up at night: Take photos of the bridge when it's lit up at night.\nEarthquake resistance: The bridge was the first infrastructure project in Mumbai to use seismic arresters. It can withstand earthquakes up to 7.0 on the Richter scale.",[
            {"Rating":4.4,"Reviews":"\n\tPositive: An engineering marvel offering stunning views of the cityscape and the Arabian Sea. The drive across the sea link is a unique experience.\n\tNegative: Toll charges can be high, and traffic congestion is common during peak hours. Limited parking options for those who want to stop and take photos."}
            ]),
        Place("5.Chhatrapati Shivaji Terminus","Chhatrapati Shivaji Terminus (CST) is a historic railway station in Mumbai, India. It's a UNESCO World Heritage Site and a prominent landmark in the city.\nHere are some reasons to visit Chhatrapati Shivaji Terminus:\nArchitecture: The station's architecture is a mix of Victorian, Italianate, and Mughal styles. It's also an example of 19th century railway architecture in the British Commonwealth.\nCentral dome: The station's central dome is the world's first octagonal ribbed masonry dome in the Italian Gothic Revival style.\nGround plan: The station's ground plan is similar to traditional Indian palace architecture.\nUse: The station is still in use today, serving as the headquarters of Central Railways and used by over three million people every day.",[
            {"Rating":4.8,"Reviews":"\n\tPositive: A UNESCO World Heritage Site with magnificent architecture. The hustle and bustle of the station capture the essence of Mumbai.\n\tNegative: Crowded during rush hours, and it's advisable to be cautious with belongings due to the heavy footfall. Photography may require permission."}
            ]),
        Place("6.Elephanta Caves","The Elephanta Caves are a collection of cave temples located on Elephanta Island in Western India.\nThe island is also known as Gharapuri.\nThe caves are dedicated to the Hindu god Shiva and feature rock-cut stone sculptures. The sculptures depict Hindu and Buddhist ideas and iconography.\nHere are some reasons to visit the Elephanta Caves:\nHistory: The caves date back to the 5th century and are a UNESCO World Heritage Site.\nCulture: The caves reflect ancient Indian culture, art, and architecture.\nSculptures: The caves feature sculptures and carvings based on Hindu and Buddhist mythology.\nFerry ride: You can take a ferry from the Gateway of India to the island.\nToy train: You can take a toy train ride.\nGuided tour: You can take a guided tour to learn about the history of the caves.",[
            {"Rating":4.3,"Reviews":"\n\tPositive: Historically rich caves with intricate sculptures. The boat ride to the island adds to the overall experience.\n\tNegative: Limited facilities on the island, and the climb to the caves can be strenuous for some. Check the boat schedule in advance."}
            ]),
        Place("7.Haji Ali Dargah","The Haji Ali Dargah is a mosque and tomb in Mumbai, India. It's located on an islet in the Arabian Sea, about 500 yards from the shoreline. The dargah is a famous landmark and a popular religious site.The dargah contains the tomb of Pir Haji Ali Shah Bukhari, a 15th-century Sufi saint. The dargah is associated with legends about doomed lovers. According to one legend, Haji Ali died while on a pilgrimage to Mecca and his casket floated back to the dargah.The dargah is an example of Indo-Islamic architecture. It's famous for its location, architecture, and religious significance. The shrine is popular with people of all faiths, including Hindus, Muslims, Christians, Sikhs, and Parsis.The dargah is only accessible at low tide. You can visit the shrine via a long causeway.",[
            {"Rating":4.5,"Reviews":"\n\tPositive: A serene and spiritually uplifting place. The location in the middle of the sea and the architecture are awe-inspiring.\n\tNegative: During high tide, the causeway leading to the dargah may get submerged, making access difficult. Respect local customs and dress modestly."}
            ]),
        Place("8.Juhu Beach","Juhu Beach is Mumbai's longest and most popular beach. It's located in the Juhu suburb, which is home to many Bollywood celebrities. The beach is known for its:\nLength: The beach stretches for six kilometers along the Arabian Sea.\nStreet food: The beach has a variety of street food stalls that serve sweet and sour Mumbai street food.\nBollywood: The beach is associated with Bollywood and has been used as a filming location.\nBioluminescence: The beach glows at night from a combination of bioluminescent phytoplankton and city lights.",[
            {"Rating":4.2,"Reviews":"\n\tPositive: A popular beach with a lively atmosphere. Perfect for a relaxing evening, enjoying street food, and watching the sunset.\n\tNegative: Crowded on weekends, and cleanliness can be a concern. Be cautious with belongings, and avoid the water during monsoon due to strong currents."}
            ]),
        Place("9.Mount Mary Basilica","Mount Mary's Basilica, also known as the Basilica of Our Lady of the Mount, is a Roman Catholic church in Bandra, Mumbai. The church is dedicated to the Virgin Mary. The basilica was established in 1640.  The current church building is about 100 years old.  The church's center piece is a statue of Mother Mary holding Jesus. The statue was brought to Bandra by Jesuit priests from Portugal in the 16th century. In 1700, Arab pirates cut off the statue's right hand.The basilica is located on a hillock, about 80 meters above sea level. It offers views of the Arabian Sea and the city's skyline. The church is considered one of the most holy places for Christians.",[
            {"Rating":4.6,"Reviews":"\n\tPositive: A serene and beautiful church with a panoramic view of the Arabian Sea. The annual Bandra Fair is a cultural highlight.\n\tNegative: Limited parking space, and the area can get crowded during religious events. Check the timings for prayer services and events in advance."}
            ]),
        Place("10.Sanjay Gandhi National Park","Sanjay Gandhi National Park (SGNP) in Mumbai is one of the most visited national parks in Asia. The park is 103 square kilometers and is the only national park in the world located within a city\nHere are some reasons to visit SGNP:\nWildlife: The park is home to over 40 species of mammals, 254 species of birds, 150 species of butterflies, 78 species of reptiles and amphibians, and 1300 plant species. The park also has a lion and tiger safari zoo.\nKanheri Caves: The park is home to the famous Kanheri Caves, which is one of the largest cave complexes in India. The caves are home to 106 Buddhist monastic caves.\nRecreational activities: The park has many recreational activities, including jungle safari, trekking, and two lakes.\nHistorical and cultural significance: The park has historical and cultural significance that dates back to the 4th century BCE.",[
            {"Rating":4.4,"Reviews":"\n\tPositive: A green oasis in the heart of the city, offering a variety of flora and fauna. The Kanheri Caves and Tiger Safari are major attractions.\n\tNegative: Weekends can be crowded, and the park may close during heavy rains. Plan accordingly, and be prepared for some walking if exploring on foot."}
            ]),
        ])

    city2 = City("Bangalore", [
        Place("1.Lalbagh Botanical Garden", "Internationally renowned as a centre for botanical artwork and conservation of plants, Lalbagh is one of the most scenic gardens in the state. Sprawling over an area of 240 acre, the park draws visitors in large numbers with its popular glass house and also serves as a home for as many as 1,854 species of plants.",[
            {"Rating":4.7,"Reviews":"\n\tPositive: A breathtaking botanical garden with diverse flora. The well-maintained grounds and seasonal flower shows make it a paradise for nature lovers.\n\tNegative: Weekend crowds can be overwhelming, impacting the peaceful ambiance. Some areas might benefit from improved signage."}
            ]),
        Place("2.Banglore Palace", "The Bangalore Palace is famous for its beautiful wood carvings and fascinating architecture. To an extent, it resembles the medieval castles of Normandy and England as it has been built in the Tudor style of architecture, with Scottish Gothic influences.",[
            {"Rating":4.6,"Reviews":"\n\tPositive: A regal experience with magnificent architecture and informative guided tours. The palace's historical significance and European design are captivating.\n\tNegative: Restricted photography inside the palace may disappoint some visitors, and the entrance fee is relatively high for some."}
            ]),
        Place("3.Tippu Sultan Summer Palace","Tipu Sultan's Summer Palace, in Bangalore, India, is an example of Indo-Islamic architecture and was the summer residence of the Mysorean ruler Tipu Sultan. Hyder Ali commenced its construction within the walls of the Bangalore Fort, and it was completed during the reign of Tipu Sultan in 1791.A small part of Tipu Sultan's Summer Palace has been converted into a museum lately, which displays various antiques and knick-knacks of Tipu Sultan himself and his father, Hyder Ali. It showcases weapons of war, clothes and knight armors of the two kings, coins, crowns etc.Tipu Sultan's Summer Palace, in Bangalore is an example of Indo-Islamic architecture and was the summer residence of the Mysorean ruler Tipu Sultan. Hyder Ali commenced its construction within the walls of the Bangalore Fort, and it was completed during the reign of Tipu Sultan in 1791",[
            {"Rating":4.5,"Reviews":"\n\tPositive: A historical gem showcasing Indo-Islamic architecture. The museum offers insights into Tipu Sultan's life, and the surrounding gardens enhance the visit.\n\tNegative: Limited parking and a relatively small palace might make the visit seem brief. Crowds can be a concern during peak hours."}
            ]),
        Place("4.Vidhana Saudha","Vidhana Soudha in Bangalore, India, is the seat of the state legislature of Karnataka. It is constructed in a style described as Neo-Dravidian, and incorporates elements of various Dravidian styles. Construction was started in 1952 and completed in 1956.Built with granite, Vidhana Soudha is the largest legislative building in India. It measures 213.36 by 106.68 metres (700.0 by 350.0 ft) on the ground and is 53.34 metres (175.0 ft) tall. The architecture includes elements of styles from the mediaeval Chalukya, Hoysala and Vijayanagara empires of Karnataka.",[
            {"Rating":4.4,"Reviews":"\n\tPositive: An architecturally impressive government building, especially illuminated at night. The surrounding area is well-maintained and suitable for a leisurely stroll.\n\tNegative: Restricted entry limits the overall visitor experience. Traffic congestion in the vicinity can be challenging."}
            ]),
        Place("5.HAL Heritage Centre And Aerospace Museum","HAL Aerospace Museum is India's first aerospace museum located at Hindustan Aeronautics Limited premises, in Bangalore. Established in 2001, the Museum is part of the HAL Heritage Centre and Aero Space Museum, and showcases the growth of the Indian aviation industry and HAL for six decades.HAL Heritage Centre and Aerospace Museum was established by Hindustan Aeronautics Limited. The museum displays a varied collection of aircraft models, fighter planes and helicopters. The museum also houses a reference library, aircraft simulators, a mock air traffic control tower and an aeromodelling club.",[
            {"Rating":4.8,"Reviews":"\n\tPositive: A fascinating museum showcasing India's aerospace achievements. The outdoor aircraft display is a highlight, and the educational value is commendable.\n\tNegative: Some interactive exhibits may require maintenance, and the museum can be crowded during school holidays."}
            ]),
        Place("6.UB City","UB City is a business district in Bengaluru, India. It consists of 6 blocks with a total built up area of over 16 lakh sq ft. Pioneered by the UB Group in Joint Venture with Prestige Group, it is built on 13 acres of land and hosts 1,000,000 sq ft of high-end commercial, retail and service apartment space.UB City is a prominent commercial complex located in Bangalore, India. It is known for its upscale shopping, dining, and office spaces. The complex is situated in the heart of the city, making it a hub for business and entertainment.",[
            {"Rating":4.6,"Reviews":"\n\tPositive: A luxurious destination with modern architecture and high-end shopping and dining options. The ambiance is sophisticated, and it attracts those with discerning tastes.\n\tNegative: Limited parking and an upscale nature that may not cater to all budgets. Casual dining options are relatively limited."}
            ]),
        Place("7.Madivala Lake","Madiwala lake is one of the biggest lakes in Bangalore, India spread over an area of 114.3 hectare. The water in the lake was fit for drinking till the early 1990s. Since then it has become unfit for drinking due to industrial waste and sewage entering the waterbody. It has gradually become polluted.",[
            {"Rating":4.3,"Reviews":"\n\tPositive: A peaceful lake surrounded by greenery, ideal for a relaxing stroll or boating. Birdwatching opportunities make it popular among nature enthusiasts.\n\tNegative: Crowded lakefront, especially on weekends. Facilities like boating docks may require better maintenance."}
            ]),
        Place("8.St. Mary's Basilica","St. Mary's Basilica is located in the Archdiocese of Bangalore in the Indian state of Karnataka. It is among the oldest churches in Bangalore and the first church in the state that has been elevated to the status of a minor basilica.Built in 1882, St. Mary's Basilica is the oldest church in Bangalore and is the only church in the state that has been elevated to the status of a minor basilica. It is famous for the festivities it holds during the St. Mary's Feast, in September each year.",[
            {"Rating":4.7,"Reviews":"\n\tPositive: A historic and architecturally rich church with a serene atmosphere. Stained glass windows and religious artifacts create an impressive spiritual experience.\n\tNegative: Limited parking, and it may get crowded during religious events. Some visitors may find the interior dimly lit."}
            ]),
        Place("9.Big Bull Temple","This temple is noted for its large statue of sacred bull,Nandi. Standing at a height of around 4 m, the statue has been carved out of a single grey granite stone and has been polished black with a mixture of charcoal powder and peanut oil.16th-century Hindu temple containing a sculpture of the sacred bull carved out of granite.",[
            {"Rating":4.5,"Reviews":"\n\tPositive: A significant religious site with a massive Nandi statue and unique architecture. The surrounding market adds to the cultural experience.\n\tNegative: Crowded area, and the market might be overwhelming. Limited parking space adds to the challenge."}
            ]),
        Place("10.Bugle Rock Temple","Serene park shaded by a tree canopy featuring gardens, waterfalls & fountains, plus three temples.Situated in N R Colony,Basavanagudi in Bangalore, Bugle Rock Park is famous for the central rock formed through geological changes over the years. Besides scientists and regular geologists, the park experiences a regular influx of tourists. There is also a watchtower that offer a bird's eye view of the city.",[
            {"Rating":4.4,"Reviews":"\n\tPositive: An ancient temple with a unique rock formation and historical significance. The panoramic view and peaceful surroundings make it ideal for meditation.\n\tNegative: Limited facilities, and the climb to the temple may be challenging. Some visitors may prefer more detailed information about the temple's history."}
            ])
        ])

    city3 = City("Pondicherry",[
        Place("1.Paradise Beach","Paradise Beach, also known as Plage Paradiso, is a secluded beach in Pondicherry. It's located about 7 kilometers south of Pondicherry and 10 kilometers from the city center. The beach is situated where the Chunnambar River meets the Bay of Bengal.\nParadise Beach is known for its: White sand, Clear water, Palm trees, Waves, Scenic setting.\nTo get to Paradise Beach, you can take a ferry from Chunnambar Boat House. The boat ride takes about 10 minutes and costs a fee.\nParadise Beach is also known for being a party beach.",[
            {"Rating":4.8,"Reviews":"\n\tPositive: A pristine and secluded beach with golden sand and clear waters. The boat ride to reach the beach adds to the adventure, and the natural beauty makes it a paradise for beach lovers.\n\tNegative: Limited facilities on the beach, so visitors should come prepared with essentials. Weekends can be busier, affecting the tranquil atmosphere."}
            ]),
        Place("2.Arulmigu Manakula Vinayagar Temple","Arulmigu Manakula Vinayagar Temple is one of the famous ancient Lord Ganesha temple in Puducherry (also known as Pondicheery), a Union Territory of India. There is a Golden Chariot in the temple which was made purely on the basis of the collection of donations from the devotees.\nOnce in a year on Vijayadhasami day, the Golden Chariot runs outside of the temple. The temple has an elephant, whom the visitors offer a coin to get a pat on their head through his trunk as a blessing.",[
            {"Rating":4.5,"Reviews":"\n\tPositive: A spiritually significant temple with a peaceful ambiance. The intricate architecture and the cultural experience during festivals make it a must-visit for devotees and tourists alike.\n\tNegative: During peak hours, the temple can get crowded, and visitors should be respectful of religious customs and dress modestly."}
            ]),
        Place("3.Rock Beach","Rock Beach, also known as Promenade Beach, is a popular beach in Pondicherry, India. It's located along the Bay of Bengal and is known for its:\nArt and culture, sunrise, sunset, and moonrise, monuments and landmarks, waves.The beach is also known for its seawall. The government of Pondicherry fortified the boulders along the shore about two decades ago to prevent erosion.",[
            {"Rating":4.7,"Reviews":"\n\tPositive: A picturesque promenade along the Bay of Bengal with a vibrant atmosphere. Perfect for a leisurely stroll, and the waves crashing against the rocks provide a soothing backdrop.\n\tNegative: Crowded during evenings, and finding parking can be a challenge. Some areas might benefit from additional seating for visitors."}
            ]),
        Place("4.Aurobindo Ashram","The Sri Aurobindo Ashram is a spiritual community in Pondicherry, India. It was founded in 1926 by Sri Aurobindo Ghosh, a philosopher-poet. The ashram grew out of a small group of disciples who gathered around Aurobindo after he retired from politics and settled in Pondicherry in 1910.Here are some reasons to visit the Sri Aurobindo Ashram:\nSpiritual growth: The ashram's practices and teachings can help you explore your inner self and deepen your understanding of spirituality.\nMeditation: Meditation is a key part of the ashram's Internal Yoga practice.\nExhibits: The ashram's Bureau Central office has exhibits that introduce visitors to the teachings and vision of Sri Aurobindo and The Mother.\nQuiet reflection: The ashram is a place for quiet reflection, with a large tree providing shade over the tomb of Sri Aurobindo and The Mother.\nThe ashram is open to the public daily from 8–11 AM and 3–5 PM",[
            {"Rating":4.6,"Reviews":"\n\tPositive: A serene and meditative space with a rich spiritual heritage. The ashram offers tranquility and a chance for introspection. The bookshop provides valuable literature on philosophy and yoga.\n\tNegative: Silence should be maintained within the ashram, and visitors should respect the rules. Limited parking may require visitors to find alternative arrangements."}
            ]),
        Place("5.Basilica The Sacred Heart Of Jesus","The Basilica of the Sacred Heart of Jesus is a Roman Catholic church in Pondicherry, India. It's located in the old town, on the South Boulevard. The church is a famous landmark and one of the most revered basilicas in India.The church was built by French missionaries in 1908. It's a Gothic structure with a Latin cross shape. The Basilica of the Sacred Heart of Jesus is a popular destination for tourists. Some reasons to visit include:\nArchitecture: The church is a fine example of Gothic architecture.\nStained glass: The church has colorful stained glass panels that depict events in the life of Jesus.\nCultural significance: The church is a revered pilgrimage site.\nCultural significance: The church is a revered pilgrimage site.\nPilgrims: The church attracts Catholics from across India. Pilgrims visit during Christmas and other festive masses.\nCelebrations: The church has grand celebrations on Christmas Eve and New Year's Eve.",[
            {"Rating":4.8,"Reviews":"\n\tPositive: A majestic church with stunning architecture and a serene atmosphere. The religious significance and the panoramic view of the city from the church premises make it a must-visit.\n\tNegative: During religious events, the church can get crowded. Visitors should be mindful of maintaining a quiet and respectful environment."}
        ])
    ])