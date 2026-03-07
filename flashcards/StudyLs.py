from .Card import Card
from .CardLs import CardLs

class StudyLs:

    def __init__(self, cardls):
        self.save_ls, self.cardls = cardls

    def get_ls(self):
        return self.cardls
    
    def get_save_ls(self):
        return self.save_ls
    
    def get(self, index):
        return self.cardls[index]
    
    def get_rand(self):
        return self.cardls.get_rand()
    
    def add(self, card):
        self.cardls.add(card)
    
    def add_card(self, term, deff):
        self.cardls.add_card(term, deff)

    def find(self, search, func):
        self.cardls.find(search, func)

    def shuffle(self):
        self.cardls.shuffle()

    def __str__(self):
        """Prints each card from cardls on its own line"""
        return str(self.cardls)
    