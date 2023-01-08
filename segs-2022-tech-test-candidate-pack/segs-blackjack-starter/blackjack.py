from src.deck import Deck
from src.player import Player
from src.dealer import Dealer

# game runs but functionality is wonky, rework 

class Blackjack:
    def __init__(self):
        # Initialize the deck object, player object and dealer object
        self.deck = Deck()
        self.player = Player("Player 1")
        self.dealer = Dealer()
        # Flags to track the game state and winner
        self.game_over = False
        self.winner = None

    def start(self):
        self.deck.shuffle()
        for x in range(2):
            self.player.hand.add_card(self.deck.deal_card())
            self.dealer.hand.add_card(self.deck.deal_card())
            self.dealer.hand.account_for_aces()

    def player_turn(self,choice):
        if choice == "h": 
            if self.player.hand.value > 21: 
                self.game_over = True
                self.winner = "dealer"
            self.player.hit(self.deck)
        else: 
            self.game_over = False

    def dealer_turn(self): 
        #Dealer can only hit until his hand value is up to 17
        if self.dealer.hand.value < 17: 
          
            if self.dealer.hand.value > 21: 
                self.game_over = True
                self.winner = "player"
            self.dealer.hit(self.deck)
        # game ends if the dealers hand is 21 or higher
        elif self.dealer.hand.value >= 21: 
            self.game_over = True 
        # here we could implement a strategy for the dealer once his hand is over 17   
        else: 
            self.game_over = True 

    def game_winner(self):
        if self.player.hand.value > self.dealer.hand.value: 
            self.winner = "player"
        elif self.dealer.hand.value > self.player.hand.value: 
            self.winner = "dealer"
        else: 
            self.winner = "Draw"


def play():
    print('Hello, potential future BBC developer!')  # execution starts here! delete this line and add your game code.
   
    game = Blackjack()
    game.start()

    while not game.game_over:
        print(f"Player's hand total value: {game.player.hand.value}")
        print(f"Dealer's hand total value: {game.dealer.hand.value}")

        if game.player.hand.value > 21: 
            print("Bust, dealer wins")
            break
        if game.dealer.hand.value > 21:
            break 

        choice = input(" Hit or stand? type: h or s: ")
        if choice == "h": 
            game.player_turn(choice)
        else:
            game.dealer_turn()

    if game.game_over: 
        game.game_winner()
        if game.winner == "player":
            print("You win hurray")
        elif game.winner == "dealer":
            print("Dealer won, unlucky")
            print(f"Dealer's hand total value: {game.dealer.hand.value}")
        else: 
            print("draw")

if __name__ == '__main__':
    play()
