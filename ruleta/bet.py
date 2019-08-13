

class BetCreator:
    def create(self, bet_type, numbers, ammount):
        bet = None
        if(bet_type == 1):
            if(StraightBet.validate_straight(numbers)):
                bet = StraightBet(numbers, ammount)
            else:
                bet = "Error, invalid bet"
        return bet


class StraightBet:
    def __init__(self, number, ammount):
        self.reward = 35
        self.ammount = ammount

    @staticmethod
    def validate_straight(number):
        if 0 <= number and number <= 36:
            return True
        else:
            return False
        