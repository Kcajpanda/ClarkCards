from .Card import Card
from .CardLs import CardLs

class StudyLs:

    def __init__(self, cardls):
        if isinstance(cardls, CardLs):
            self.save_ls, self.cardls = cardls
        else:
            exit(f"Error invalid datatype for StudyLs creation GIVEN={type(cardls)}, EXPEC=CardLs")

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
    
    def start_over(self):
        self.cardls.start_over()

    def __next__(self):
        return next(self.cardls)

    def __str__(self):
        """Prints each card from cardls on its own line"""
        return str(self.cardls)
    