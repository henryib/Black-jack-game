from src.hand import Hand

class Dealer:
	def __init__(self):
		self.hand = Hand()
		self.is_busted = False

	def hit(self, deck): 
		# add card from deck to dealers hand
		self.hand.add_card(deck.deal_card())
		# deals with the case where an ace is drawn
		self.hand.account_for_aces()
		# if the value of the dealers hand is over 21 then he has gone bust
		if self.hand.value > 21:
			self.is_busted = True