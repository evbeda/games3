from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import PLAYER_WON, PLAYER_LOST


class Bet:
    def __init__(self, amount):
        self.amount = amount

    def check(self, turn, dice):
        raise NotImplementedError

    def pay(self):
        raise NotImplementedError


class PassBet(Bet):
    def __init__(self, amount):
        super().__init__(amount)

    def check(self, turn, dice):
        return turn.state == PLAYER_WON

    # not tested
    def pay(self):
        return 2 * self.amount


class DoNotPassBet(Bet):
    def __init__(self, amount):
        super().__init__(amount)

    def check(self, turn, dice):
        return turn.state == PLAYER_LOST

    # not tested
    def pay(self):
        return 2 * self.amount


# class ConcrentDiceBet(Bet):
    # def __init__(self, amount):
        # super().__init__(amount)


bet_types = {
    'PASS_BET': PassBet,
    'DO_NOT_PASS_BET': DoNotPassBet
}


class BetCreator:

    @staticmethod
    def create(bet_type, amount, *bet_values):
        BetCreator.validate_bet_type(bet_type)
        bet = None
        bet_class = bet_types[bet_type]  # obtain bet Class from dictionary
        bet = bet_class(amount)
        return bet

    @staticmethod
    def validate_bet_type(bet_type):
        if bet_type not in bet_types:
            raise InvalidBetTypeException()

#    @staticmethod
#    def list_bets():
#        menu = ''
#        for bet in bet_types:
#            menu += bet.name
#        return menu
