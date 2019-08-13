from models.exceptions.UnplayableCardException import UnplayableCardException


class Player:
    def __init__(self, name):
        self.name = name
        self.power_cards = [1, 2, 3, 4, 5]
        self.wounds = 0
        self.gold = 0

    # def __eq__(self, player):
    #     return self.name == player.name

    def play(self, card_to_play):
        self.validate(card_to_play)
        self.power_cards.remove(card_to_play)
        self.actual_card = card_to_play

    def validate(self, card):
        if card not in self.power_cards:
            raise UnplayableCardException(f'You can\'t play {card} again')  
