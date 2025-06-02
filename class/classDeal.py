from classStack import makeStack
from random import shuffle

dealerStack = makeStack.makeDealerStack(1)
shuffle(dealerStack)
# print(dealerStack[0])
playerHand = []
dealerHand = []

class makeDeal:
    def __init__(deal, numCards):
        makeDeal.numCards = numCards



    # newDeal
    # returns new hands for player and dealer (2 cards apiece)
    # reads and removes from dealerStack
    def newDeal():
        playerCards = 2
        dealerCards = 2
        while playerCards > 0:
            newCard = dealerStack.pop(0)
            playerHand.append(newCard)
            playerCards -= 1
        while dealerCards > 0:
            newCard = dealerStack.pop(0)
            dealerHand.append(newCard)
            dealerCards -= 1
            
    newDeal() 
    print("Player hand:",playerHand)
    print("Dealer hand:",dealerHand)
    
    
    
    
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