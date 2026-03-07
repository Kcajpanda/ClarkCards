from flashcards.Card import Card
from flashcards.CardLs import CardLs

card = Card("T1", "D1")

Cards = [card, Card("T2","D2"), Card("T3","D3"), Card("T4","D4"), Card("T5","D5"), Card("T6","D6"), Card("T7","D7")]
# print(type(Cards))
FlashCards = CardLs(Cards)

print(f"card: {card}\n")
print(f"FlashCards\n{FlashCards}")

print(f"{FlashCards.find("T1", Card.get_term)}\n")
FlashCards.shuffle()
print(FlashCards)