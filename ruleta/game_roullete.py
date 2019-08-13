from .bet import BetCreator
from .player import Player
from .roulette import Roulette
# Exceptions
from .exceptions.out_of_cash_exception import OutOfCashException
from .exceptions.invalid_bet_exception import InvalidBetException


class GameRoulette:
    name = 'Roulette'

    def __init__(self):
        self.is_playing = True
        start_money = int(input())
        self.player1 = Player(start_money)
        self.roulette1 = Roulette()

    def next_turn(self):
        are_bets_open = True
        bets = []
        while(are_bets_open):
            BetCreator.list_bets()  # show the available bets
            bet = self.bet_type_input()
            if (bet == "END"):
                are_bets_open = False
            else:
                bets.append(bet)

    def bet_type_input(self):
        valid_input = True
        while not valid_input:
            bet_type = int(input("Enter a bet type"))
            if bet_type == 0:
                return 'END'
            elif not 1 <= bet_type <= 10:
                print('Your input is invalid')
            else:
                return self.enter_a_bet(bet_type)

    def enter_a_bet(self, bet_type):
        numbers = input("Please enters the numbers for the bet")
        ammount = input("Enter the ammount of money of the bet")
        try:
            self.player1.dicrement_money(ammount)
            bet_factory = BetCreator()
            bet = bet_factory.create(bet_type, numbers, ammount)
            return bet
        except OutOfCashException:
            print('Error: Out of cash')
        except InvalidBetException:
            print('Your chosen numbers are invalid')

    def play(self):
        self.board
        self.next_turn()
        # winner_number = self.roulette1.generate_number()

    @property
    def board(self):
        self.roulette1.get_last_numbers()
