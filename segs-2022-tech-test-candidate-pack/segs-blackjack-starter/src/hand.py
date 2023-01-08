from src.card import Card

class Hand:
	def __init__(self):
		# initilaise empty array for staoring cards
		self.cards = []
		self.value = 0 
		self.aces = 0 


	def add_card(self, card): 
		self.cards.append(card)
		self.value += self.get_card_value(card)
		if card.weight == "A" : 
			self.aces =+1


	def account_for_aces(self):
		# if the hand is over 21 and there is atleast 1 ace in the hand
		while self.value > 21 and self.aces > 0: 
			# dercrease the hand value by 10(aces can be 11 or 1)
			self.value -= 10 
			self.aces -=1


	def get_card_value(self, card): 
		#return card values based on the rules ive been given
		if card.weight == "A":
			return 11
		elif card.weight in ["J", "Q", "K"]:
			return 10 
		else: 
			#returnn face value
			return int(card.weight)
