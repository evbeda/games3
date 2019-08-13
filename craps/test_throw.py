import unittest
from throw import Throw
from game import Game
from constants import GAME_IN_PROGRESS, GAME_STARTED


class TestThrow(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.throw = Throw(game=self.game)

    def test_shoots_two_dice(self):
        """Tests that only two dice are thrown."""
        dice = self.throw.shoot()
        dice_count = len(dice)
        self.assertEqual(dice_count, 2)

    def test_dice_shot_numbers(self):
        """Tests that dice numbers are between 1 and 6."""
        dice = self.throw.shoot()
        for die in dice:
            self.assertGreaterEqual(die, 1)
            self.assertLessEqual(die, 6)

    def test_throw_game(self):
        """Tests that every Throw belongs to a Game."""
        self.assertIsNotNone(self.throw.game)

    def test_game_state_changes_when_throw(self):
        """Tests that Game state changes to GAME_IN_PROGRESS after first throw."""
        dice = self.throw.shoot()
        self.throw.change_game_state(dice)
        self.assertEqual(self.game.state, GAME_IN_PROGRESS)


if __name__ == '__main__':
    unittest.main(verbosity=2)
