import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.cardgame= CardGame
        self.card_1 = Card("diamonds", 5)
        self.card_2 = Card("hearts", 10)
        self.card_3 = Card("clubs", 1)
        self.cards = [self.card_1, self.card_2, self.card_3]

    def test__check_for_ace(self):
        test_result = self.cardgame.check_for_ace(self, self.card_3)
        self.assertTrue(test_result)

    