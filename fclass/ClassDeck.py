from ClassCard import Card

# general functions

#DECKNUM
#accepts a number of decks
#returns a number of cards in that many decks (decks * 52)

# general variables


#DEL    
# deckLength = 1
# deckLength = deckNum(deckLength)
# print(deckLength)


#try_2
class Deck:
    def __init__(deck, deckLength):
        deck.deckLength = deckLength
    
    def deckNum(decks):
        return (decks * 52)

    # def deckMake(deck):
    #     print(list(range(1, deck.deckLength + 1)))
    def deckMake():
        #aceVal is placeholder
        aceVal = 1 #placeHolder
        cardVals = [aceVal,2,3,4,5,6,7,8,9,10,10,10,10]
        cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = ["spades", "hearts", "diamonds", "clubs"]
        newDeck = []
        for suitsIndex in range(len(cardSuits)):
            for facesIndex in range(len(cardFaces)):
                newDeck.append([cardVals[facesIndex], cardFaces[facesIndex], cardSuits[suitsIndex]])
        return newDeck
        # print(list(newDeck))
            #         newCard = [cardVals[facesIndex], (Card.cardFaces[facesIndex]), (Card.cardSuits[suitsIndex])]
            #         print(newCard)
            #         newDeck.append(newCard)
            #         print(newDeck)



# newDeck = Deck(deckLength)
    
    # print(deckMake())
    

# # from cardClass (WORKS)
# card1 = Card(7, "7", "spades")

# # test function call #DEL
# card1.PrintCard()


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
    
