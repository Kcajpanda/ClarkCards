from flashcards.Card import Card
from flashcards.CardLs import CardLs

cardTest = False
cardLsTest = True

def class_tests():

    card = Card("T1", "D1")
    card2 = Card("T1", "D1")

    if cardTest:
        print("Card Tests:")
        print(f"- Card.get_term() = {card.get_term()}")
        print(f"- Card.get_defn() = {card.get_defn()}")
        print(f"- str(Card) = {card}")
        print(f"- card == card2 {card==card2}")

    cards = [Card("T2","D2"), Card("T3","D3"), Card("T4","D4"), Card("T5","D5"), Card("T6","D6"), Card("T7","D7")]
    cardls = CardLs(cards)

    if cardLsTest:
        print("CardLs Tests:")
        print(f"- cardls.get(0) = {cardls.get(0)}")
        cardls.add(card)
        print(f"- cardls.add(card)")
        cardls.add_card("T8", "D8")
        print("- cardls.add_card('T8', 'D8')")
        print(f"- str(cardls)\n{cardls}")
        print(f"- cardls.find('T3') = {cardls.find("T3", Card.get_term)}")
        cardls.shuffle()
        print(f"- cardls.shuffle() = print()")
        print(cardls)
        print(f"- cardls.get_rand() = {cardls.get_rand()}")
        print(f"- cardls.get_rand() = {cardls.get_rand()}")
        print("- cardls iter:")
        print(f"- next(cardls) = {next(cardls)}")
        print(f"- next(cardls) = {next(cardls)}")
        print(f"- next(cardls) = {next(cardls)}")
        cardls.start_over()
        print(f"- cardls.start_over()")
        print(f"- next(cardls) = {next(cardls)}")

class_tests()