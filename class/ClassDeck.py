from ClassCard import Card

#try_2
class Deck:
    def __init__(deck, deckLength):
        deck.deckLength = deckLength

    def deckMake(deck):
        print(list(range(1, 52)))

newDeck = Deck(52)
    
newDeck.deckMake()



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
    
