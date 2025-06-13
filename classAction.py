from classDeck import Deck
from classCard import Card
from classHand import Hand
from random import shuffle

printCards = Deck.printCards
# print(dealerStack[0])

class Action:
    def __init__(deal, numCards):
        Action.numCards = numCards

    


    # input a number of decks
    # outputs a stack of cards for the dealer to draw from
    # def makeDealerStack(numDecks):
    #     deckStack = []
    #     newDeck = Deck.deckMake()
    #     while numDecks > 0:
    #         # print(decks) #DEL
    #         deckStack += newDeck
    #         numDecks -= 1
    #     return deckStack
    

    #global is useful here so functions can modify variables
    global dealerStack
    from classHand import dealerStack
    # dealerStack = Hand.makeDealerStack(1)
    # shuffle(dealerStack)

    # initial deal for dealer (2 cards into dealerHand)
    # call to return dealerHand (fresh deal)
    # def dealerDeal():
    #     dealerHand = []
    #     dealerCards = 2
    #     while dealerCards > 0:
    #         newCard = dealerStack.pop(0)
    #         dealerHand.append(newCard)
    #         dealerCards -= 1
    #     return (dealerHand)
    
    # # see below
    # def playerDeal():
    #     playerCards = 2
    #     playerHand = []
    #     while playerCards > 0:
    #         newCard = dealerStack.pop(0)
    #         playerHand.append(newCard)
    #         playerCards -= 1
    #     return (playerHand)
    
    #PLAYERHANDVAL
    #input a list of cards
    #return a value based on card.cardVal as global #playerHandVal
    #Aces have their value reduced to 1 if player is over 21
    # global playerHandVal
    # def calcPlayerVal(hand):
    #     playerHandVal = 0
    #     #iterates through hand, adds cards to accumulator
    #     for card in hand:
    #         playerHandVal += card.cardVal
    #     #checks if hand valuue is over 21
    #     if playerHandVal > 21:
    #         #checks for aces (card.cardVal == 11)
    #         for card in hand:
    #             #if any aces present (AND val > 21), subtract 10 ; return new hand value
    #             if card.cardVal == 11:
    #                 playerHandVal -= 10
    #                 return playerHandVal
    #     #else return hand value
    #     return playerHandVal
    
    #CHECKHANDVAL
    #input int
    #if int > 21, hand is bust, game is over
    #returns playerBust() (ends game, play again?) 
    #or FALSE

    # def checkHandVal(val):
    #     if val > 21:
    #         return True
            
    #CALCDEALERHVAL
    #input hand
    #returns int based on dealer card values
    #helper function for gameplay loop
    # global dealerHandVal
    # def calcDealerVal(hand):
    #     dealerHandVal = 0
    #     for card in hand:
    #         dealerHandVal += card.cardVal
    #     if dealerHandVal > 21:
    #         for card in hand:
    #             if card.cardVal == 11:
    #                 dealerHandVal -= 10
    #                 return dealerHandVal
    #     return dealerHandVal

####PLAYER FUNCTIONS####
    
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
    def playerStand(playerHand, dealerHand):
        Action.dealerPlay(playerHand, dealerHand)

    #PLAYERBUST
    #ends game with a loss
    def playerBust(hand):
        print("You went bust with a value of " + str(Deck.calcHandVal(hand)))
        #modify to new game!!!
        exit()
    
    #PLAYERWIN
    #ends game with a win
    def playerWin(playerHand, dealerHand):
        print("Your value was", Deck.calcHandVal(playerHand))
        print("The dealer had a value of", Deck.calcHandVal(dealerHand))
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
        print("You have: ", end=""), Deck.printCards(playerHand), print(str(Deck.calcHandVal(playerHand)))
        if Deck.calcHandVal(playerHand) > 21:
            Action.playerBust(playerHand)
        print("Dealer is showing: ['" +Card.PrintCard(dealerHand[0]) + "', '**']"), print(str(dealerHand[0].cardVal))
        play = input("Would you like to: \n (H)it? \n (S)tand?").lower()
        if play == "s" or play == "stand":
            Action.playerStand(playerHand, dealerHand)
        if play == "h" or play == "hit":
            Action.playerDraw(playerHand)
            Action.playerPlay(playerHand, dealerHand)
        else:
            print("Please enter a valid input! \n")
            Action.playerPlay(playerHand, dealerHand)


####DEALER FUNCTIONS####


    #DEALERSTAND
    #ends dealer phase, moves to comparative phase #ENDPHASE
    def dealerStand(playerHand, dealerHand):
        Action.endPhase(playerHand, dealerHand)

    #DEALERHIT
    #adds card to dealerHand from dealerStack
    def dealerHit(playerHand, dealerHand):
        newCard = dealerStack.pop(0)
        dealerHand.append(newCard)
        print("Dealer draws ", Card.PrintCard(newCard))
        Action.dealerPlay(playerHand, dealerHand)

    #DEALERPLAY
    # input hand
    # output dealer hand value (or zero if bust)
    def dealerPlay(playerHand, dealerHand):
        print("You have: ", end=""), Deck.printCards(playerHand), print(str(Deck.calcHandVal(playerHand)))
        print("Dealer has "), Deck.printCards(dealerHand), print(str(Deck.calcHandVal(dealerHand)))
        if Deck.calcHandVal(dealerHand) > 21:
            print("Dealer busts!")
            Action.playerWin(playerHand, dealerHand)
        if Deck.calcHandVal(dealerHand) > 16:
            Action.dealerStand(playerHand, dealerHand)
        if Deck.calcHandVal(dealerHand) > 0:
            Action.dealerHit(playerHand, dealerHand)
        else:
            "Error in Action.dealerPlay, dealer value <= 0" ; exit()

    #ENDPHASE
    #input dealerHand and playerHand
    #compares values of hands and determines
    #winner or tie, with a message
    #ends program
    def endPhase(playerHand, dealerHand):
        print("Dealer has: ", str(Deck.calcHandVal(dealerHand)))
        print("Player has: ", str(Deck.calcHandVal(playerHand)))
        playerVal = Deck.calcHandVal(playerHand)
        dealerVal = Deck.calcHandVal(dealerHand)
        if int(playerVal) == int(dealerVal):
            print("It's a tie! Game over. \n"); exit()
        if int(playerVal) > int(dealerVal):
            print("You win! Game over. \n"); exit()
        if int(playerVal) < int(dealerVal):
            print("You lose! Game over. \n"); exit()
        

#GAMEPLAY START ###

# card3 = Card(5, "5", "hearts")
# card1 = Card(10, "3", "diamonds")
# card2 = Card(11, "4", "spades")
# cards  = [card1, card2, card3]

# print(Deck.calcHandVal(cards))



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
   