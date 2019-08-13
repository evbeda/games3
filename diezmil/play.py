import random 


class Play(object):
    def __init__(self):
        self.play_score = None
        self.dices = []

    def play_dices(self, dice_qty):
        if dice_qty > 5:
            return False
        for j in range(dice_qty):
            self.dices.append(random.randint(1, 6))

    def check_combination(self, play):
        total_score = 0
        is_repeated = False
        play.sort()
        if play == [1, 2, 3, 4, 5]:
            total_score += 500
            return total_score
        for i in play:
            quantity = play.count(i)
            if i == 1:
                total_score += 100
            elif i == 5:
                total_score += 50
            if quantity == 4 and is_repeated is False:
                total_score += i*100*2
                is_repeated = True
            if quantity == 3 and is_repeated is False:
                total_score += i*100
                is_repeated = True

        return total_score
