import random


class Play(object):
    def __init__(self):
        self.play_score = 0
        self.dices = []
        self.selected_dices = []
        self.is_playing = True
        self.play_temp_score = 0

    def roll_dices(self, dice_qty):
        if dice_qty > 5:
            return False
        for j in range(dice_qty):
            self.dices.append(random.randint(1, 6))
        self.dices.sort()
        self.check_combination(self.dices)

    def select_dices(self, selected_dices_positions):
        # self.selected_dices += self.dices[selected_dices_positions]
        # print(self.selected_dices)
        for position in selected_dices_positions:
            self.selected_dices.append(self.dices[position])
        self.play_score = self.check_combination(self.selected_dices)[1]
        self.is_playing = False

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
        if self.is_a_stair(dices):
            self.play_temp_score = 500
            return (dices, 500)
        elif self.is_repeated(dices):
            self.play_temp_score = self.calculate_repeated(dices)[1]
            return self.calculate_repeated(dices)
        else:
            self.play_temp_score = self.calculate_individual_values(dices)[1]
            return self.calculate_individual_values(dices)

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
