from classCard import Card
from classDeck import Deck
from random import shuffle

class Hand:
    def __init__(self, cards):
        Hand.cards = cards


    # input a number of decks
    # outputs a stack of cards for the dealer to draw from
    def makeDealerStack(numDecks):
        deckStack = []
        newDeck = Deck.deckMake()
        while numDecks > 0:
            # print(decks) #DEL
            deckStack += newDeck
            numDecks -= 1
        return deckStack
    

    #global is useful here so functions can modify variables

    global dealerStack
    #default option, meant to be modified
    dealerStack = makeDealerStack(1)
    shuffle(dealerStack)

    # initial deal for dealer (2 cards into dealerHand)
    # call to return dealerHand (fresh deal)
    def dealerDeal():
        dealerHand = []
        dealerCards = 2
        while dealerCards > 0:
            newCard = dealerStack.pop(0)
            dealerHand.append(newCard)
            dealerCards -= 1
        return (dealerHand)
    
    # see below
    def playerDeal():
        playerCards = 2
        playerHand = []
        while playerCards > 0:
            newCard = dealerStack.pop(0)
            playerHand.append(newCard)
            playerCards -= 1
        return (playerHand)