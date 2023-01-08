import random
from src.card import Card

class Deck:
    def __init__(self):
        self.cards = [] # initialise empty array to store cards
        self.build_deck() # build the deck

    def build_deck(self):
        #lists of all suits and values/weights
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        weights = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        #loop through each suit and weight and creare a new Card object for each pair(52 cards)
        for suit in suits:
            for weight in weights:
                self.cards.append(Card(suit,weight))

    def shuffle(self):
        # randomly shuffle the dek of cards
        random.shuffle(self.cards)

    def deal_card(self):
        # Return the top card and remove it from the deck
        return self.cards.pop()