from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import (
    PLAYER_WON,
    PLAYER_LOST,
    BET_IN_PROGRESS,
    BET_LOST,
    BET_PAYED,
    PASS_BET,
    DO_NOT_PASS_BET,
    DOUBLE_BET,
    SEVEN_BET,
    CRAPS_BET,
    GAME_STARTED,
    LOSING_SCORES,
    GAME_IN_PROGRESS
)


class Bet:
    def __init__(self, amount, selected_dices):
        self.selected_dices = selected_dices
        self.amount = amount
        self.amount_payed = 0
        self.state = BET_IN_PROGRESS

    def check(self, turn):
        raise NotImplementedError

    def pay(self, turn):
        raise NotImplementedError


class PassBet(Bet):

    def __str__(self):
        ret = ''
        ret += 'Bet type: {}\n'.format(type(self))
        ret += 'Amount bet: {}\n'.format(self.amount)
        ret += 'Amount payed: {}\n'.format(self.amount_payed)
        ret += 'Bet state: {}\n'.format(self.state)
        return ret

    def check(self, turn):
        return turn.state == PLAYER_WON

    def pay(self, turn):
        if self.check(turn):
            self.amount_payed = 2 * self.amount
            self.state = BET_PAYED
            return self.amount_payed
        else:
            self.state = BET_LOST
            self.amount_payed = 0
            return self.amount_payed


class DoNotPassBet(Bet):

    def __str__(self):
        ret = ''
        ret += 'Bet type: {}\n'.format(type(self))
        ret += 'Amount bet: {}\n'.format(self.amount)
        ret += 'Amount payed: {}\n'.format(self.amount_payed)
        ret += 'Bet state: {}\n'.format(self.state)
        return ret

    def check(self, turn):
        return turn.state == PLAYER_LOST

    def pay(self, turn):
        if self.check(turn):
            self.amount_payed = 2 * self.amount
            self.state = BET_PAYED
            return self.amount_payed
        else:
            self.amount_payed = 0
            self.state = BET_LOST
            return self.amount_payed


class SevenBet(Bet):

    def __str__(self):
        ret = ''
        ret += 'Bet type: {}\n'.format(type(self))
        ret += 'Amount bet: {}\n'.format(self.amount)
        ret += 'Amount payed: {}\n'.format(self.amount_payed)
        ret += 'Bet state: {}\n'.format(self.state)
        return ret

    def check(self, turn):
        return sum(turn.dice) == 7

    def pay(self, turn):
        if self.check(turn):
            self.amount_payed = 4 * self.amount
            self.state = BET_PAYED
            return self.amount_payed
        else:
            self.amount_payed = 0
            self.state = BET_LOST
            return self.amount_payed


class DoubleBet(Bet):

    def __str__(self):
        ret = ''
        ret += 'Bet type: {}\n'.format(type(self))
        ret += 'Amount bet: {}\n'.format(self.amount)
        ret += 'Amount payed: {}\n'.format(self.amount_payed)
        ret += 'Bet state: {}\n'.format(self.state)
        return ret

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
            self.amount_payed = rates[turn.dice] * self.amount
            self.state = BET_PAYED
            return self.amount_payed
        else:
            self.amount_payed = 0
            self.state = BET_IN_PROGRESS
            return self.amount_payed


class CrapsBet(Bet):

    def __str__(self):
        ret = ''
        ret += 'Bet type: {}\n'.format(type(self))
        ret += 'Amount bet: {}\n'.format(self.amount)
        ret += 'Amount payed: {}\n'.format(self.amount_payed)
        ret += 'Bet state: {}\n'.format(self.state)
        return ret

    def check(self, turn):
        return(
            sum(turn.dice) in LOSING_SCORES and
            turn.state == GAME_IN_PROGRESS
        )

    def pay(self, turn):
        if self.check(turn):
            self.state = BET_PAYED
            return 15 * self.amount
        else:
            self.state = BET_LOST
            return 0


bet_types = {
    PASS_BET: PassBet,
    DO_NOT_PASS_BET: DoNotPassBet,
    DOUBLE_BET: DoubleBet,
    SEVEN_BET: SevenBet,
    CRAPS_BET: CrapsBet
}

# Bet
ONLY_START_BETS = [CrapsBet, PassBet, DoNotPassBet]


class BetCreator:

    @staticmethod
    def create(bet_type, amount, turn, *bet_values):
        BetCreator.validate_bet_type(bet_type)
        BetCreator.validate_bet_turn(bet_type, turn)
        bet = None
        bet_class = bet_types[bet_type]  # obtain bet Class from dictionary
        bet = bet_class(amount, bet_values)
        return bet

    @staticmethod
    def validate_bet_type(bet_type):
        if bet_type not in bet_types:
            raise InvalidBetTypeException()

    @staticmethod
    def validate_bet_turn(bet_type, turn):
        if turn.state != GAME_STARTED:
            if type(bet_type) in ONLY_START_BETS:
                raise InvalidBetTurnException()

# @TODO: INTEGRATE LIST_BETS
#    @staticmethod
#    def list_bets():
#        menu = ''
#        for bet in bet_types:
#            menu += bet.type
#        return menu
