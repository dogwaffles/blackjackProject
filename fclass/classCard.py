# currentframe()
# for use in dynamic error reporting :)
from inspect import currentframe

cf = currentframe()

#class Card, to be imported for classic card games
# represents a single card, for math and nominal use 
#thanks to W3 school for the help learning this one.
class Card:
    def __init__(card, cardVal, cardFace, cardSuit):
        card.cardVal = cardVal #int - 1-10
        card.cardFace = cardFace #str - A, 2-10, J, Q, K
        card.cardSuit = cardSuit #str - spades, hearts, diamonds, clubs

    #needs refactoring
    #cardlist
    #FIXME
    aceVal = 1

    # cardList = [
    #     Card(aceVal, "A", "spades"),
    #     Card(2, "2", "spades"),
    #     Card(3, "3", "spades"),
    #     Card(4, "4", "spades"),
    #     Card(5, "5", "spades"),
    #     Card(6, "6", "spades"),
    #     Card(7, "7", "spades"),
    #     Card(8, "8", "spades"),
    #     Card(9, "9", "spades"),
    #     Card(10, "10", "spades"),
    #     Card(10, "jack", "spades"),
    #     Card(10, "queen", "spades"),
    #     Card(10, "king", "spades")]

    #values for card .cardVal .cardFace .cardSuit
    # cardVals = [aceVal,2,3,4,5,6,7,8,9,10,10,10,10]
    # cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # cardSuits = ["spades", "hearts", "diamonds", "clubs"]

    # for suit in cardSuits:
    #     for i in cardVals:
    #         print(Card(cardVals[i], cardFaces[i], cardSuits[suit]))

    #test loop to check card values, use existing functions, nested FOR loop
# for index, card in cardList.items():
#     print(card.cardFace) # + " : " + str(card["cardVal"]))

    # fn PRINTCARD uses print.cardFace and print.cardSuit
    # to print a card string for player display
    # there is probably a more elegant way to handle this series of ifs
    # if not any([]) produces false if any statement in the iterable returns true:
    # (skipping the error > exit())
    # local
    # Uses class reference when called ie card.checkCard()
    def checkCard(card):
        if not any([
            (card.cardSuit == "\u2660"),
            (card.cardSuit == "\u2665"),
            (card.cardSuit == "\u2666"),
            (card.cardSuit == "\u2663") ]):
            # triggers if none of the cardSuit ascii symbols are present in the card
            print("Error in PrintCard.py at ", cf, ". \n Ending program") ; exit()
        else:
            print(card.cardFace + card.cardSuit)
    # PRINTCARD
    # recieves a card, transforms that card into a graphic, based on its card.cardSuit
    # runs card.checkCard to check validity of entry and prints the cardSuit and cardFace
    def PrintCard(card):
        if card.cardSuit == "spades":
            card.cardSuit = "\u2660" #ascii graphics, tested well
        if card.cardSuit == "hearts":
            card.cardSuit = "\u2665"
        if card.cardSuit == "diamonds":
            card.cardSuit = "\u2666"
        if card.cardSuit == "clubs":
            card.cardSuit = "\u2663"
        # fixed: function call here is with class reference
        # NOT checkCard(card) 
        card.checkCard()


# DECK_GENERATE
#GENERATES A DECK, ITERATING THROUGH ALL SUITS, FACES, AND VALUES

    def deckMake():
        aceVal = 1
        cardVals = [aceVal,2,3,4,5,6,7,8,9,10,10,10,10]
        cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = ["spades", "hearts", "diamonds", "clubs"]
        for suitsIndex in range(len(cardSuits)):
            for facesIndex in range(len(cardFaces)):
                print(cardVals[facesIndex], cardFaces[facesIndex], cardSuits[suitsIndex])
 
    # deckMake()
 
    #test loop to check card values, use existing functions, nested FOR loop
    # for i in range(len(cardFaces)):
    #     # testCa
    #     print(cardFaces[i]) # + " : " + str(card["cardVal"]))
# class Card takes 3 values but returns 4 (self)
# self.cardVal = 7, self.cardFace = "7", etc.
#DEL
# card1 = Card(7, "7", "spades")



# # test function call #DEL
# card1.PrintCard()