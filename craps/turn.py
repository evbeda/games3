import random
from .constants import GAME_STARTED, GAME_IN_PROGRESS, PLAYER_LOST, PLAYER_WON


class Turn:
    def __init__(self):
        self.state = GAME_STARTED
        self.point = None
        self.bets = []

    def get_next_state(self, dice):
        losing_scores = [2, 3, 12]
        winning_scores = [7, 11]
        score = sum(dice)
        if self.state == GAME_STARTED:
            if score in losing_scores:
                return PLAYER_LOST
            if score in winning_scores:
                return PLAYER_WON
            return GAME_IN_PROGRESS
        if self.state == GAME_IN_PROGRESS:
            if score == self.point:
                return PLAYER_WON
            if score == 7:
                return PLAYER_LOST
            return GAME_IN_PROGRESS

    def shoot(self):
        # Throws two dice, returns their values and changes the state.
        self.dice = random.sample(range(1, 7), k=2)
        next_state = self.get_next_state(self.dice)
        self.state = next_state
        if not self.point and next_state == GAME_IN_PROGRESS:
            self.point = sum(self.dice)
        return tuple(self.dice)

    def check_bets(self, dice):
        activated_bets = []
        for bet in self.bets:
            if bet.check(self):
                activated_bets.append(bet)
        self.bets = [
            bet
            for bet in self.bets
            if bet not in activated_bets]
        return activated_bets

    def pay_bets(self, dice):
        activated_bets = self.check_bets(dice)
        amount = 0
        for bet in activated_bets:
            amount += bet.pay(self)
        return amount
