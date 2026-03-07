from .Card import Card
from .CardLs import CardLs
import copy

class StudyLs:

    def __init__(self, cardls:CardLs) -> StudyLs:
        """
        Wrapper for CardLs that allows a saved copy of orignal to be preserved and retored as needed.
        """
        if isinstance(cardls, CardLs):
            self.save_ls, self.cardls = cardls
        else:
            exit(f"Error invalid datatype for StudyLs creation GIVEN={type(cardls)}, EXPEC=CardLs")

    # Getters
    def get_ls(self) -> CardLs:
        """
        Returns mutable CardLs (self.cardls).
        """
        return self.cardls
    
    def get_save_ls(self) -> CardLs:
        """
        Returns saved CardLs (self.save_ls).
        """
        return self.save_ls
    
    def get(self, index) -> Card:
        """
        Abstracted get() of the mutable CardLs (self.cardls).
        """
        return self.cardls[index]
    
    # Methods
    def restore(self) -> None:
        """
        Restores self.cardls to same order as self.save_ls
        """
        self.cardls = copy.copy(self.save_ls)

    def add(self, card:Card) -> None:
        """
        Abstracted add() of the mutable CardLs (self.cardls).
        """
        self.cardls.add(card)
    
    def add_card(self, term, deff) -> None:
        """
        Abstracted add_card() of the mutable CardLs (self.cardls).
        """
        self.cardls.add_card(term, deff)
    
    def get_rand(self) -> Card:
        """
        Abstracted get_rand() of the mutable CardLs (self.cardls).
        """
        return self.cardls.get_rand()

    def find(self, search, func) -> Card:
        """
        Abstracted find() of the mutable CardLs (self.cardls).
        """
        self.cardls.find(search, func)

    def shuffle(self) -> None:
        """
        Abstracted shuffle() of the mutable CardLs (self.cardls).
        """
        self.cardls.shuffle()
    
    def start_over(self) -> None:
        """
        Abstracted resets iter() of the mutable CardLs (self.cardls).
        """
        self.cardls.start_over()

    # Class Methods
    def __next__(self) -> Card:
        """
        Abstracted next() of the mutable CardLs (self.cardls).
        """
        return next(self.cardls)

    def __str__(self):
        """
        Prints each card from mutable CardLs (self.cardls) on its own line.
        """
        return str(self.cardls)
    