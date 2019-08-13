from .exceptions.invalid_bet_exception import InvalidBetException


class StraightBet:
    def __init__(self, bet_value, ammount):
        self.reward = 35
        self.ammount = ammount
        self.bet_value = bet_value
        self.validate()

    def validate(self):
        ''' expect bet_value like "1" '''
        if not (0 <= self.bet_value <= 36):
            raise InvalidBetException('Invalid bet')


bet_types = {
    1: StraightBet,
}


class BetCreator:
    def create(self, bet_type, bet_value, ammount):
        bet = None
        if bet_type in bet_types:
            try:
                bet_class = bet_types[bet_type]
                bet = bet_class(bet_value, ammount)
            except InvalidBetException:
                print('Your bet value is invalid ')
        elif bet_type == 0:
            bet = 'END'
        else:
            bet = "Error, invalid bet"
        return bet

    @staticmethod
    def list_bets():
        pass
