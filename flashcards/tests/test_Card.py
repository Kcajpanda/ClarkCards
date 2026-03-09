import pytest
from Card import *
from CardLs import *

# cards = [Card("T2","D2"), Card("T3","D3"), Card("T4","D4"), Card("T5","D5"), Card("T6","D6"), Card("T7","D7")]
# cardls = CardLs(cards)

# Card Test Methods
class CardTests:
    def test_card_get_term():
        card = Card("T1","D1")
        assert card.get_term() == "T1"

    def test_card_get_defn():
        card = Card("T1","D1")
        assert card.get_term() == "D1"

    def test_card_str():
        card = Card("T1","D1")
        assert str(card) == "T1 : D1"

    def test_card_eq():
        card = Card("T1","D1")
        card2 = Card("T2","D2")
        card3 = Card("T1","D1")
        assert card.__eq__(card3) == True
        assert card.__eq__(card2) == False

    def test_card_init_error():
        with pytest.raises(InvalidCardArgTypeTerm, match="Error type of arg term cannot be None, GIVEN=None"):
            card = Card(None, "D1")
        with pytest.raises(InvalidCardArgTypeDefn, match="Error type of arg defn cannot be None, GIVEN=None"):
            card = Card("T1", None)

# CardLs Test Methods
# class CardLsTest:
#     def test_cardls_get():
#         cards = [Card("T2","D2"), Card("T3","D3"), Card("T4","D4"), Card("T5","D5"), Card("T6","D6"), Card("T7","D7")]
#         cardls = CardLs(cards)


# if cardLsTest:
#         print("CardLs Tests:")
#         print(f"- cardls.get(0) = {cardls.get(0)}")
#         cardls.add(card)
#         print(f"- cardls.add(card)")
#         cardls.add_card("T8", "D8")
#         print("- cardls.add_card('T8', 'D8')")
#         print(f"- str(cardls)\n{cardls}")
#         print(f"- cardls.find('T3') = {cardls.find("T3", Card.get_term)}")
#         cardls.shuffle()
#         print(f"- cardls.shuffle() = print()")
#         print(cardls)
#         print(f"- cardls.get_rand() = {cardls.get_rand()}")
#         print(f"- cardls.get_rand() = {cardls.get_rand()}")
#         print("- cardls iter:")
#         print(f"- next(cardls) = {next(cardls)}")
#         print(f"- next(cardls) = {next(cardls)}")
#         print(f"- next(cardls) = {next(cardls)}")
#         cardls.start_over()
#         print(f"- cardls.start_over()")
#         print(f"- next(cardls) = {next(cardls)}")

# Card tests
# CardTests.test_card_get_term()
# CardTests.test_card_get_defn()
# CardTests.test_card_str()
# CardTests.test_card_eq()
# CardTests.test_card_init_error()

# jack is 67!!! love sabine
