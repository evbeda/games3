from .exceptions.invalid_bet_exception import InvalidBetTypeException


class Bet:
    def __init__(self, amount):
        self.amount = amount


class PassBet(Bet):
    def __init__(self, amount):
        super().__init__(amount)


class DoNotPassBet(Bet):
    def __init__(self, amount):
        super().__init__(amount)


# class ConcrentDiceBet(Bet):
    # def __init__(self, amount):
        # super().__init__(amount)


bet_types = {
    'PASS_BET': PassBet,
    'DO_NOT_PASS_BET': DoNotPassBet
}


class BetCreator:
    def create(self, bet_type, amount, *bet_values):
        self.validate_bet_type(bet_type)
        bet = None
        bet_class = bet_types[bet_type]  # obtain bet Class from dictionary
        bet = bet_class(amount)
        return bet

    def validate_bet_type(self, bet_type):
        if bet_type not in bet_types:
            raise InvalidBetTypeException()

#    @staticmethod
#    def list_bets():
#        menu = ''
#        for bet in bet_types:
#            menu += bet.name
#        return menu
