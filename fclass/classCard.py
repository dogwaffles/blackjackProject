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
    # helper function for PRINTCARD
    # inputs Card 
    # uses Card.cardSuit to determine new symbol
    # returns appropriate string ascii symbol to represent suit in playspace
    def suitTransform(card):
        if card.cardSuit == "spades":
            card.cardSuit = "\u2660" #ascii graphics, tested well
        if card.cardSuit == "hearts":
            card.cardSuit = "\u2665"
        if card.cardSuit == "diamonds":
            card.cardSuit = "\u2666"
        if card.cardSuit == "clubs":
            card.cardSuit = "\u2663"
        return card.cardSuit
    
    # SUITCHECK
    # helper for PRINTCARD
    # input str suit
    # exits program if suit is outside of allowed
    def suitCheck(suit):
        if not any([
            (suit == "\u2660"),
            (suit == "\u2665"),
            (suit == "\u2666"),
            (suit == "\u2663") ]):
            print("Error in ClassCard.py at ", cf, " \n Ending program") ; exit()       

    # PRINTCARD
    # inputs Card
    # outputs str .cardFace str .cardSuit in playspace
    # str .cardSuit is transformed into appropriate ascii symbol in SUITTRANSFORM
    # calls exit() if suit check is invalid
    def PrintCard(card):
        # changes str .cardSuit into str ascii 'newSuit'
        newSuit = Card.suitTransform(card)
        # checks for validity of newSuit, exits otherwise
        Card.suitCheck(newSuit)
        # returns str data for playspace
        # NOTE: this will change the card global, but that shouldn't matter
        return (card.cardFace + card.cardSuit)

card1 = Card(3, "3", "diamonds")
card2 = Card(4, "4", "spades")
cards  = [card1, card2]
print(Card.PrintCard(cards[1]))