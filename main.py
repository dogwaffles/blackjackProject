#thanks to geeksforgeeks.org
#easy way to add seperate folder for imports
# import sys
# sys.path.insert(0, '/home/louis/Documents/programming/python/blackjackProject/fclass')

#from .fclass import classAction
#from .fclass import classDeck
#from .fclass import classCard

from classAction import Action
from classCard import Card
from classDeck import Deck


#new hands dealt
dealerCurrentHand = Action.dealerDeal()
playerCurrentHand = Action.playerDeal()


#makes code more readable, shows card faces in playspace
printCards = Deck.printCards

#show player cards
print("Player has: ",end=""), printCards(playerCurrentHand)

#shows single card
printCard = Card.PrintCard

#show dealer card


# Action.playerDraw(playerCurrentHand)
# print("Player has: ",end=""), printCards(playerCurrentHand)


Action.playerPlay(playerCurrentHand, dealerCurrentHand)

#calculating hand values

#player
#CALCULATEPLAYERVAL

#dealer
#CALCULATEDEALERVAL



## MAIN GAME
# START GAME
# GAME PLAY (LOOP) # NEW CLASS?
#DEAL
#SHOW PLAYER HAND
#SHOW DEALER CARD
#PLAYER ACTION
#DEALER ACTION
#RESOLVE
#PLAY AGAIN?
#EXTRA (PLAYER STAT, ETC.)








#TEST CASES
# input array of class Card
# output imagified cards for playspace
printCards = Deck.printCards

print("Dealer has: ",end=""), printCards(dealerCurrentHand)
print("Player has: ",end=""), printCards(playerCurrentHand)

