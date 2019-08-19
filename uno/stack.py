import random
from .const import YELLOW, GREEN, BLUE, RED
from .card import (
    NumberCard,
    ReverseCard,
    SkipCard,
    DrawTwoCard,
    DrawFourCard,
    WildCard,
)


class Stack():
    def __init__(self):
        self.stack_cards = self.generate_cards()
        self.discard_cards = []

    def generate_cards(self):
        generated_cards = []
        generated_number_cards = [
            NumberCard(color, num)
            for num in range(0, 10)
            for color in [YELLOW, GREEN, BLUE, RED]
        ] * 2
        generated_reverse_cards = [
            ReverseCard(color)
            for color in [YELLOW, GREEN, BLUE, RED]
        ] * 2
        generated_skip_cards = [
            SkipCard(color)
            for color in [YELLOW, GREEN, BLUE, RED]
        ] * 2
        generated_draw_two_cards = [
            DrawTwoCard(color)
            for color in [YELLOW, GREEN, BLUE, RED]
        ] * 2
        generated_draw_four_cards = [
            DrawFourCard()
            for num in range(0, 4)
        ]
        generated_wild_cards = [
            WildCard()
            for num in range(0, 4)
        ]
        generated_cards = generated_number_cards + \
            generated_reverse_cards + \
            generated_skip_cards + \
            generated_draw_two_cards + \
            generated_draw_four_cards + \
            generated_wild_cards
        random.shuffle(generated_cards)
        return generated_cards

    def recreate_stack(self):
        discard_cards = self.discard_cards
        self.discard_cards = self.discard_cards.pop()
        random.shuffle(discard_cards)
        self.stack_cards = discard_cards

    def put_card_in_discard(self, card=None):
        if card is None:
            self.discard_cards.append(self.stack_cards.pop())
        else:
            self.discard_cards.append(card)

    def generate_cards_player(self):
        cards_qty = 0
        cards_player = []
        while cards_qty != 7:
            cards_player.append(self.stack_cards.pop())
            cards_qty += 1
        return cards_player
