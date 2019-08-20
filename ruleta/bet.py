from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .board import BOARD
import math

all_values = list(range(1, 37))


class Bet:
    # reward = 0

    def __init__(self, bet_value, amount):
        self.validate(bet_value)
        self.target_numbers = \
            sorted(self.transform_bet_values_to_target_values(bet_value))
        self.amount = amount

    # called by str(bet)
    # returns like "DOUBLE_BET 9 12, $5"
    def __str__(self):
        bet_str = self.name + " "
        bet_target_numbers = [
            str(target_number)
            for target_number in self.target_numbers
            ]
        bet_str += " ".join(bet_target_numbers)
        bet_str += ", bet $" + str(self.amount)
        return bet_str

    def transform_bet_values_to_target_values(self, bet_value):
        return bet_value

    def is_winner(self, chosen_number):
        return chosen_number in self.target_numbers

    def calculate_award(self, chosen_number):
        return self.reward * self.amount \
            if self.is_winner(chosen_number) else 0


class StraightBet(Bet):
    name = 'STRAIGHT_BET'
    reward = 35

    # Uses __str__ from Bet 

    def validate(self, bet_value):
        ''' expect bet_value like "1" '''
        if not (0 <= bet_value[0] <= 36):
            raise InvalidBetException()


class DoubleBet(Bet):
    name = 'DOUBLE_BET'
    reward = 17

    # Uses __str__ from Bet 

    def validate(self, bet_values):
        row1 = 0
        row2 = 0
        for row in BOARD:
            if bet_values[0] in row:
                row1 = BOARD.index(row)
            if bet_values[1] in row:
                row2 = BOARD.index(row)
        if(sorted(bet_values) in [[0, 2], [0, 1]]):
            pass
        elif abs(row1-row2) == 0 and abs(bet_values[0]-bet_values[1]) != 3:
            raise InvalidBetException
        elif abs(row1-row2) > 1:
            raise InvalidBetException
        elif abs(row1-row2) == 1 and abs(bet_values[0]-bet_values[1]) != 1:
            raise InvalidBetException


class ColorBet(Bet):
    name = 'COLOR_BET'
    reward = 2

    # called by str(bet)
    # returns like "COLOR_BET red, $15"
    def __str__(self):
        bet_str = self.name + " "
        bet_str += str(self.get_color())
        bet_str += ", bet $" + str(self.amount)
        return bet_str

    def get_color(self):
        range_1 = [number for number in all_values if number in range(1, 11)
                   and number % 2 == 1]
        range_2 = [number for number in all_values if number in range(19, 29)
                   and number % 2 == 1]
        range_3 = [number for number in all_values if number in range(11, 19)
                   and number % 2 == 0]
        range_4 = [number for number in all_values if number in range(29, 37)
                   and number % 2 == 0]
        red = sorted(range_1 + range_2 + range_3 + range_4)
        if self.target_numbers == red:
            return 'red'
        else:
            return 'black'

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
    name = 'EVENODD_BET'
    reward = 2

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
    name = 'LOWHIGH_BET'
    reward = 2

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
    name = 'STREET_BET'
    reward = 11

    def validate(self, bet_values):
        ''' expect bet_value like "1" '''
        bet_values.sort()
        valid_bets = []
        for index in range(1, 13):
            valid_bets.append([row[index] for row in BOARD])
        if bet_values not in valid_bets:
            raise InvalidBetException()


class SixLineBet(Bet):
    name = 'SIXLINE_BET'
    reward = 5

    def validate(self, bet_values):
        bet_values.sort()
        valid_numbers = [[n, n+3] for n in range(1, 37, 3) if n != 34]
        if bet_values not in valid_numbers:
            raise InvalidBetException

    def transform_bet_values_to_target_values(self, bet_values):
        return [n for n in range(bet_values[0], bet_values[1] + 3)]


class OneDozenBet(Bet):
    name = 'ONEDOZEN_BET'
    reward = 2

    # called by str(bet)
    # returns like "ONEDOZEN_BET 1 dozen, $5"
    def __str__(self):
        bet_str = self.name + " "
        bet_str += str(self.get_dozen()) + " dozen"
        bet_str += ", bet $" + str(self.amount)
        return bet_str

    def validate(self, bet_value):
        if bet_value not in list(range(1, 4)):
            raise InvalidBetException()

    def transform_bet_values_to_target_values(self, bet_value):
        # For example: bet_value = 1
        # low = 0, high = 13
        low = 12 * (bet_value - 1)
        high = (12 * bet_value) + 1
        possible_target_values = [n for n in range(low, high)]
        possible_target_values.pop(0)
        return possible_target_values

    def get_dozen(self):
        return int(max(self.target_numbers) / 12)


class TwoDozenBet(Bet):
    name = 'TWODOZEN_BET'
    reward = 1.5

    def validate(self, bet_values):
        if len(bet_values) != 2:
            raise InvalidBetException()
        # It verifies that both values are between 1 and 3 and aren't equal
        if bet_values[0] in list(range(1, 4)) and \
            bet_values[1] in list(range(1, 4)) and \
                bet_values[0] != bet_values[1]:
            pass
        else:
            raise InvalidBetException()

    def transform_bet_values_to_target_values(self, bet_values):
        all_target_values = []
        for bet_value in bet_values:
            low = 12 * (bet_value - 1)
            high = (12 * bet_value) + 1
            possible_target_values = [n for n in range(low, high)]
            possible_target_values.pop(0)
            all_target_values += possible_target_values
        # Remove duplicated values
        all_target_values = list(dict.fromkeys(all_target_values))
        return all_target_values

    def calculate_award(self, chosen_number):
        return math.floor(self.reward * self.amount) \
            if self.is_winner(chosen_number) else 0


class TrioBet(Bet):
    name = 'TRIO_BET'
    reward = 11

    def validate(self, bet_values):
        if 0 not in bet_values:
            if len(bet_values) == 2:
                bet_values.sort()
                if bet_values[0] in BOARD[0] and \
                    bet_values[1] in BOARD[2] and \
                        abs(bet_values[0] - bet_values[1]) == 2:
                    pass
                else:
                    raise InvalidBetException()
            else:
                raise InvalidBetException()
        else:
            raise InvalidBetException()

    def transform_bet_values_to_target_values(self, bet_values):
        return list(range(bet_values[0], bet_values[1] + 1))


class QuadrupleBet(Bet):
    name = 'QUADRUPLE_BET'
    reward = 8

    def validate(self, bet_values):
        if 0 not in bet_values:
            if len(bet_values) == 4:
                bet_values.sort()
                # Same Line Condition
                same_linecond = abs(bet_values[0] - bet_values[1]) == 1 and \
                    abs(bet_values[2] - bet_values[3]) == 1
                # Adyacent Line Condition
                ady_linecond = abs(bet_values[0] - bet_values[2]) == 3 and \
                    abs(bet_values[1] - bet_values[3]) == 3
                if same_linecond and ady_linecond:
                    pass
                else:
                    raise InvalidBetException()
            else:
                raise InvalidBetException()
        else:
            raise InvalidBetException()

    def transform_bet_values_to_target_values(self, bet_values):
        return sorted(bet_values)


bet_types = {
    'STRAIGHT_BET': StraightBet,
    'COLOR_BET': ColorBet,
    'EVENODD_BET': EvenOddBet,
    'LOWHIGH_BET': LowHighBet,
    'STREET_BET': StreetBet,
    'SIXLINE_BET': SixLineBet,
    'DOUBLE_BET': DoubleBet,
    'ONEDOZEN_BET': OneDozenBet,
    'TWODOZEN_BET': TwoDozenBet,
    'TRIO_BET': TrioBet,
    'QUADRUPLE_BET': QuadrupleBet
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
        bet_names = [bet_class.name for bet_class in bet_types.values()]
        return ', '.join(bet_names)
