from classAction import Action

class Game:
    def __init__(self, numDecks):
        Game.numDecks = numDecks

    
    # GAME CODE


    #STARTDEAL 
    # starts the game
    # creates a dealer stack
    # deals two cards each to player and dealer
    # saves hands as playerHand and dealerHand
    # dealerStack can be modified with input option numDecks
    global dealerCurrentHand
    dealerCurrentHand = []
    def startDeal():
        Action.dealerStack
        dealerCurrentHand = Action.dealerDeal()
        playerHand = Action.playerDeal()

    print(dealerCurrentHand)
        