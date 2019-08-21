import unittest
from .const import GREEN, RED, BLUE, YELLOW, DRAW_CARD_INPUT, EXIT
from parameterized import parameterized
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

    def set_up(self):
        self.game = Uno()

    def test_is_playing(self):
        uno = Uno()
        self.assertEqual(uno.is_playing, True)
        uno.play(EXIT)
        self.assertEqual(uno.is_playing, False)

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
        uno.play(DRAW_CARD_INPUT)
        self.assertEqual(len(uno.stack.stack_cards), 96)

    def test_initial_take_card_cards_player_length(self):
        uno = Uno()
        uno.play(DRAW_CARD_INPUT)
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
        play_card = uno.play('1')
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
        uno.play('1')
        # check player_cards length reduced
        self.assertEqual(len(uno.player.cards_player), 5)
        # chek played_card equal to last discard_card
        self.assertEqual(last_played_card, uno.stack.discard_cards[-1])

    def test_player_winner(self):
        uno = Uno()
        uno.stack.discard_cards = [NumberCard(RED, '7')]
        uno.player.cards_player = [NumberCard(GREEN, '7')]
        self.assertEqual(uno.play('1'), 'You WON')

    def test_computer_player_winner(self):
        uno = Uno()
        uno.player.loses_turn = True
        uno.stack.discard_cards = [NumberCard(BLUE, '5')]
        uno.computer_player.cards_player = [NumberCard(YELLOW, '5')]
        self.assertEqual(uno.play(1), 'Computer WON')

    def test_board(self):
        game = Uno()

        # Override cards
        card1 = NumberCard(GREEN, 3)
        card2 = NumberCard(RED, 4)
        card3 = NumberCard(BLUE, 5)
        card4 = NumberCard(BLUE, 6)
        cards = [card1, card2, card3]
        game.player.cards_player = cards
        game.stack.discard_cards.append(card4)

        # Test
        board = game.board
        expected_board = "Your cards are: \n" +\
            "1: 3 - green\n" +\
            "2: 4 - red\n" +\
            "3: 5 - blue\n" +\
            "The last card played is: \n" +\
            "6 - blue"
        self.assertEqual(board, expected_board)

    def test_validate_draw_card_input(self):
        uno = Uno()
        uno.play('')
        self.assertEqual(len(uno.player.cards_player), 8)

    @parameterized.expand([
        ('1 red', (0, 'red')),
        # ('2 blue', (1, 'blue')),
        # ('3 green', (2, 'green')),
        # ('4 yellow', (3, 'yellow')),
        # ('1', (0, None)),
        # ('2', (1, None)),
        # ('3', (2, None)),
    ])
    def test_validate_play_card_input(self, user_input, index_in_hand):
        uno = Uno()
        self.assertEqual(uno.parse_command(user_input), index_in_hand)

    def test_decide_whos_next_player(self):
        uno = Uno()
        self.assertEqual(uno.decide_whos_next(True), uno.player)
        self.assertEqual(uno.decide_whos_next(False), uno.computer_player)

    def test_decide_whos_next_computer_player(self):
        uno = Uno()
        uno.current_player = uno.computer_player
        self.assertEqual(uno.decide_whos_next(True), uno.computer_player)
        self.assertEqual(uno.decide_whos_next(False), uno.player)