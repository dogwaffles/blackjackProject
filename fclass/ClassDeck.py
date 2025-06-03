from classCard import Card


class Deck:
    def __init__(deck, deckLength):
        deck.deckLength = deckLength


    global decks
    decks = 1


    def deckNum(decks):
        return (decks * 52)
    
    def printHand(hand):
        currentHand = []
        for card in hand:
            cardIndex = hand.index(card)
            currentHand.append(hand[cardIndex])
        #I don't know why printCards needs to use Deck. here
        #I made a small effort to fix it...
        Deck.printCards(currentHand)

    # DECKMAKE
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

    global cardVals
    global cardFaces
    global cardSuits
    global aceVal
    aceVal = 1 #placeHolder
    cardVals = [aceVal,2,3,4,5,6,7,8,9,10,10,10,10]
    cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardSuits = ["spades", "hearts", "diamonds", "clubs"]

    #FIXME experimental, perhaps move to __str__ in class Card
    def printCards(deck):
        newDeck = []
        for card in deck:
            cardPrint = card.PrintCard()
            newDeck.append(cardPrint)
            # print(cardPrint)
        print(newDeck)

