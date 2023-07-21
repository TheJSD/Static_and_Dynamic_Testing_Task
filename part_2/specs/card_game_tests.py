import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Hearts", 7)
        self.card3 = Card("Diamonds", 8)
        # self.cards = self.card1 + self.card2 + self.card3
    
    def test_check_for_ace(self):
        test_result = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, test_result)

    def test_check_for_highest_card(self):
        highest_card = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, highest_card)
    
    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 16", CardGame.cards_total(self, cards))