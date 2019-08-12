# Color: red, yellow, blue and green

# Normal cards: from 0 to 9, 2 cards of each color and number

# Special cards
# - reverse: 2 of each color
# - skip: 2 of each color
# - drawTwo: 2 of each color
# - drawFour: total 4
# - wildCard: total 4

class Card():
    
    def same_to(self, card):
        if self.color == card.color:
            return True

class NumberCard(Card):

    def __init__(self, color, number):
        self.color = color
        self.number = number

class ReverseCard(Card):

    def __init__(self, color):
        self.color = color
        