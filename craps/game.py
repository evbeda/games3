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
        self.money = 1000

    def next_turn(self):
        if self.turn.state == PLAYER_LOST:
            self.turn = Turn()
            return LOST_MESSAGE
        if self.turn.state == PLAYER_WON:
            self.turn = Turn()
            return WON_MESSAGE
        return BET_MESSAGE

    def play(self, user_input):
        if user_input == 'No':
            self.is_playing = False
            return 'Game Over'
        if user_input == 'Go':
            self.money += self.turn.shoot()
            return self.turn.dice
        try:
            bet_type, amount, bet_values = \
                CrapsGame.resolve_command(user_input)
            bet = BetCreator.create(bet_type, amount, bet_values)
            self.decrease_money(amount)
            self.turn.bets.append(bet)
            return BET_PLACED + bet_type
        except InvalidBetTypeException:
            return INVALID_BET_TYPE
        except OutOfCashException:
            return OUT_OF_CASH

    def decrease_money(self, amount):
        if amount >= self.money:
            raise OutOfCashException()
        self.money -= amount

    # @property
    # def board(self):
    #     return self.turn.point

    # command like
    # BETNAME amount dice_options
    @staticmethod
    def resolve_command(command):
        list_string = command.split()
        bet_type = list_string[0]
        amount = int(list_string[1])
        bet_values = [int(number) for number in list_string[2:]]
        if len(bet_values) > 2:
            bet_values = bet_values[0:2]
        return (bet_type, amount, bet_values)
