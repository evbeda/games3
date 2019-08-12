import unittest
from diez_mil import DiezMil


class TestDiezMil(unittest.TestCase):
    def setUp(self):
        self.game=DiezMil()
    def test_check_players_qty(self):
        checkPlayersQty=self.game.checkPlayersQty(0)
        self.assertEquals(checkPlayersQty, False)    
    def test_check_combination_no_score(self):
        dice=[2,3,3,4,3]
        score=self.game.checkCombination(dice)
        self.assertEquals(score, 0)
    
    def test_check_combination_score(self):
        dice=[1,3,3,4,5]
        score=self.game.checkCombination(dice)
        self.assertEquals(score, 150)
        


if __name__ == '__main__':
    unittest.main()
