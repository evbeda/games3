

class Card():
    pass


class PostColoredCard(Card):

    def __init__(self):
        self.color = ''

    def set_color(self, color):
        self.color = color

    def is_valid(self, card):
        return True


class ColoredCard(Card):

    def __init__(self, color):
        self.color = color

    def same_color(self, card):
        return self.color == card.color

    def same_type(self, card):
        return type(self) == type(card)

    def is_valid(self, card):
        return self.same_color(card) or self.same_type(card)


class NumberCard(ColoredCard):

    def __init__(self, color, number):
        super().__init__(color)
        self.number = number

    def same_number(self, card):
        if self.same_type(card):
            return card.number == self.number
        return False

    def is_valid(self, card):
        return self.same_color(card) or self.same_number(card)


class ReverseCard(ColoredCard):

    def __init__(self, color):
        super().__init__(color)


class SkipCard(ColoredCard):

    def __init__(self, color):
        super().__init__(color)


class DrawTwoCard(ColoredCard):
    def __init__(self, color):
        self.color = color
        self.cardsToDraw = 2

# TODO This should check the stack, not a previous card. Check camel_case.
    def action(self, previousCard):
        if type(previousCard) == DrawTwoCard:
            self.cardsToDraw += previousCard.cardsToDraw
        return self.cardsToDraw


class DrawFourCard(PostColoredCard):
    pass


class WildCard(PostColoredCard):
    pass
