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
UNO_FINAL_COMPUTER_CARD = [NumberCard('red', 9), NumberCard('green', 8)]
UNO_ALMOST_FINISHED_BOARD = '''Your cards are:
1: 9 - red
Computer remaining cards: 2
The last card played is:
7 - red'''

UNO_FINISHED_BOARD = '''Your cards are:

Computer remaining cards: 2
The last card played is:
9 - red'''

EXIT_MESSAGE = 'Bye!'

INVALID_CARD_MESSAGE = "Invalid card."

FINISHED_PLAY_MESSAGE = ""
