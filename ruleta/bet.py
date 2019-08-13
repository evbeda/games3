from .exceptions.invalid_bet_exception import InvalidBetException
from .player import Player

class StraightBet:
    def __init__(self, bet_value, ammount, player):
        self.reward = 35
        self.ammount = ammount
        self.bet_value = bet_value
        self.player = player
        self.validate()

    def validate(self):
        ''' expect bet_value like "1" '''
        if not (0 <= self.bet_value <= 36):
            raise InvalidBetException('Invalid bet')
    
    def calculate_total_award(self):
        return self.reward * self.ammount        
    
    def win_bet(self, chosen_number):
        if chosen_number == self.bet_value:
            self.player.money += self.calculate_total_award()


bet_types = {
    1: StraightBet,
}


class BetCreator:
    def create(self, bet_type, bet_value, ammount, player):
        bet = None
        if bet_type in bet_types:
            try:
                bet_class = bet_types[bet_type]
                bet = bet_class(bet_value, ammount, player)
            except InvalidBetException:
                print('Your bet value is invalid ')
        return bet

    @staticmethod
    def list_bets():
        pass
