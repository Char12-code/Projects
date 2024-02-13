import random
import json

class TarotCard:
    def __init__(self, name, category, upright, inverted):
        self.name = name
        self.category = category
        self.is_upright = self.decide_orientation()
        self.meanings = upright if self.is_upright else inverted

    def decide_orientation(self):
        return random.choice([True, False])

    def get_meaning(self, topic):
        return self.meanings.get(topic, f"No meaning found for the {topic} topic.")

class TarotReading:
    def __init__(self, tarot_deck):
        self.tarot_deck = tarot_deck

    def start_reading(self, num_cards=10):  # Default to drawing 10 cards
        print("Welcome to the Tarot Reading! Press Enter to reveal each card.")
        print("Before we start, let me give you a brief explanation of how tarot works.")

        # Explanation of tarot
        input("Press Enter to continue...")
        print("\nTarot cards are often used for gaining insights into various aspects of life, including love, career, and finance.")
        print("When a card is drawn, its meaning may vary based on whether it's upright or inverted (reversed).")
        print("Let's get started!")

        # Get the user's chosen topic before revealing the cards
        user_topic = input("Choose a subject for all cards (love, career, finance): ").lower()

        # Check if the user's input is valid
        valid_subjects = ["love", "career", "finance"]
        if user_topic not in valid_subjects:
            print("Invalid input. Please choose from the available subjects.")
            return

        # Shuffle the tarot deck to get random cards
        random.shuffle(self.tarot_deck)

        # Tarot reading process
        for i in range(1, num_cards + 1):
            # Display the card information and meaning
            print(f"\nCard {i}: {self.tarot_deck[i-1].name} ({self.tarot_deck[i-1].category})")
            if self.tarot_deck[i-1].is_upright:
                print("Your card's orientation is upright")
            else:
                print("Your card's orientation is inverted (reversed)")
            print(f"Meaning for {user_topic.capitalize()}: {self.tarot_deck[i-1].get_meaning(user_topic)}")
            # Wait for the user to press Enter to reveal the next card
            input("\nPress Enter to continue...")

        # End of the tarot reading
        print("\nTarot Reading Complete! Thank you for participating.")

# Read data from the JSON file
with open('tarot_data.json', 'r') as data_file:
    tarot_data = json.load(data_file)

# Create the tarot deck
tarot_deck = [TarotCard(card['name'], card['category'], card['upright'], card['inverted']) for card in tarot_data]

# Create a TarotReading instance and start the reading with 10 cards
tarot_reading = TarotReading(tarot_deck)
tarot_reading.start_reading(num_cards=10)
