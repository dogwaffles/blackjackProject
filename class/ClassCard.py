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

    # fn PRINTCARD uses print.cardFace and print.cardSuit
    # to print a card string for player display
    # (I tried making another  function to insert into this function, but I recieved that NoneType error...)
    # there is probably a more elegant way to handle this if
    # if not any([]) produces false if any statement in the iterable returns true
    # (skipping the error > exit())
    # local
    # Uses class reference when called ie card.checkCard()
    def checkCard(card):
        if not any([
            (card.cardSuit == "\u2660"),
            (card.cardSuit == "\u2665"),
            (card.cardSuit == "\u2666"),
            (card.cardSuit == "\u2663") ]):
            # error handling with debug information, cf is currentframe() from inspect library
            # triggers if none of the cardSuit ascii symbols are present in the card
            print("Error in PrintCard.py at ", cf, ". \n Ending program") ; exit()
        else:
            print(card.cardFace + card.cardSuit)

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

# class Card takes 3 values but returns 4 (self)
# self.cardVal = 7, self.cardFace = "7", etc.
#DEL
card1 = Card(7, "7", "spades")

# test function call #DEL
card1.PrintCard()
