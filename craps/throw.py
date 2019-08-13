import random
from constants import GAME_IN_PROGRESS


class Throw:
    def __init__(self, game):
        self.game = game

    def shoot(self):
        """Throws the dice and return their values."""
        dice = random.sample(range(1, 7), k=2)
        return tuple(dice)

    def change_game_state(self, dice):
        """Changes game state based on dice values."""
        self.game.state = GAME_IN_PROGRESS
