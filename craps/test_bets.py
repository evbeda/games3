import unittest
from unittest.mock import patch
from parameterized import parameterized
from .game import CrapsGame
from .turn import Turn
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_STARTED,
    GAME_IN_PROGRESS,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
)


class TestBets(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()
