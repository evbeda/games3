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

    def is_a_stair(self, dices):
        dices.sort()
        return (dices == [1, 2, 3, 4, 5] or dices == [2, 3, 4, 5, 6])

    def is_repeated(self, dices):
        return any(dices.count(x) >= 3 for x in dices)

    def check_combination(self, dices):
        if self.is_a_stair(dices):
            return (dices, 500)
        elif self.is_repeated(dices):
            return self.calculate_repeated(dices)
        else:
            return ([], 0)

    def calculate_repeated(self, dices):
        for dice in set(dices):
            if dices.count(dice) >= 3:
                qty = dices.count(dice)
                score = dice
                if (dice == 1):
                    if qty == 5:
                        return ([1]*qty, 10000)
                    else:
                        score *= 1000
                else:
                    score *= 100
                score *= 2 ** (qty-3)
                return ([dice]*qty, score)
        else:
            return ([], 0)
