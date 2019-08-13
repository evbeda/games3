from .bet import BetCreator
from .player import Player
from .roulette import Roulette


class GameRoulette:
    name = 'Roulette'

    def __init__(self):
        self.is_playing = True
        print("Game started. \nHow much money do you have?")
        start_money = int(input())
        self.player1 = Player(start_money)
        self.roulette1 = Roulette()

    def next_turn(self):
        print("Bet’s open \nMake a bet.")
        are_bets_open = True
        bets = []
        while(are_bets_open):
            BetCreator.list_bets()
            bet = self.player1.place_bet()
            if (bet == "END"):
                are_bets_open = False
                break
            else:
                bets.append(bet)
        return bets
        print("Bets are closed")

    def play(self):
        self.next_turn()
        # winner_number = self.roulette1.generate_number()

    def board(self):
        self.roulette1.get_last_numbers()
