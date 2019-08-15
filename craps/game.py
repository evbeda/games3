from .turn import Turn
from .bet import BetCreator
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .exceptions.out_of_cash_exception import OutOfCashException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
    BET_PLACED,
    INVALID_BET_TYPE,
    OUT_OF_CASH
)


class CrapsGame:

    name = 'Craps Game'
    # input_args = 1

    def __init__(self):
        self.turn = Turn()
        self.is_playing = True
        self.bets = []
        self.money = 1000

    def next_turn(self):
        if self.turn.state == PLAYER_LOST:
            # not tested
            self.bets = []
            return LOST_MESSAGE
        elif self.turn.state == PLAYER_WON:
            # not tested
            self.bets = []
            return WON_MESSAGE
        return BET_MESSAGE

    def play(self, user_input):
        if user_input == 'No':
            self.is_playing = False
            return 'Game Over'
        elif user_input == 'Go':
            turn_dice = self.turn.shoot()
            # not tested ...
            activated_bets = self.turn.check_bets(self.bets, turn_dice)
            for bet in activated_bets:
                self.money += bet.pay()
            self.bets = [
                bet
                for bet in self.bets
                if bet not in activated_bets]
            # ... not tested
            return turn_dice
        else:
            try:
                bet_type, amount, bet_values = self.resolve_command(user_input)
                bet = BetCreator.create(bet_type, amount, bet_values)
                self.decrease_money(amount)
                self.bets.append(bet)
                return BET_PLACED + bet_type
            except InvalidBetTypeException:
                return INVALID_BET_TYPE
            except OutOfCashException:
                return OUT_OF_CASH

    # command like
    # BETNAME amount dice_options
    def resolve_command(self, command):
        list_string = command.split()
        bet_type = list_string[0]
        amount = int(list_string[1])
        bet_values = [int(number) for number in list_string[2:]]
        if len(bet_values) > 2:
            bet_values = bet_values[0:2]
        return (bet_type, amount, bet_values)

    def decrease_money(self, amount):
        if amount >= self.money:
            raise OutOfCashException()
        self.money -= amount

    # @property
    # def board(self):
    #     return self.turn.point
