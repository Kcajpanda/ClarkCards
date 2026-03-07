import random
from .Card import Card

class CardLs:
     #TODO add __init_ for manually adding cards from console in

    def __init__(self, cards):
        """inits with list of cards becoming self.cards"""
        if isinstance(cards, list):
            self.cards = cards
        else:
            exit(f"error invalid datatype for Cards creation GIVEN={type(cards)}, EXPEC=list")

    def add(self, card):
        """takes give card an input and appends to end of self.cards"""
        self.cards.append(card)

    def add_card(self, term, defn):
        """accepts a term and defn and creates and appends that new card to self.cards"""
        self.add(Card(term,defn))
    
    def get(self, index):
        """returns card at given index"""
        if index < 0:
            return 0
        else:
            return self.cards[index]
        
    def get_rand(self):
        """Returns a random card from self.cards"""
        return random.choice(self.cards)
    
    def find(self, search, func):
        """searches self.cards for a given string.
        
        func input is used to change search from searching a cards term or defn.
        
        Ex: .find("T1", Card.get_term)
        Ex: .find("D1", Card.get_defn)"""
        for index, card in enumerate(self.cards):
            if func(card) == search:
                return index
        return -1
    
    def shuffle(self):
        """Shuffles self.cards.
        
        It chooses to random indices and swaps them and repeats random swap operations for at least as many times as half the length of the list and up to 3 times the list's length"""
        return random.shuffle(self.cards)
    
    def __str__(self):
        """Prints each card on its own line"""
        string = ""
        for card in self.cards:
            string += str(card) + "\n"
        return string