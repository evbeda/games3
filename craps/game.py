from .turn import Turn
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
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
            pass
            # input bet

    # @property
    # def board(self):
    #     return self.turn.point
