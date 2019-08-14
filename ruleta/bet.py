from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException


class StraightBet:
    name = 'STRAIGHT_BET\n'

    def __init__(self, bet_value, ammount, player):
        self.reward = 35
        self.ammount = ammount
        self.bet_value = bet_value[0]
        self.validate()
        self.player = player

    def validate(self):
        ''' expect bet_value like "1" '''
        if not (0 <= self.bet_value <= 36):
            raise InvalidBetException()

    def calculate_total_award(self):
        return self.reward * self.ammount

    def win_bet(self, chosen_number):
        if chosen_number == self.bet_value:
            self.player.money += self.calculate_total_award()


bet_types = {
    'STRAIGHT_BET': StraightBet,
}


class BetCreator:
    def create(self, bet_type, bet_values, ammount, player):
        bet = None
        bet_class = bet_types[bet_type]  # obtain bet Class from dictionary
        bet = bet_class(bet_values, ammount, player)
        return bet

    def validate_bet_type(bet_type):
        if bet_type not in bet_types:
            raise InvalidBetTypeException()

    @staticmethod
    def list_bets():
        menu = ''
        for bet in bet_types:
            menu += bet.name
        return menu
