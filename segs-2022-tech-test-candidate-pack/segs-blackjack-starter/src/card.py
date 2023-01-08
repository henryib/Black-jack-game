class Card: 
	def __init__(self,suit,weight):
		# Initialize the suit and weight of the card
		self.suit = suit
		self.weight = weight

	def __repr__(self):
		#return the string representation of tthe card 
		return f"{self.weight} of {self.suit}"