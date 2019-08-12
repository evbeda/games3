

class Bet:
    def __init__(self, bet_type, numbers, ammount):
        bet = None
        if(bet_type == 1 and StraightBet.validate_straight(numbers)):
            bet = StraightBet(numbers, ammount)
        return bet


class StraightBet:
    def __init__(self, number, ammount):
        self.reward = 35
        self.ammount = ammount

    def validate_straight(number):
        if 0 <= number and number <= 36:
            return True
        else:
            return False
        