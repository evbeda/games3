from .card import NumberCard
RED = 'red'
GREEN = 'green'
BLUE = 'blue'
YELLOW = 'yellow'
DRAW_CARD_INPUT = ''
EXIT = 'exit'
ASK_FOR_INPUT = \
    "Please select index of card to play! \n" + \
    "Or just press enter to draw a card \n" + \
    "(Type exit to quit) \n"
UNO_FINAL_LAST_PLAYED_CARD = NumberCard('red', 7)
UNO_FINAL_PLAYER_CARD = NumberCard('red', 9)
UNO_ALMOST_FINISHED_BOARD = "Your cards are: \n" +\
            "1: 9 - red\n" +\
            "The last card played is: \n" +\
            "7 - red"
UNO_FINISHED_BOARD = 'Your cards are: \nThe last card played is: \n9 - red'
