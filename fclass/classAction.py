from classDeck import Deck
from classCard import Card
from random import shuffle

# print(dealerStack[0])

class Action:
    def __init__(deal, numCards):
        Action.numCards = numCards


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
    

    #global is useful here so functions can modify the dealerStack while dealing
    global dealerStack
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
    
    #PLAYERHANDVAL
    #input a list of cards
    #return a value based on card.cardVal as global #playerHandVal
    #Aces have their value reduced to 1 if player is over 21
    global playerHandVal
    def calcPlayerVal(hand):
        playerHandVal = 0
        #iterates through hand, adds cards to accumulator
        for card in hand:
            playerHandVal += card.cardVal
        #checks if hand valuue is over 21
        if playerHandVal > 21:
            #checks for aces (card.cardVal == 11)
            for card in hand:
                #if any aces present (AND val > 21), subtract 10 ; return new hand value
                if card.cardVal == 11:
                    playerHandVal -= 10
                    return playerHandVal
        #else return hand value
        return playerHandVal

    

#GAMEPLAY START ###

card3 = Card(5, "5", "hearts")
card1 = Card(10, "3", "diamonds")
card2 = Card(11, "4", "spades")
cards  = [card1, card2, card3]

print(Action.calcPlayerVal(cards))



    #STARTDEAL 
    # starts the game
    # creates a dealer stack
    # deals two cards each to player and dealer
    # saves hands as playerHand and dealerHand
    # dealerStack can be modified with input option numDecks
    # .Deal functions should be modified to return nothing and write 
    #to global .Hand vars
    # def startDeal():
    #     dealerStack = Action.makeDealerStack(1)
    #     shuffle(dealerStack)
    #     Action.dealerDeal()
    #     Action.playerDeal()
   