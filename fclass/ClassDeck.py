from classCard import Card


class Deck:
    def __init__(deck, deckLength):
        deck.deckLength = deckLength
    
    global decks
    decks = 1
    
    def deckNum(decks):
        return (decks * 52)

    # DECKMAKE
    # returns a full deck of 52 class Card
    def deckMake():
        # variables for function
        aceVal = 1 #placeHolder
        cardVals = [aceVal,2,3,4,5,6,7,8,9,10,10,10,10]
        cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = ["spades", "hearts", "diamonds", "clubs"]
        newDeck = []
        # nested for loop, iterates through suits, faces,values
        # appends each Card into newDeck
        for suitsIndex in range(len(cardSuits)):
            for facesIndex in range(len(cardFaces)):
                newDeck.append(Card(cardVals[facesIndex], cardFaces[facesIndex], cardSuits[suitsIndex]))
        return newDeck

    #FIXME experimental, perhaps move to __str__ in class Card
    def printCards(deck):
        newDeck = []
        for card in deck:
            cardPrint = card.PrintCard()
            newDeck.append(cardPrint)
            # print(cardPrint)
        print(newDeck)

    # def makeDealerStack(decks):
    #     deckStack = []
    #     newDeck = Deck.deckMake()
    #     while decks > 0:
    #         # print(decks) #DEL
    #         deckStack += newDeck
    #         decks -= 1
    #     return deckStack

# newDeck = Deck(deckLength)
    
    # deck1 = deckMake()
    # printStack(deck1)
    




# try_1
# def deckMake():
    # #aceVal is placeholder
    # aceVal = 1
    # newDeck = []
    # cardVals = [aceVal,2,3,4,5,6,7,8,9,10,10,10,10]
    # cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # cardSuits = ["spades", "hearts", "diamonds", "clubs"]
    # for suitsIndex in range(len(cardSuits)):
    #     for facesIndex in range(len(cardFaces)):
    #         newDeck.append([cardVals[facesIndex], cardFaces[facesIndex], cardSuits[suitsIndex]])
    # print(list(newDeck))
            # newCard = [cardVals[facesIndex], (Card.cardFaces[facesIndex]), (Card.cardSuits[suitsIndex])]
            # print(newCard)
            # newDeck.append(newCard)
            # print(newDeck)
    
# print
# deck1 = deckMake()
    
