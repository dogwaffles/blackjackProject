#thanks to geeksforgeeks.org
import sys
sys.path.insert(0, '/home/louis/Documents/programming/python/blackjackProject/fclass')

import ast
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
    Deck.printCards(currentHand)

# printHand(dealerCurrentHand)
# print(dealerCurrentHand)

def cardToList(cardList): #DEL deprecated 
    newCardList = []
    for card in cardList:
        cardVal = card[0]
        cardFace = card[1]
        cardSuit = card[2]
        newCardList.append(Card(cardVal, cardFace, cardSuit))
    return cardList

# print(readCard(dealerCurrentHand)[0])

# def printHand(hand):
#     # list(hand)
#     for card in hand:
#         cardIndex = hand.index(card)
        # print(readCard(Card.PrintCard(dealerCurrentHand[cardIndex])))

# printHand(dealerCurrentHand)


# Protocol to convert card object to usable data USEFUL
# print(printHand(dealerCurrentHand))
# print(dealerCurrentHand[0].cardVal)

print("Dealer has ",end=""), printHand(dealerCurrentHand)
print("Player has: ",end=""), printHand(playerCurrentHand)

