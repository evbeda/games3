import random
from .exceptions.exceptions import NotANumberException, \
    NotCorrectSelectedCardException


class Player:
    def __init__(self, name='', character=None):
        self.name = ''
        self.character = character[0] if character else ''
        self.wounds = character[1] if character else 0
        self.gold = character[2] if character else 0

    def add_wounds(self, wounds):
        self.wounds += wounds

    def add_gold(self, gold):
        self.gold += gold

    def select_card(self, cards):
        raise NotImplementedError("Can't be called")


class ComputerPlayer(Player):
    def select_card(self, cards):
        return random.choice(cards) if cards else []


class HumanPlayer(Player):
    def select_card(self, cards):
        asking_ended = False
        while asking_ended is False:
            # Add Print card
            sel_card = input('Which card do you want to select? \n')
            try:
                selected_card = int(sel_card)
            except ValueError:
                raise NotANumberException()
            if selected_card in cards:
                return selected_card
            else:
                raise NotCorrectSelectedCardException()
