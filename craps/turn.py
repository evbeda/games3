import random
from .constants import GAME_STARTED, GAME_IN_PROGRESS, PLAYER_LOST, PLAYER_WON


class Turn:
    def __init__(self):
        self.state = GAME_STARTED
        self.point = None

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
        elif self.state == GAME_IN_PROGRESS:
            if score == self.point:
                return PLAYER_WON
            elif score == 7:
                return PLAYER_LOST
            else:
                return GAME_IN_PROGRESS

    def shoot(self):
        # Throws two dice, returns their values and changes the state.
        dice = random.sample(range(1, 7), k=2)
        next_state = self.get_next_state(dice)
        self.state = next_state
        if not self.point and next_state == GAME_IN_PROGRESS:
            self.point = sum(dice)
        return tuple(dice)

    # not tested
    def check_bets(self, bets, dice):
        activated_bets = []
        for bet in bets:
            if bet.check(self, dice):
                activated_bets.append(bet)
        return activated_bets
