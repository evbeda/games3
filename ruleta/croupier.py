from .exceptions.out_of_cash_exception import OutOfCashException


class Croupier:
    def __init__(self, player):
        self.player = player
        self.bets = []

    def discount_money_from_player(self, ammount):
        if ammount >= self.player.money:
            raise OutOfCashException()
        self.player.money -= ammount

    def add_bet(self, bet):
        self.bets.append(bet)
