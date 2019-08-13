import random
from constants import GAME_STARTED, GAME_IN_PROGRESS, PLAYER_LOST, PLAYER_WON


class Turn:
    def __init__(self):
        self.state = GAME_STARTED

    def get_next_state(self, dice):
        losing_scores = [2, 3, 12]
        winning_scores = [7, 11]
        score = sum(dice)
        if self.state == GAME_STARTED:
            if score in losing_scores:
                return PLAYER_LOST
            elif score in winning_scores:
                return PLAYER_WON
            else:
                return GAME_IN_PROGRESS

    def shoot(self):
        """Throws the dice, returns their values and changes the state."""
        dice = random.sample(range(1, 7), k=2)
        self.state = self.get_next_state(dice)
        return tuple(dice)
