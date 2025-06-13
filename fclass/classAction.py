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
    

    #global is useful here so functions can modify variables
    global playerCurrentHand
    playerCurrentHand = []
    global dealerCurrentHand
    dealerCurrentHand = []
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
    
    #CHECKHANDVAL
    #input int
    #if int > 21, hand is bust, game is over
    #returns playerBust() (ends game, play again?) 
    #or FALSE

    def checkHandVal(val):
        if val > 21:
            return True
            
    #CALCDEALERHVAL
    #input hand
    #returns int based on dealer card values
    global dealerHandVal
    def calcDealerVal(hand):
        dealerHandVal = 0
        for card in hand:
            dealerHandVal += card.cardVal
        if dealerHandVal > 21:
            for card in hand:
                if card.cardVal == 11:
                    dealerHandVal -= 10
                    return dealerHandVal
        return dealerHandVal
    
    #PLAYERDRAW
    #accepts a list (playerCurrentHand)
    #appends a card from dealerStack(.pop)
    def playerDraw(hand):
        newCard = dealerStack.pop(0)
        print("You drew a ", Card.PrintCard(newCard))
        hand.append(newCard)
        return hand

    #PLAYERSTAND
    #ends player turn (moves to dealer turn)
    def playerStand():
        Action.dealerPlay()

    #PLAYERBUST
    #ends game with a loss
    def playerBust(hand):
        print("You went bust with a value of " + str(Action.calcPlayerVal(hand)))
        #modify to new game!!!
        exit()
    
    #PLAYERWIN
    #ends game with a win
    def playerWin():
        print("Your value was", Action.calcPlayerVal(playerCurrentHand))
        print("The dealer had a value of", Action.calcDealerVal(dealerCurrentHand))
        print("You win!")
        #!!!
        exit()


    #PLAYERPLAY
    #while game is active
    #modifies hand based on player action
    #takes input and modifies accordingly
    #hit - add a card
    #stand - end turn
    #double - double bet, add a card #!!!
    #split - splits into two hands #!!!
    def playerPlay(playerHand, dealerHand):
        print("You have: "), Deck.printCards(playerHand)
        if Action.calcPlayerVal(playerHand) > 21:
            Action.playerBust(playerHand)
        print("Dealer is showing: ['" +Card.printCard(dealerCurrentHand[0]) + "', '**']")
        play = input("Would you like to: \n (H)it? \n (S)tand?")
        if play == "S" or play == "stand":
            Action.playerStand()
        if play == "H" or play == "hit":
            Action.playerDraw(playerHand)
            Action.playerPlay(playerHand, dealerHand)
        else:
            print("Please enter a valid input! \n")
            Action.playerPlay()


    #DEALERSTAND
    #ends dealer phase, moves to comparative phase #ENDPHASE
    def dealerStand():
        Action.endPhase()

    #DEALERHIT
    #adds card to dealerHand from dealerStack
    def dealerHit():
        newCard = dealerStack.pop(0)
        dealerCurrentHand.append(newCard)

    #DEALERPLAY
    # input hand
    # output dealer hand value (or zero if bust)
    def dealerPlay(hand):

        if Action.calcDealerVal(dealerCurrentHand) > 21:
            Action.playerWin()
        if Action.calcDealerVal(dealerCurrentHand) > 16:
            Action.dealerStand()
        if Action.calcDealerVal(dealerCurrentHand) > 0:
            Action.dealerHit()
        else:
            "Error in Action.dealerPlay, dealer value <= 0" ; exit()
        

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
   