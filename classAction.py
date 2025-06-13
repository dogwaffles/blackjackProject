from classDeck import Deck
from classCard import Card
# from classHand import Hand
from random import shuffle

printCards = Deck.printCards
# print(dealerStack[0])

class Action:
    def __init__(deal, numCards):
        Action.numCards = numCards

    

    #global is useful here so functions can modify variables
    global dealerStack
    from classHand import dealerStack
    # dealerStack = Hand.makeDealerStack(1)
    # shuffle(dealerStack)

            

####PLAYER FUNCTIONS####
    
    #PLAYERDRAW
    #accepts a list (playerCurrentHand)
    #appends a card from dealerStack(.pop)
    def playerDraw(hand):
        
        newCard = dealerStack.pop(0)
        print("\nYou drew a ", Card.PrintCard(newCard))
        hand.append(newCard)
        return hand

    #PLAYERSTAND
    #ends player turn (moves to dealer turn)
    def playerStand(playerHand, dealerHand):
        print("\nYou stand with " + str(Deck.calcHandVal(playerHand))+ "\n")
        Action.dealerPlay(playerHand, dealerHand)

    #PLAYERBUST
    #ends game with a loss
    def playerBust(hand):
        print("You went bust with a value of " + str(Deck.calcHandVal(hand)))
        print("Game over. You lose.\n")
        #modify to new game!!!
        exit()
    
    #PLAYERWIN
    #ends game with a win
    def playerWin(playerHand, dealerHand):
        print("Your value was", Deck.calcHandVal(playerHand))
        print("The dealer had a value of\n", Deck.calcHandVal(dealerHand))
        print("You win!\n")
        #!!!
        exit()


    #PLAYERPLAY
    #while game is active
    #modifies hand based on player action
    #takes input and modifies player hand accordingly
        #hit - add a card
        #stand - end turn
        #double - double bet, add a card #!!!
        #split - splits into two hands #!!!
    def playerPlay(playerHand, dealerHand):
        # announces current hand and hand value
        print("\nYou have: ", end=""), Deck.printCards(playerHand)
        if Deck.calcHandVal(playerHand) > 21:
            Action.playerBust(playerHand)
        print("Dealer is showing: ['" +Card.PrintCard(dealerHand[0]) + "', '**']\n")
        print("Player value: ",str(Deck.calcHandVal(playerHand)))
        print("Dealer shows: ",str(dealerHand[0].cardVal), "\n")
        play = input("Would you like to: \n (H)it? \n (S)tand? \n").lower()
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
        print("Dealer stands with ", Deck.calcHandVal(dealerHand), "\n")
        Action.endPhase(playerHand, dealerHand)

    #DEALERHIT
    #adds card to dealerHand from dealerStack
    def dealerHit(playerHand, dealerHand):
        newCard = dealerStack.pop(0)
        dealerHand.append(newCard)
        print("\nDealer draws ", Card.PrintCard(newCard), "\n")
        Action.dealerPlay(playerHand, dealerHand)

    #DEALERPLAY
    # input hand
    # output dealer hand value (or playerWin() if bust)
    # dealer play is deterministic
    def dealerPlay(playerHand, dealerHand):
        print("You have: ", end=""), Deck.printCards(playerHand)
        print("Dealer has: ", end=""), Deck.printCards(dealerHand), print("")
        print("Player value: ",str(Deck.calcHandVal(playerHand)))
        print("Dealer value: ",str(Deck.calcHandVal(dealerHand)), "\n")
        if Deck.calcHandVal(dealerHand) > 21:
            print("Dealer busts!\n")
            Action.playerWin(playerHand, dealerHand)
        if Deck.calcHandVal(dealerHand) > 16:
            Action.dealerStand(playerHand, dealerHand)
        input("Press enter to continue.\n")
        if Deck.calcHandVal(dealerHand) > 0:
            Action.dealerHit(playerHand, dealerHand)
        else:
            "Error in Action.dealerPlay, dealer value <= 0" ; exit()

    ###ENDPHASE
    #input dealerHand and playerHand
    #compares values of hands and determines
    #winner or tie, with a message
    #ends program
    def endPhase(playerHand, dealerHand):
        print("Player has: ", end=""), Deck.printCards(playerHand)
        print("Dealer has: ", end=""), Deck.printCards(dealerHand), print("")
        print("Player value: ",str(Deck.calcHandVal(playerHand)))
        print("Dealer value: ",str(Deck.calcHandVal(dealerHand)), "\n")
        playerVal = Deck.calcHandVal(playerHand)
        dealerVal = Deck.calcHandVal(dealerHand)
        if int(playerVal) == int(dealerVal):
            print("It's a tie! Game over. \n"); exit()
        if int(playerVal) > int(dealerVal):
            print("You win! Game over. \n"); exit()
        if int(playerVal) < int(dealerVal):
            print("You lose! Game over. \n"); exit()


###TEST CODE###