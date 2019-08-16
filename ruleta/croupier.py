from .exceptions.out_of_cash_exception import OutOfCashException


class Croupier:
    def __init__(self, player):
        self.player = player
        self.bets = []

    def discount_money_from_player(self, ammount):
        if ammount >= self.player.money:
            raise OutOfCashException()
        self.player.money -= ammount

    def add_bet(self, bet, amount):
        self.discount_money_from_player(amount)
        self.bets.append(bet)

    def calculate_total_award(self, chosen_number):
        for bet in self.bets:
            self.player.money += bet.calculate_award(chosen_number)
        else:
            self.bets = []


