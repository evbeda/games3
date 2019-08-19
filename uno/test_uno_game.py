import unittest
from .const import GREEN, RED, BLUE, YELLOW
# from parameterized import parameterized
from .uno import Uno
from .card import (
    NumberCard,
    ReverseCard,
    SkipCard,
    DrawTwoCard,
    # DrawFourCard,
    # WildCard,
)


class TestUnoGame(unittest.TestCase):

    # testing initial conditions

    def test_is_playing(self):
        uno = Uno()
        self.assertEqual(uno.is_playing, True)

    def test_remaining_initial_stack_length(self):
        uno = Uno()
        self.assertEqual(len(uno.stack.stack_cards), 97)

    def test_initial_cards_player_length(self):
        uno = Uno()
        self.assertEqual(len(uno.player.cards_player), 7)

    def test_initial_discard_cards_length(self):
        uno = Uno()
        self.assertEqual(len(uno.stack.discard_cards), 1)

    # testing initial play take a card conditions
    def test_initial_take_card_stack_length(self):
        uno = Uno()
        uno.play('0')
        self.assertEqual(len(uno.stack.stack_cards), 96)

    def test_initial_take_card_cards_player_length(self):
        uno = Uno()
        uno.play('0')
        self.assertEqual(len(uno.player.cards_player), 8)

    # test playing a card

    def test_play_a_invalid_car(self):
        uno = Uno()
        uno.stack.discard_cards = [NumberCard(GREEN, '5')]
        uno.player.cards_player = [
            NumberCard(RED, '7'),
            NumberCard(BLUE, '7'),
            NumberCard(YELLOW, '7'),
            ReverseCard(RED),
            SkipCard(RED),
            DrawTwoCard(RED),
        ]
        play_card = uno.play(1)
        self.assertEqual(play_card, "Your card is not valid")
        # check player_cards length same
        self.assertEqual(len(uno.player.cards_player), 6)

    def test_play_a_valid_card(self):
        uno = Uno()
        uno.stack.discard_cards = [NumberCard(RED, '7')]
        uno.player.cards_player = [
            NumberCard(GREEN, '7'),
            NumberCard(BLUE, '7'),
            NumberCard(YELLOW, '7'),
            ReverseCard(RED),
            SkipCard(RED),
            DrawTwoCard(RED),
        ]
        last_played_card = uno.player.cards_player[0]
        uno.play(1)
        # check player_cards length reduced
        self.assertEqual(len(uno.player.cards_player), 5)
        # chek played_card equal to last discard_card
        self.assertEqual(last_played_card, uno.stack.discard_cards[-1])

    def test_winner(self):
        uno = Uno()
        uno.stack.discard_cards = [NumberCard(RED, '7')]
        uno.player.cards_player = [NumberCard(GREEN, '7')]
        self.assertEqual(uno.play(1), 'You WON')

    def verify_first_turn_computer_player():
        uno = Uno()
        uno.computer_player.auto_play()
        discard_cards_qty = len(uno.stack.discard_cards)
        self.assertEqual(len(uno.computer_player.cards_player), 6)
        self.assertEqual(len(uno.stack.discard_cards), discard_cards_qty + 1)


