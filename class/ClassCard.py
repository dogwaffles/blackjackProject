# for use in dynamic error reporting :)
from inspect import currentframe

cf = currentframe()

#class Card, to be imported for classic card games
#thanks to W3 school for the help with this one.
class Card:
    def __init__(self, cardVal, cardFace, cardSuit):
        self.cardVal = cardVal #int - 1-10
        self.cardFace = cardFace #str - A, 2-10, J, Q, K
        self.cardSuit = cardSuit #str - spades, hearts, diamonds, clubs


# fn PRINTCARD uses self.cardFace and self.cardSuit
# to print a card string for player display
# (I tried making another  function to insert into this function, but I recieved that NoneType error...)
# (... which I guess is some kind of scope error. This is a good result for my first session.)
    def PrintCard(self):
        if self.cardSuit == "spades":
            self.cardSuit = "\u2660" #ascii graphics, tested well0
        if self.cardSuit == "hearts":
            self.cardSuit = "\u2665"
        if self.cardSuit == "diamonds":
            self.cardSuit = "\u2666"
        if self.cardSuit == "clubs":
            self.cardSuit = "\u2663"
        # there is probably a more elegant way to handle this elif
        elif (self.cardSuit != "\u2660") | (self.cardSuit != "\u2665") | (self.cardSuit != "\u2666") | (self.cardSuit != "\u2663"):
            # error handling with debug information, cf is currentframe() from inspect
            print("Error in PrintCard at ", cf, ". \n Ending program") ; exit()
        print(self.cardFace + self.cardSuit)

# class Card takes 3 values but returns 4 (self)
# self.cardVal = 7, self.cardFace = "7", etc.
#DEL
card1 = Card(7, "7", "fdsa")

# test function call #DEL
card1.PrintCard()
