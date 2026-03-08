import random
from .Card import Card

class CardLs:
     #TODO add __init_ for manually adding cards from console in
    # Constructors
    def __init__(self, cards:list):
        """inits with list of cards becoming self.cards"""
        if isinstance(cards, list):
            self.cards = cards
            self.start_over()
        else:
            raise InvalidCardLsArgType(cards)
    
    # Getters
    def get(self, index:int) -> Card:
        """returns card at given index"""
        if index < 0:
            return 0
        else:
            return self.cards[index]
    
    # Methods
    def add(self, card:Card) -> None:
        """
        Takes give card an input and appends to end of self.cards.
        """
        self.cards.append(card)

    def add_card(self, term, defn) -> None:
        """
        Accepts a term and defn and creates and appends that new card to self.cards
        """
        self.add(Card(term,defn))
    
    def get_rand(self) -> Card:
        """
        Returns a random card from self.cards.
        """
        return random.choice(self.cards)
    
    def find(self, search:str, func) -> Card:
        """
        Searches self.cards for a given string.
        
        func input is used to change search from searching a cards term or defn.
        
        Ex: .find("T1", Card.get_term)
        Ex: .find("D1", Card.get_defn)
        """
        for index, card in enumerate(self.cards):
            if func(card) == search:
                return index
        return -1
    
    def shuffle(self) -> None:
        """
        Shuffles self.cards.
        
        It chooses to random indices and swaps them and repeats random swap operations for at least as many times as half the length of the list and up to 3 times the list's length.
        """
        return random.shuffle(self.cards)
    
    def start_over(self) -> None:
        """
        Resets iter of self.cards.
        """
        self.cards_iter = iter(self.cards)
    
    # Class Methods
    def __next__(self) -> Card:
        return next(self.cards_iter)
    
    def __str__(self):
        """
        Prints each card on its own line.

        EX:
        
        """
        string = ""
        for card in self.cards:
            string += str(card) + "\n"
        return string

    # Exceptions
class InvalidCardLsArgType (Exception):
    """
    Exception for when CardLs __init__ is passed an invalid typr for arg cardls.

    EX:

    """
    def __init__(self, input, message="Error type of arg cardls must be 'list', GIVEN="):
        super().__init__(f"{message}{type(input)}, EXPEC='list'")