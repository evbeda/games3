import unittest
from .models.Player import Player
from .models.LevelHand import LevelHand
from .models.Game import Game
from .models.Monster import Monster
from .models.exceptions.UnplayableCardException import UnplayableCardException


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

    # Monster card
    def _play_power_cards_against_room(self, room, play_a, play_b, play_c):
        handA = LevelHand(Player('A'))
        handB = LevelHand(Player('B'))
        handC = LevelHand(Player('C'))
        handA.play(play_a)
        handB.play(play_b)
        handC.play(play_c)
        room.resolve_room([handA, handB, handC])
        return handA, handB, handC

    def test_jugadores_bajan_531_contra_dragon_y_A_no_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 5, 3, 1)
        self.assertEqual(0, handA.player.wounds)
        
    def test_jugadores_bajan_531_contra_dragon_y_B_no_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 5, 3, 1)
        self.assertEqual(0, handB.player.wounds)

    def test_jugadores_bajan_531_contra_dragon_y_C_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 5, 3, 1)
        self.assertEqual(3, handC.player.wounds)

    def test_jugadores_bajan_554_contra_dragon_y_A_no_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 5, 5, 4)
        self.assertEqual(0, handA.player.wounds)
    
    def test_jugadores_bajan_554_contra_dragon_y_B_no_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 5, 5, 4)
        self.assertEqual(0, handB.player.wounds)

    def test_jugadores_bajan_554_contra_dragon_y_C_no_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 5, 5, 4)
        self.assertEqual(0, handC.player.wounds)

    def test_jugadores_bajan_322_contra_dragon_y_A_no_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 3, 2, 2)
        self.assertEqual(0, handA.player.wounds)

    def test_jugadores_bajan_322_contra_dragon_y_B_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 3, 2, 2)
        self.assertEqual(3, handB.player.wounds)

    def test_jugadores_bajan_322_contra_dragon_y_C_recibe_danio(self):
        handA, handB, handC = \
            self._play_power_cards_against_room(Monster(14, 3), 3, 2, 2)
        self.assertEqual(3, handB.player.wounds)

    



if __name__ == '__main__':
    unittest.main()
