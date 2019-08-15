from .bet import BetCreator
from .player import Player
from .roulette import Roulette
# Exceptions
from .exceptions.out_of_cash_exception import OutOfCashException
from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException


class GameRoulette:
    name = 'Roulette'

    def __init__(self):
        self.is_playing = True
        self.player1 = Player(100)
        self.roulette1 = Roulette()
        self.round_bets = []

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
            # ver si el jugador gano
            # reset round_bets
        else:
            try:
                bet_type, bet_values, ammount = self.resolve_command(command)
                self.player1.dicrement_money(ammount)
                bet_creator = BetCreator()
                self.round_bets.append(
                    bet_creator.create(bet_type, bet_values, ammount))
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
