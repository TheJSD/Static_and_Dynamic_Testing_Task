import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        card1 = Card("Clubs", 1)
        card2 = Card("Hearts", 7)
        card3 = Card("Diamonds", 8)
    
    def test_check_for_ace(self):
        test_result = check_for_ace(card1)
        self.assertEqual(True, test_result)