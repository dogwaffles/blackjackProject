#thanks to geeksforgeeks.org
import sys
sys.path.insert(0, '/home/louis/Documents/programming/python/blackjackProject/fclass')

from classDeal import makeDeal
from classCard import Card
from ClassDeck import Deck

dealerCurrentHand = makeDeal.dealerDeal()
playerCurrentHand = makeDeal.playerDeal()
readCard = Card.PrintCard

def printHand(hand):
    currentHand = []
    for card in hand:
        cardIndex = hand.index(card)
        currentHand.append(hand[cardIndex])
    Deck.printStack(currentHand)

printHand(dealerCurrentHand)

# def makeCard(list): #DEL deprecated 
#     cardList = []
#     for card in list:
#         cardVal = card[0]
#         cardFace = card[1]
#         cardSuit = card[2]
#         cardList.append(Card(cardVal, cardFace, cardSuit))
#     return cardList

# print(readCard(dealerCurrentHand)[0])

# def printHand(hand):
#     # list(hand)
#     for card in hand:
#         cardIndex = hand.index(card)
        # print(readCard(Card.PrintCard(dealerCurrentHand[cardIndex])))

# printHand(dealerCurrentHand)

# print(printHand(dealerCurrentHand))

print("Dealer has ",end=""), printHand(dealerCurrentHand)
print("Player has: ",end=""), printHand(playerCurrentHand)

