
class Player():

    def __init__(self, cards_player):
        self.cards_player = cards_player
        self.loses_turn = False

    def selected_card(self, index_card):
        for index, card in enumerate(self.cards_player):
            if index == index_card - 1:
                return card

    def add_cards_to_hand(self, cards):
        for card in cards:
            self.cards_player.append(card)

    def auto_play(self):
        last_card = stack.discard_cards[-1]
        for card in self.computer_player.cards_player:
            if card.is_valid(self.stack.last_card):
                self.computer_player.cards_player.remove(card)
                self.stack.put_card_in_discard(card)

        if last_card == stack.discard_cards[-1]:
            return self.player.cards_player.append(
                self.stack.stack_cards.pop())

