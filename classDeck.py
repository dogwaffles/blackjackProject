from classCard import Card


class Deck:
    def __init__(deck, deckLength):
        deck.deckLength = deckLength

    # number of decks - eventually will be user-defined
    global decks
    decks = 1

    # input number of decks
    # output number of cards (decks * 52)
    def deckNum(decks):
        return (decks * 52)
    

    def calcHandVal(hand):
        handVal = 0
        #iterates through hand, adds cards to accumulator
        for card in hand:
            handVal += card.cardVal
        #checks if hand valuue is over 21
        if handVal > 21:
            #checks for aces (card.cardVal == 11)
            for card in hand:
                #if any aces present (AND val > 21), subtract 10 ; return new hand value
                if card.cardVal == 11:
                    handVal -= 10
                    return handVal
        #else return hand value
        return handVal

    # input array of class Card
    # output array of string for playspace
    def printCards(deck):
        newDeck = []
        for card in deck:
            #PrintCard uses 2 Card attributes and stringifies them
            cardPrint = card.PrintCard()
            newDeck.append(cardPrint)
        print(newDeck)


    # returns a full deck of 52 class Card
    def deckMake():
        # variables for function
        newDeck = []
        # nested for loop, iterates through suits, faces,values
        # appends each Card into newDeck
        for suitsIndex in range(len(cardSuits)):
            for facesIndex in range(len(cardFaces)):
                newDeck.append(Card(cardVals[facesIndex], cardFaces[facesIndex], cardSuits[suitsIndex]))
        return newDeck

    # used in deckMake() DO NOT DELETE
    global aceVal
    global cardVals
    global cardFaces
    global cardSuits
    aceVal = 1 #placeHolder
    cardVals = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardSuits = ["spades", "hearts", "diamonds", "clubs"]


