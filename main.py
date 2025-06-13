#
from classAction import Action
from classHand import Hand


# new hands dealt
# I seperate this into two functions to avoid having to return to
#two variables simultaneously
dealerCurrentHand = Hand.dealerDeal()
playerCurrentHand = Hand.playerDeal()


#makes code more readable, shows card faces in playspace
# printCards = Deck.printCards
# hasattr
#show player 
# print("Player has: ",end=""), printCards(playerCurrentHand)

#shows single card
# printCard = Card.PrintCard

#show dealer card


# Action.playerDraw(playerCurrentHand)
# print("Player has: ",end=""), printCards(playerCurrentHand)

# Starts the game
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
# printCards = Deck.printCards

# print("Dealer has: ",end=""), printCards(dealerCurrentHand)
# print("Player has: ",end=""), printCards(playerCurrentHand)

