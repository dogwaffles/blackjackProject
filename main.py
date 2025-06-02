#thanks to geeksforgeeks.org
import sys
sys.path.insert(0, '/home/louis/Documents/programming/python/blackjackProject/fclass')

from classDeal import makeDeal
from classCard import Card

dealerCurrentHand = makeDeal.dealerDeal()
playerCurrentHand = makeDeal.playerDeal()
readCard = Card.PrintCard

def makeCard(list):
    cardList = []
    for card in list:
        cardVal = card[0]
        cardFace = card[1]
        cardSuit = card[2]
        cardList.append(Card(cardVal, cardFace, cardSuit))
    return cardList


print(readCard(makeCard(dealerCurrentHand)[0]))

def printHand(hand):
    # list(hand)
    for card in hand:
        cardIndex = hand.index(card)
        # print(readCard(Card.PrintCard(dealerCurrentHand[cardIndex])))

# printHand(dealerCurrentHand)

# print(printHand(dealerCurrentHand))

print("Dealer has", )
print("Player has", playerCurrentHand)

