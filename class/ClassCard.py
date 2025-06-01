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

#cardlist
#may be useful

aceVal = 1

card_dict = {
    0: {"cardName":"Joker", "cardVal":0},
    1: {"cardName":"Ace", "cardVal":aceVal},
    2: {"cardName":"Two", "cardVal":2},
    3: {"cardName":"Three", "cardVal":3},
    4: {"cardName":"Four", "cardVal":4},
    5: {"cardName":"Five", "cardVal":5},
    6: {"cardName":"Six", "cardVal":6},
    7: {"cardName":"Seven", "cardVal":7},
    8: {"cardName":"Eight", "cardVal":8},
    9: {"cardName":"Nine", "cardVal":9},
    10: {"cardName":"Ten", "cardVal":10},
    11: {"cardName":"Jack", "cardVal":10},
    12: {"cardName":"Queen", "cardVal":10},
    13: {"cardName":"King", "cardVal":10}
}

for index, card in card_dict.items():
    print(card["cardName"] + " : " + str(card["cardVal"]))

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
            # error handling with debug information, cf is currentframe() from inspect library
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

# class Card takes 3 values but returns 4 (self)
# self.cardVal = 7, self.cardFace = "7", etc.
#DEL
card1 = Card(7, "7", "spades")

# test function call #DEL
card1.PrintCard()
