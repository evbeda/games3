import unittest
from parameterized import parameterized
from .const import (
    DRAW_CARD_INPUT, EXIT,
    HUMAN_PLAYER_WON_MESSAGE,
    COMPUTER_WON_MESSAGE,
    INVALID_CARD_MESSAGE,
    RED,
    YELLOW,
    GREEN,
    BLUE,
    )
from .uno import Uno
from .card import NumberCard, ReverseCard, SkipCard

expected_board = '''Your cards are:
1: 3 - green
2: 4 - red
3: 5 - blue
Computer remaining cards: 7
The last card played is:
6 - blue'''


class TestUnoGame(unittest.TestCase):
    def setUp(self):
        self.game = Uno()
        self.STACK_EXAMPLE = [
                            NumberCard(RED, 5),
                            NumberCard(YELLOW, 4)
                        ]

    def test_is_playing(self):
        self.assertEqual(self.game.is_playing, True)
        self.game.play(EXIT)
        self.assertEqual(self.game.is_playing, False)

    def test_current_player(self):
        self.assertEqual(self.game.current_player, self.game.player)

    def test_player_draws(self):
        initial_stack_size = len(self.game.stack.stack_cards)
        initial_player_hand_size = len(self.game.current_player.cards_player)

        self.game.player_draws(self.game.current_player)

        stack_size = len(self.game.stack.stack_cards)
        player_hand_size = len(self.game.current_player.cards_player)

        self.assertEqual(stack_size, initial_stack_size - 1)
        self.assertEqual(player_hand_size, initial_player_hand_size + 1)

    def test_remaining_initial_stack_length(self):
        self.assertEqual(len(self.game.stack.stack_cards), 97)

    def test_initial_cards_player_length(self):
        self.assertEqual(len(self.game.player.cards_player), 7)

    def test_initial_discard_cards_length(self):
        self.assertEqual(len(self.game.stack.discard_cards), 1)

    def test_initial_take_card_stack_length(self):
        self.game.play(DRAW_CARD_INPUT)
        self.assertEqual(len(self.game.stack.stack_cards), 96)
        self.assertEqual(len(self.game.player.cards_player), 8)

    @parameterized.expand([
        (NumberCard(RED, '7'), ),
        (NumberCard(BLUE, '7'), ),
        (NumberCard(YELLOW, '7'), ),
        (ReverseCard(RED), ),
        (SkipCard(RED), ),
    ])
    def test_play_invalid_card(self, card):
        uno = Uno()
        uno.stack.discard_cards = [NumberCard(GREEN, '5')]
        uno.player.cards_player = [card]
        result = uno.play('1')
        expected = INVALID_CARD_MESSAGE
        self.assertEqual(result, expected)
        self.assertEqual(len(uno.player.cards_player), 1)

    @parameterized.expand([
        (NumberCard(RED, '7'), ),
        (NumberCard(BLUE, '7'), ),
        (NumberCard(YELLOW, '7'), ),
        (ReverseCard(RED), ),
        (SkipCard(RED), ),
    ])
    def test_play_a_valid_card(self, card):
        uno = Uno()
        uno.stack.discard_cards = [NumberCard(RED, '7')]
        uno.player.cards_player = [card]
        last_played_card = uno.player.cards_player[0]
        uno.play('1')
        self.assertEqual(len(uno.player.cards_player), 1)
        self.assertEqual(last_played_card, uno.stack.top_card)

    def test_player_winner(self):
        self.game.player.cards_player = []
        self.game.computer_player.cards_player = self.STACK_EXAMPLE
        self.assertEqual(self.game.winner(), HUMAN_PLAYER_WON_MESSAGE)

    def test_computer_player_winner(self):
        self.game.computer_player.cards_player = []
        self.game.player.cards_player = self.STACK_EXAMPLE
        self.assertEqual(self.game.winner(), COMPUTER_WON_MESSAGE)

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
        
        self.assertEqual(board, expected_board)

    def test_validate_draw_card_input(self):
        self.game.current_player = self.game.computer_player
        self.game.player_passes()
        self.assertEqual(len(self.game.computer_player.cards_player), 8)

    def test_player_pass_his_turn(self):
        self.game.player_passes()
        self.assertEqual(self.game.current_player, self.game.player)
        self.game.player_passes()
        self.assertEqual(self.game.computer_player, self.game.current_player)

    @parameterized.expand([
        ('1 red', (0, 'red')),
        ('2 blue', (1, 'blue')),
        ('3 green', (2, 'green')),
        ('4 yellow', (3, 'yellow')),
        ('1', (0, None)),
        ('2', (1, None)),
        ('3', (2, None)),
    ])
    def test_validate_play_card_input(self, user_input, index_in_hand):
        self.assertEqual(self.game.parse_command(user_input), index_in_hand)

    def test_decide_whos_next_player(self):
        self.assertEqual(
            self.game.decide_whos_next(False), self.game.computer_player
            )
        self.assertEqual(
                self.game.decide_whos_next(True), self.game.player
            )

    def test_decide_whos_next_computer_player(self):
        self.game.current_player = self.game.computer_player
        self.assertEqual(
            self.game.decide_whos_next(False), self.game.player)
        self.assertEqual(
            self.game.decide_whos_next(True), self.game.computer_player
            )
