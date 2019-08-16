from .bet import BetCreator
from .croupier import Croupier
from .roulette import Roulette
from .player import Player
# Exceptions
from .exceptions.out_of_cash_exception import OutOfCashException
from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException


class GameRoulette:
    name = 'Roulette'

    def __init__(self):
        self.is_playing = True
        self.croupier = Croupier(Player(100))
        self.roulette1 = Roulette()

    def next_turn(self):
        return BetCreator.list_bets() if self.is_playing else 'Game over'

    def play(self, command):
        '''
        command is like:
        BET_SIMPLE 36 100
        BET...
        GO
        QUIT
        '''
        if command == 'END_GAME':
            self.is_playing = False
            return 'Bye'
        elif command == 'GO':
            pass
            # correr ruleta
            # croupier resuelve el award
            # reset round_bets
        else:
            try:
                bet_type, bet_values, ammount = self.resolve_command(command)
                self.croupier.discount_money_from_player(ammount)
                self.croupier.add_bet(
                    BetCreator.create(bet_type, bet_values, ammount))
                return 'Your bet was saved succesfully'
            except OutOfCashException:
                return f'Not enough cash! you have {self.player1.money}'
            except InvalidBetException:
                return 'Your bet is invalid'
            except InvalidBetTypeException:
                return 'Your bet type is invalid'

    def resolve_command(self, command):
        list_string = command.split()
        bet_type = list_string[0]
        BetCreator.validate_bet_type(bet_type)
        bet_values = [int(number) for number in list_string[1:-1]]
        ammount = int(list_string[-1])
        return (bet_type, bet_values, ammount)

    @property
    def board(self):
        self.roulette1.get_last_numbers()
