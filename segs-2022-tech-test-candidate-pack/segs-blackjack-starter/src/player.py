from src.hand import Hand

class Player:
	def __init__(self, name):
		# inititialise the player name
		self.name = name
		# inititialise players hand as an object
		self.hand = Hand()

	def hit(self, deck):
		# add a card from the deck to the players hand
		self.hand.add_card(deck.deal_card())
		# for the case an ace is drawn
		self.hand.account_for_aces()


