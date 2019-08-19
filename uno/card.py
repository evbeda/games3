

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

    name = 'Number'

    def __init__(self, color, number):
        super().__init__(color)
        self.number = number

    def __str__(self):
        return '{} - {}'.format(self.number, self.color)

    def same_number(self, card):
        if self.same_type(card):
            return card.number == self.number
        return False

    def is_valid(self, card):
        return self.same_color(card) or self.same_number(card)

    def get_action(self):
        return (False, 0)


class ReverseCard(ColoredCard):

    name = 'Reverse'

    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return '{} - {}'.format(self.name, self.color)

    def get_action(self):
        return (True, 0)


class SkipCard(ColoredCard):

    name = 'Skip'

    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return '{} - {}'.format(self.name, self.color)

    def get_action(self):
        return (True, 0)


class DrawTwoCard(ColoredCard):

    name = 'Draw Two'

    def __init__(self, color):
        self.color = color
        self.cards_to_draw = 2

    def __str__(self):
        return '{} - {}'.format(self.name, self.color)

    def get_action(self):
        return (True, 2)
        # if type(previousCard) == DrawTwoCard:
        #     self.cards_to_draw += previousCard.cards_to_draw
        # return self.cards_to_draw


class DrawFourCard(PostColoredCard):

    name = 'Draw Four'

    def get_action(self):
        return (True, 4)

    def __str__(self):
        return '{}'.format(self.name)


class WildCard(PostColoredCard):

    name = 'Wild'

    def __str__(self):
        return '{}'.format(self.name)
