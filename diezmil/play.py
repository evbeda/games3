import random
from . import WINNING_PLAY
from .exceptions.exceptions import PlayRemainsWithNoScore


class Play(object):
    def __init__(self):
        self.play_score = 0
        self.dices = []
        self.is_playing = True

    def roll_dices(self, dice_qty):
        if dice_qty > 5:
            return False
        for j in range(dice_qty):
            self.dices.append(random.randint(1, 6))
        self.dices.sort()
        self.play_score = self.check_combination(self.dices)

    def choose_dices(self, selected_dices_positions):
        return [
            value
            for position, value in enumerate(self.dices)
            if position in selected_dices_positions
        ]

    def select_dices(self, selected_dices_positions):
        reminders = len(self.dices) - len(selected_dices_positions)
        choosen_dices = self.choose_dices(selected_dices_positions)
        play_score = self.check_combination(choosen_dices)
        # you can't keep dices with 0 points
        if play_score == 0:
            raise PlayRemainsWithNoScore
        self.dices = choosen_dices
        self.play_score = play_score
        self.is_playing = False
        return reminders

    def calculate_individual_values(self, dices):
        total_score = 0
        total_score += dices.count(5) * 50 + dices.count(1) * 100
        ones = [i for i in dices if i == 1]
        fives = [i for i in dices if i == 5]
        return ones + fives, total_score

    def is_a_stair(self, dices):
        dices.sort()
        return (dices == [1, 2, 3, 4, 5] or dices == [2, 3, 4, 5, 6])

    def is_repeated(self, dices):
        return any(dices.count(x) >= 3 for x in dices)

    def check_combination(self, dices):
        total_score = 0
        if dices == [1, 1, 1, 1, 1]:
            return WINNING_PLAY
        if self.is_a_stair(dices):
            return 500
        elif self.is_repeated(dices):
            total_score = self.calculate_repeated(dices)[1]
            dices = [
                dice for dice in dices
                if dice not in self.calculate_repeated(dices)[0]
            ]
            total_score += self.calculate_individual_values(dices)[1]
            return total_score
        total_score = self.calculate_individual_values(dices)[1]
        return total_score

    def calculate_repeated(self, dices):
        for dice in set(dices):
            if dices.count(dice) >= 3:
                qty = dices.count(dice)
                score = dice
                if (dice == 1):
                    score *= 1000
                else:
                    score *= 100
                score *= 2 ** (qty-3)
                return ([dice]*qty, score)
        else:
            return ([], 0)

    def __str__(self):
        ret = f'Dices: {self.dices}\n'
        ret += f'Play score {self.play_score}\n'
        return ret
