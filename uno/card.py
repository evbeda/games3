# Color: red, yellow, blue and green

# Normal cards: from 0 to 9, 2 cards of each color and number

# Special cards
# - reverse: 2 of each color
# - skip: 2 of each color
# - drawTwo: 2 of each color
# - drawFour: total 4
# - wildCard: total 4


class Card():
    pass


class PostColoredCard(Card):

    def __init__(self):
        self.post_color = ''

    def same_to(self, card):
        return True


class ColoredCard(Card):

    def __init__(self, color):
        self.color = color

    def same_to(self, card):
        if isinstance(card, PostColoredCard):
            return True
        elif self.color == card.color:
            return True


class NumberCard(ColoredCard):

    def __init__(self, color, number):
        super().__init__(color)
        self.number = number


class ReverseCard(ColoredCard):

    def __init__(self, color):
        super().__init__(color)


class SkipCard(ColoredCard):
    pass


class DrawTwoCard(ColoredCard):
    pass


class DrawFourCard(PostColoredCard):
    pass


class WildCard(PostColoredCard):
    pass
