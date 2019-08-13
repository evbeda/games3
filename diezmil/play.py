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
        is_repeated = False
        dices.sort()
        if dices == [1, 2, 3, 4, 5]:
            total_score += 500
            return total_score
        for i in dices:
            quantity = dices.count(i)
            if i == 1:
                total_score += 100
            elif i == 5:
                total_score += 50
            if quantity == 4 and is_repeated is False:
                total_score += i*100*2
                is_repeated = True
            #Missing: calculate score when rolling five 1 s  (should return: 1200) or five 5 s (should return: 1050) 
            #
            if quantity == 3 and is_repeated is False:
                if i == 1:
                    total_score += 1000
                else:
                    total_score += i*100
                is_repeated = True
                
        return total_score
