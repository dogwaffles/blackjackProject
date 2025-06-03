from ClassDeck import Deck
from random import shuffle

# print(dealerStack[0])

class makeDeal:
    def __init__(deal, numCards):
        makeDeal.numCards = numCards



    def makeDealerStack(numDecks):
        deckStack = []
        newDeck = Deck.deckMake()
        while numDecks > 0:
            # print(decks) #DEL
            deckStack += newDeck
            numDecks -= 1
        return deckStack
    

    global dealerStack
    dealerStack = makeDealerStack(1)
    shuffle(dealerStack)


    # newDeal
    # returns new hands for player and dealer (2 cards apiece)
    # reads and removes from dealerStack
    def dealerDeal():
        dealerHand = []
        dealerCards = 5
        while dealerCards > 0:
            newCard = dealerStack.pop(0)
            dealerHand.append(newCard)
            dealerCards -= 1
        return (dealerHand)
    
    def playerDeal():
        playerCards = 2
        playerHand = []
        while playerCards > 0:
            newCard = dealerStack.pop(0)
            playerHand.append(newCard)
            playerCards -= 1
        return (playerHand)
    # print(newDeal())
    # newDeal() 
    # print("Player hand:",playerHand)
    # print("Dealer hand:",dealerHand)
    
    
    
    
    # dealerHand = []
    # playerHand = []
    # newStack = makeStack(1)


    # def makeDeal(deckStack):
    #     dealerStack = makeStack(1)
    #     dealerNum = 2
    #     playerNum = 2
    #     while playerNum > 0:
    #         newCard = dealerStack.pop(0)
    #         print(newCard)