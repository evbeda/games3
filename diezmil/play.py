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

    def check_combination(self, dices):
        total_score = 0
        dices.sort()
        stair = (dices == [1, 2, 3, 4, 5] or dices == [2, 3, 4, 5, 6])
        if stair:
            total_score += 500
            return total_score
        unique_dices = set(dices)
        for i in unique_dices:
            quantity = dices.count(i)
            if i == 1 and quantity >= 3:
                total_score += 1000
                quantity -= 3
            elif quantity >= 4:
                total_score += i*100*2
                quantity -= 4
            elif quantity == 3:
                total_score += i*100
                quantity -= 3
            if i == 1:
                total_score += 100 * quantity
            elif i == 5:
                total_score += 50 * quantity

        return total_score
