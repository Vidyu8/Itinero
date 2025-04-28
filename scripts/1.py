import json

class Place:
    def __init__(self, name, description, reviews):
        self.name = name
        self.description = description
        self.reviews = reviews

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "reviews": self.reviews
        }

class City:
    def __init__(self, name, places):
        self.name = name
        self.places = places

    def to_dict(self):
        return {
            "city": self.name,
            "places": [place.to_dict() for place in self.places]
        }

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

# Convert to JSON
json_data = json.dumps(city3.to_dict(), indent=4)

# Save to a file
with open("pondicherry_places.json", "w", encoding="utf-8") as f:
    f.write(json_data)

print("JSON file created successfully!")