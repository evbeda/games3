import unittest
from models.Player import Player
from models.LevelHand import LevelHand
from models.Game import Game
from models.exceptions.UnplayableCardException import UnplayableCardException


class TestDungeon(unittest.TestCase):
    # Test del jugador
    def test_init_player(self):
        hand = LevelHand(Player('A'))
        self.assertEqual(5, len(hand.cards_to_play))

    def test_jugador_con_cartas_431_no_puede_jugar2(self):
        hand = LevelHand(Player('A'))
        hand.play(2)
        hand.play(5)
        with self.assertRaises(UnplayableCardException):
            hand.play(2)

    def test_actual_card_es_2_si_se_jugo_un2(self):
        hand = LevelHand(Player('A'))
        hand.play(2)
        self.assertEqual(2, hand.last_card_played)

    def test_si_se_jugo_un3_no_hay_un_3_en_la_mano(self):
        hand = LevelHand(Player('A'))
        hand.play(3)
        self.assertTrue(3 not in hand.cards_to_play)

    # Game
    def test_gana_el_jugador_A(self):
        playerA = Player('A')
        playerB = Player('B')
        playerC = Player('C')
        playerA.gold = 50
        playerA.wounds = 10
        playerB.gold = 40
        playerB.wounds = 15
        playerC.gold = 60
        playerC.wounds = 20
        game = Game([playerA, playerB, playerC])
        self.assertEqual(playerA, game.get_winner())

    # Room card


if __name__ == '__main__':
    unittest.main()
