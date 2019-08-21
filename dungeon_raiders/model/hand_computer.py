from random import choice


class HandComputer:
    def __init__(self, player):
        self.cards_to_play = [1, 2, 3, 4, 5]
        self.player = player
        self.last_card_played = None

    def play(self):
        card_to_play = choice(self.cards_to_play)
        self.cards_to_play.remove(card_to_play)
        self.last_card_played = card_to_play
