from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import PLAYER_WON, PLAYER_LOST


class Bet:
    def __init__(self, amount, selected_dices):
        self.selected_dices = selected_dices
        self.amount = amount

    def check(self, turn):
        raise NotImplementedError

    def pay(self, turn):
        raise NotImplementedError


class PassBet(Bet):
    def check(self, turn):
        return turn.state == PLAYER_WON

    def pay(self, turn):
        if self.check(turn):
            return 2 * self.amount
        return 0


class DoNotPassBet(Bet):
    def check(self, turn):
        return turn.state == PLAYER_LOST

    def pay(self, turn):
        if self.check(turn):
            return 2 * self.amount
        return 0


class SevenBet(Bet):
    def check(self, turn):
        return sum(turn.dice) == 7

    def pay(self, turn):
        if self.check(turn):
            return 4 * self.amount
        return 0


class DoubleBet(Bet):
    def check(self, turn):
        return turn.dice[0] == turn.dice[1]

    def pay(self, turn):
        rates = {
            (1, 1): 30,
            (6, 6): 30,
            (3, 3): 10,
            (4, 4): 10,
            (2, 2): 8,
            (5, 5): 8
        }
        if self.check(turn):
            return rates[turn.dice] * self.amount
        return 0


# class ConcrentDiceBet(Bet):
    # def __init__(self, amount):
        # super().__init__(amount)


BET_TYPES = {
    'PASS_BET': PassBet,
    'DO_NOT_PASS_BET': DoNotPassBet,
    'DOUBLE_BET': DoubleBet,
    'SEVEN_BET': SevenBet
}


class BetCreator:

    @staticmethod
    def create(bet_type, amount, *bet_values):
        BetCreator.validate_bet_type(bet_type)
        bet = None
        bet_class = BET_TYPES[bet_type]  # obtain bet Class from dictionary
        bet = bet_class(amount, bet_values)
        return bet

    @staticmethod
    def validate_bet_type(bet_type):
        if bet_type not in BET_TYPES:
            raise InvalidBetTypeException()

#    @staticmethod
#    def list_bets():
#        menu = ''
#        for bet in bet_types:
#            menu += bet.name
#        return menu
