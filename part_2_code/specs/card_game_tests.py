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

    def test__highest_card(self):
        test_result = self.cardgame.highest_card(self, self.card_1, self.card_2)
        self.assertEqual(self.card_2, test_result)

    def test__cards_total(self):
        test_result = self.cardgame.cards_total(self, self.cards)
        self.assertEqual("You have a total of" + str(16), test_result)
    