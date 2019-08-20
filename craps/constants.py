# from .bet import CrapsBet


# Game states
GAME_STARTED = 'GAME_STARTED'
GAME_IN_PROGRESS = 'GAME_IN_PROGRESS'
PLAYER_LOST = 'PLAYER_LOST'
PLAYER_WON = 'PLAYER_WON'

# Messages
WON_MESSAGE = 'You won. Do you want to keep playing?'
LOST_MESSAGE = 'You lost. Do you want to keep playing?'
BET_MESSAGE = 'Place a bet'
BET_PLACED = 'Your bet was placed successfully: '
INVALID_BET_TYPE = 'Invalid bet type'
OUT_OF_CASH = "You don't have enough money"
CAN_NOT_LEAVE = "You can't leave until the turn ends. "
INVALID_TURN_BET = "You can't make this bet in this turn"
# Bet States
BET_IN_PROGRESS = 'In progress'
BET_PAYED = 'Payed'
BET_LOST = 'Lost'

# Bet Names
PASS_BET = 'PASS_BET'
DO_NOT_PASS_BET = 'DO_NOT_PASS_BET'
DOUBLE_BET = 'DOUBLE_BET'
SEVEN_BET = 'SEVEN_BET'
CRAPS_BET = 'CRAPS_BET'

# Bet
# ONLY_START_BETS = [CrapsBet]
