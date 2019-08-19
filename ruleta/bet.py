from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .board import board

all_values = list(range(1, 37))


class Bet:
    # reward = 0

    def __init__(self, bet_value, amount):
        self.validate(bet_value)
        self.target_numbers = \
            sorted(self.transform_bet_values_to_target_values(bet_value))
        self.amount = amount

    def transform_bet_values_to_target_values(self, bet_value):
        return bet_value

    def is_winner(self, chosen_number):
        return chosen_number in self.target_numbers

    def calculate_award(self, chosen_number):
        if self.is_winner(chosen_number):
            return self.reward * self.amount
        else:
            return 0


class StraightBet(Bet):
    name = 'STRAIGHT_BET\n'
    reward = 35

    def __init__(self, bet_value, amount):
        super().__init__(bet_value, amount)

    def validate(self, bet_value):
        ''' expect bet_value like "1" '''
        if not (0 <= bet_value[0] <= 36):
            raise InvalidBetException()


class ColorBet(Bet):
    name = 'COLOR_BET\n'
    reward = 2

    def __init__(self, bet_value, amount):
        super().__init__(bet_value, amount)

    def transform_bet_values_to_target_values(self, bet_value):
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
        if bet_value[0].lower() not in ['red', 'black']:
            raise InvalidBetException()


class EvenOddBet(Bet):
    name = 'EVEN_ODD_BET\n'
    reward = 2

    def __init__(self, bet_value, amount):
        super().__init__(bet_value, amount)

    def validate(self, bet_value):
        if bet_value[0].lower() not in ['even', 'odd']:
            raise InvalidBetException()

    def transform_bet_values_to_target_values(self, bet_value):
        odd = [n for n in all_values if n % 2 == 1]
        if bet_value[0].lower() == 'odd':
            return odd
        else:
            return list(set(all_values) - set(odd))


class LowHighBet(Bet):
    name = 'LOW_HIGH_BET\n'
    reward = 2

    def __init__(self, bet_value, amount):
        super().__init__(bet_value, amount)

    def validate(self, bet_value):
        if bet_value[0].lower() not in ['low', 'high']:
            raise InvalidBetException()

    def transform_bet_values_to_target_values(self, bet_value):
        low = [number for number in all_values if number in range(1, 19)]
        if bet_value[0].lower() == 'low':
            return low
        else:
            return list(set(all_values) - set(low))


class StreetBet(Bet):
    name = 'STREET_BET\n'
    reward = 11

    def __init__(self, bet_values, amount):
        super().__init__(bet_values, amount)

    def validate(self, bet_values):
        ''' expect bet_value like "1" '''
        bet_values.sort()
        valid_bets = []
        for index in range(1, 13):
            valid_bets.append([row[index] for row in board])
        if bet_values not in valid_bets:
            raise InvalidBetException()


class SixLineBet(Bet):
    name = 'SIXLINE_BET\n'
    reward = 5

    def __init__(self, bet_values, amount):
        super().__init__(bet_values, amount)

    def validate(self, bet_values):
        bet_values.sort()
        valid_numbers = [[n, n+3] for n in range(1, 37, 3) if n != 34]
        if bet_values not in valid_numbers:
            raise InvalidBetException

    def transform_bet_values_to_target_values(self, bet_values):
        return [n for n in range(bet_values[0], bet_values[1] + 3)]


bet_types = {
    'STRAIGHT_BET': StraightBet,
    'COLOR_BET': ColorBet,
    'EVENODD_BET': EvenOddBet,
    'LOWHIGH_BET': LowHighBet,
    'STREET_BET': StreetBet,
    'SIXLINE_BET': SixLineBet
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
