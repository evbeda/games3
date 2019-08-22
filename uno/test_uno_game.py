import unittest
from .const import DRAW_CARD_INPUT, EXIT
from parameterized import parameterized
from .uno import Uno


class TestUnoGame(unittest.TestCase):
    def setUp(self):
        self.game = Uno()

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
        
    # def test_player_plays_card(self):
        # initial_stack_size = len(self.game.stack.stack_cards)
        # initial_player_hand_size = len(self.game.current_player.cards_player)

        # self.game.player_plays_card(self.game.current_player, )

        # stack_size = len(self.game.stack.stack_cards)
        # player_hand_size = len(self.game.current_player.cards_player)

        # self.assertEqual(stack_size, initial_stack_size - 1)
        # self.assertEqual(player_hand_size, initial_player_hand_size + 1)

    def test_remaining_initial_stack_length(self):
        self.assertEqual(len(self.game.stack.stack_cards), 97)

    def test_initial_cards_player_length(self):
        self.assertEqual(len(self.game.player.cards_player), 7)

    def test_initial_discard_cards_length(self):
        self.assertEqual(len(self.game.stack.discard_cards), 1)

    def test_initial_take_card_stack_length(self):
        uno = Uno()
        uno.play(DRAW_CARD_INPUT)
        self.assertEqual(len(uno.stack.stack_cards), 96)
        self.assertEqual(len(uno.player.cards_player), 8)

    # def test_play_invalid_card(self):
    #     uno = Uno()
    #     uno.stack.discard_cards = [NumberCard(GREEN, '5')]
    #     uno.player.cards_player = [
    #         NumberCard(RED, '7'),
    #         NumberCard(BLUE, '7'),
    #         NumberCard(YELLOW, '7'),
    #         ReverseCard(RED),
    #         SkipCard(RED),
    #         DrawTwoCard(RED),
    #     ]
    #     result = uno.play('1')
    #     expected = INVALID_CARD_MESSAGE
    #     self.assertEqual(result, expected)
    #     self.assertEqual(len(uno.player.cards_player), 6)

    # def test_play_a_valid_card(self):
    #     uno = Uno()
    #     uno.stack.discard_cards = [NumberCard(RED, '7')]
    #     uno.player.cards_player = [
    #         NumberCard(GREEN, '7'),
    #         NumberCard(BLUE, '7'),
    #         NumberCard(YELLOW, '7'),
    #         ReverseCard(RED),
    #         SkipCard(RED),
    #         DrawTwoCard(RED),
    #     ]
    #     last_played_card = uno.player.cards_player[0]
    #     uno.play('1')
    #     # check player_cards length reduced
    #     self.assertEqual(len(uno.player.cards_player), 5)
    #     # check played_card equal to last discard_card
    #     self.assertEqual(last_played_card, uno.stack.discard_cards[-1])

    # def test_player_winner(self):
        # uno = Uno()
        # uno.stack.discard_cards = [NumberCard(RED, '7')]
        # uno.player.cards_player = [NumberCard(GREEN, '7')]
        # self.assertEqual(uno.play(1), 'You WON')

    # def test_computer_player_winner(self):
        # uno = Uno()
        # uno.player.loses_turn = True
        # uno.stack.discard_cards = [NumberCard(BLUE, '5')]
        # uno.computer_player.cards_player = [NumberCard(YELLOW, '5')]
        # self.assertEqual(uno.play(1), 'Computer WON')

    # def test_board(self):
        # game = Uno()

        # # Override cards
        # card1 = NumberCard(GREEN, 3)
        # card2 = NumberCard(RED, 4)
        # card3 = NumberCard(BLUE, 5)
        # card4 = NumberCard(BLUE, 6)
        # cards = [card1, card2, card3]
        # game.player.cards_player = cards
        # game.stack.discard_cards.append(card4)

        # # Test
        # board = game.board
        # expected_board = "Your cards are: \n" +\
            # "1: 3 - green\n" +\
            # "2: 4 - red\n" +\
            # "3: 5 - blue\n" +\
            # "The last card played is: \n" +\
            # "6 - blue"
        # self.assertEqual(board, expected_board)

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
        self.assertEqual(uno.decide_whos_next(False), uno.player)
        self.assertEqual(uno.decide_whos_next(True), uno.computer_player)

    def test_decide_whos_next_computer_player(self):
        uno = Uno()
        uno.current_player = uno.computer_player
        self.assertEqual(uno.decide_whos_next(False), uno.computer_player)
        self.assertEqual(uno.decide_whos_next(True), uno.player)
