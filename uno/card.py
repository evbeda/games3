# Color: red, yellow, blue and green

# Normal cards: from 0 to 9, 2 cards of each color and number

# Special cards
# - reverse: 2 of each color
# - skip: 2 of each color
# - drawTwo: 2 of each color
# - drawFour: total 4
# - wildCard: total 4


class Card():

    def same_type_validator(self, card1, card2):
        if type(card1) == type(card2):
            return True
        else:
            return False


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
        return False


class NumberCard(ColoredCard):

    def __init__(self, color, number):
        super().__init__(color)
        self.number = number

    def same_to(self, card):

        if super().same_to(card):
            return True

        if isinstance(card, NumberCard):
            if card.number == self.number:
                return True
        else:
            return False


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

    def action(self, previousCard):
        if type(previousCard) == DrawTwoCard:
            self.cardsToDraw += previousCard.cardsToDraw
        return self.cardsToDraw


class DrawFourCard(PostColoredCard):
    # Chequear por que necesita self, y cuando se agrega, explota en el test.
    def evaluate_next_card(top_card, selected_card):
        return True


class WildCard(PostColoredCard):
    pass
