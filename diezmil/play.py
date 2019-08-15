import random


class Play(object):
    def __init__(self):
        self.play_score = None
        self.dices = []
        self.is_playing = True

    def play_dices(self, dice_qty):
        if dice_qty > 5:
            return False
        for j in range(dice_qty):
            self.dices.append(random.randint(1, 6))
        return self.dices

    def calculate_individual_values(self, dices):
        total_score = 0
        total_score += dices.count(5) * 50
        total_score += dices.count(1) * 100
        return total_score

