from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException

all_values = list(range(37))


class Bet:
    # reward = 0

    def __init__(self, bet_value, ammount):
        self.ammount = ammount
        self.target_numbers = bet_value

    def is_winner(self, chosen_number):
        return chosen_number in self.target_numbers

    def calculate_total_award(self, chosen_number):
        if self.is_winner(chosen_number):
            return self.reward * self.ammount
        else:
            return 0


class StraightBet(Bet):
    name = 'STRAIGHT_BET\n'
    reward = 35

    def __init__(self, bet_value, ammount):
        self.ammount = ammount
        self.target_numbers = bet_value
        self.validate(bet_value[0])

    def validate(self, bet_value):
        ''' expect bet_value like "1" '''
        if not (0 <= bet_value <= 36):
            raise InvalidBetException()


class ColorBet(Bet):
    name = 'COLOR_BET\n'
    reward = 2

    def __init__(self, bet_value, ammount):
        self.validate(bet_value[0])
        self.ammount = ammount
        self.target_numbers = \
            self.transform_bet_value_to_target_values(bet_value)

    def transform_bet_value_to_target_values(self, bet_value):
        range_1 = [number for number in all_values if number in range(1, 11)
                   and number % 2 == 1]
        range_2 = [number for number in all_values if number in range(19, 29)
                   and number % 2 == 1]
        range_3 = [number for number in all_values if number in range(11, 19)
                   and number % 2 == 0]
        range_4 = [number for number in all_values if number in range(29, 37)
                   and number % 2 == 0]
        red = range_1 + range_2 + range_3 + range_4
        if bet_value[0].lower() == 'red':
            return red
        else:
            return list(set(all_values) - set(red))

    def validate(self, bet_value):
        ''' expect bet_value like "Red" or "Black" '''
        if bet_value.lower() not in ['red', 'black']:
            raise InvalidBetException()


class EvenOddBet(Bet):
    name = 'EVEN_ODD_BET\n'
    reward = 2
    # to do same as in ColorBet

    def __init__(self, bet_value, ammount):
        self.validate(bet_value[0])
        self.ammount = ammount
        self.target_numbers = \
            self.transform_bet_value_to_target_values(bet_value)

    def validate(self, bet_value):
        ''' expect bet_value like "Even" or "Odd" '''
        if bet_value[0].lower() not in ['even', 'odd']:
            raise InvalidBetException()

    def transform_bet_value_to_target_values(self, bet_value):
        odd = [n for n in all_values if n % 2 == 1]
        if bet_value[0].lower() == 'odd':
            return odd
        else:
            return list(set(all_values) - set(odd))


bet_types = {
    'STRAIGHT_BET': StraightBet,
}


class BetCreator:

    def create(bet_type, bet_values, ammount):
        bet = None
        bet_class = bet_types[bet_type]  # obtain bet Class from dictionary
        bet = bet_class(bet_values, ammount)
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
