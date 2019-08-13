from .exceptions.out_of_cash_exception import OutOfCashException


class Player:
    def __init__(self, start_money):
        self.money = start_money

    def dicrement_money(self, ammount):
        if ammount >= self.money:
            raise OutOfCashException('Te quedaste sin saldo')
        self.money -= ammount
