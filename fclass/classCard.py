# currentframe()
# for use in dynamic error reporting :)
from inspect import currentframe

cf = currentframe()

# class Card, to be imported for classic card games
# represents a single card, for math and nominal use 
# thanks to W3 school for the help learning this one.
class Card:
    def __init__(card, cardVal, cardFace, cardSuit):
        card.cardVal = cardVal #int - 1-10
        card.cardFace = cardFace #str - A, 2-10, J, Q, K
        card.cardSuit = cardSuit #str - spades, hearts, diamonds, clubs

    # SUITTRANSFORM
    # inputs Card {spades, hearts, diamonds, clubs}
    # outputs appropriate string ascii symbol to represent suit in playspace
    # def suitTransform(card):
    #     if card.cardSuit == "spades":
    #         card.cardSuit = "\u2660" #ascii graphics, tested well
    #     if card.cardSuit == "hearts":
    #         card.cardSuit = "\u2665"
    #     if card.cardSuit == "diamonds":
    #         card.cardSuit = "\u2666"
    #     if card.cardSuit == "clubs":
    #         card.cardSuit = "\u2663"
    #     return card.cardsuit

    # PRINTCARD
    # inputs Card
    # outputs [] string cardFace string cardSuit in play space
    # transforming suit string into ascii symbol
    # calls exit() if suit check is invalid
    def PrintCard(card):
        # changes string .cardSuit into ascii character
        # I tried turning this into a helper function (and may return to it later)
        #FIXME
        if card.cardSuit == "spades":
            card.cardSuit = "\u2660" #ascii graphics, tested well
        if card.cardSuit == "hearts":
            card.cardSuit = "\u2665"
        if card.cardSuit == "diamonds":
            card.cardSuit = "\u2666"
        if card.cardSuit == "clubs":
            card.cardSuit = "\u2663"
        # if a valid string is not present, exits program with error message
        if not any([
            (card.cardSuit == "\u2660"),
            (card.cardSuit == "\u2665"),
            (card.cardSuit == "\u2666"),
            (card.cardSuit == "\u2663") ]):
            print("Error in PrintCard.py at ", cf, ". \n Ending program") ; exit()
        else:
            return (card.cardFace + card.cardSuit)
