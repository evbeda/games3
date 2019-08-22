from random import choice


class Player():

    def __init__(self, cards):
        self.cards_player = cards
        self.already_take_a_card = False


class HumanPlayer(Player):
    def __init___(self, cards):
        super().__init__(cards)

    def select_card(self, card_index, stack):
        card = self.cards_player[card_index]
        if not card.is_valid(stack.get_last_discard_card):
            raise Exception()
        return card


class ComputerPlayer(Player):
    def __init__(self, cards):
        super().__init__(cards)

    def select_card(self, card_index, stack):
        possible_cards = [
            card for card in self.cards_player
            if card.is_valid(stack.get_last_discard_card)
        ]
        if possible_cards:
            return choice(possible_cards)
        return None
