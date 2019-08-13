import unittest
from models.Player import Player
from models.Game import Game
from models.exceptions.UnplayableCardException import UnplayableCardException


class TestDungeon(unittest.TestCase):
    # Test del jugador
    def test_init_player(self):
        player = Player('A')
        self.assertEqual(5, len(player.power_cards))

    def test_jugador_con_cartas_431_no_puede_jugar2(self):
        player = Player('A')
        player.play(2)
        player.play(5)
        with self.assertRaises(UnplayableCardException):
            player.play(2)

    def test_actual_card_es_2_si_se_jugo_un2(self):
        player = Player('A')
        player.play(2)
        self.assertEqual(2, player.actual_card)

    def test_si_se_jugo_un3_no_hay_un_3_en_la_mano(self):
        player = Player('A')
        player.play(3)
        self.assertTrue(3 not in player.power_cards)

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
