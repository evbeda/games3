from .exceptions.UnplayableCardException import UnplayableCardException


class LevelHand:
    def __init__(self, player):
        self.cards_to_play = [1, 2, 3, 4, 5]
        self.player = player
        self.last_card_played = 0

    def play(self, card_to_play):
        self.validate(card_to_play)
        self.cards_to_play.remove(card_to_play)
        self.last_card_played = card_to_play

    def validate(self, card):
        if card not in self.cards_to_play:
            raise UnplayableCardException(f'You can\'t play {card} again')
