#thanks to geeksforgeeks.org
import sys
sys.path.insert(0, '/home/louis/Documents/programming/python/blackjackProject/fclass')

import ast
from classAction import Action
from classCard import Card
from ClassDeck import Deck

dealerCurrentHand = Action.dealerDeal()
playerCurrentHand = Action.playerDeal()
readCard = Card.PrintCard

printHand = Deck.printHand

print("Dealer has ",end=""), printHand(dealerCurrentHand)
print("Player has: ",end=""), printHand(playerCurrentHand)

