from .const import YELLOW, GREEN, BLUE, RED
from .card import NumberCard


class Stack():
    def __init__(self):
        self.cards = self.generate_cards()

    def generate_cards(self):
        generated_cards = [
            NumberCard(color, num)
            for num in range(0, 10)
            for color in [YELLOW, GREEN, BLUE, RED]
        ] * 2
        return generated_cards

    def count_number_cards(self):
        count = 0
        for card in self.cards:
            if type(card) == NumberCard:
                count += 1
        return count
