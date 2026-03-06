import unittest
from Personal.FlashCards.flashcards.Card import Card

class TestCardMethods (unittest.TestCase):

    def test_get_term(self):
        card = Card("T1","D1")
        self.assertEqual(card.get_term(), "T1")
    

