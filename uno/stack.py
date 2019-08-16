from .const import YELLOW, GREEN, BLUE, RED
from .card import NumberCard
from .card import ReverseCard
from .card import SkipCard
from .card import DrawTwoCard
from .card import DrawFourCard
from .card import WildCard
import random


class Stack():
    def __init__(self):
        self.stack_cards = self.generate_cards()
        self.discard = []

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

    def take_card(self):
        return self.stack_cards.pop()

    def is_stack_empty(self):
        discard = self.discard
        self.discard = self.discard.pop()
        random.shuffle(discard)
        self.stack_cards = discard
