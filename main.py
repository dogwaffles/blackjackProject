#thanks to geeksforgeeks.org
#easy way to add seperate folder for imports
import sys
sys.path.insert(0, '/home/louis/Documents/programming/python/blackjackProject/fclass')

from classAction import Action
from classCard import Card
from classDeck import Deck


#new hands dealt
dealerCurrentHand = Action.dealerDeal()
playerCurrentHand = Action.playerDeal()


# input array of class Card
# output imagified cards for playspace
printCards = Deck.printCards



#TEST CASES

print("Dealer has: ",end=""), printCards(dealerCurrentHand)
print("Player has: ",end=""), printCards(playerCurrentHand)

