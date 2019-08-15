from .turn import Turn
from .bet import BetCreator
from .exceptions.invalid_bet_exception import InvalidBetTypeException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
    BET_PLACED,
    INVALID_BET_TYPE
)


class CrapsGame:

    name = 'Craps Game'
    # input_args = 1

    def __init__(self):
        self.turn = Turn()
        self.is_playing = True
        self.bets = []

    def next_turn(self):
        if self.turn.state == PLAYER_LOST:
            return LOST_MESSAGE
        elif self.turn.state == PLAYER_WON:
            return WON_MESSAGE
        return BET_MESSAGE

    def play(self, user_input):
        if user_input == 'No':
            self.is_playing = False
            return 'Game Over'
        elif user_input == 'Go':
            turn_score = self.turn.shoot()
            return turn_score
        else:
            try:
                bet_type, amount, bet_values = self.resolve_command(user_input)
                bet = BetCreator.create(bet_type, amount, bet_values)
                self.bets.append(bet)
                return BET_PLACED + bet_type
            except InvalidBetTypeException:
                return INVALID_BET_TYPE

    # command like
    # BETNAME amount dice_options
    def resolve_command(self, command):
        list_string = command.split()
        bet_type = list_string[0]
        amount = int(list_string[1])
        bet_values = [int(number) for number in list_string[2:]]
        if len(bet_values) > 2:
            bet_values = bet_values[0:2]
        return (bet_type, amount, bet_values)

    # @property
    # def board(self):
    #     return self.turn.point
