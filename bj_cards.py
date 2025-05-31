
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
   

