class Card:

    # Constructors
    def __init__(self, term, defn): 
        """
        Creates a card object with two inputs storing them as term and defn.
        
        Meant to serve a object abstracting a flashcard: front and back, or term and defn.
        """
        if not term is None:
            if not defn is None:
                self.term, self.defn = term, defn
            else:
                raise InvalidCardArgTypeDefn(defn)
        else:
            raise InvalidCardArgTypeTerm(term)
    
    # Getters
    def get_term(self) -> Any:
        """
        Returns a cards term.
        """
        return self.term
    
    def get_defn(self) -> Any:
        """
        Returns a cards defn.
        """
        return self.defn
    
    # Class Methods
    def __str__(self):
        """
        __str__ for Card class, prints term then defn seperated by _:_ ending with a linebreak.
        """
        return f"{self.term} : {self.defn}"
    
    def __eq__(self, obj):
        """
        __eq__ for Card, checks if its a type(Card) and then makes sure its term and fen are the same as the obj.
        """
        if isinstance(obj, Card):
            if self.term == obj.term:
                if self.defn == obj.defn:
                    return True
        return False

# Exceptions
class InvalidCardArgTypeTerm (Exception):
    """
    Exception for when Card __init__ is passed an Nonetype for arg term.

    EX:

    """
    def __init__(self, input, message="Error type of arg term cannot be None, GIVEN="):
        super().__init__(f"{message}{type(input)}")

class InvalidCardArgTypeDefn (Exception):
    """
    Exception for when Card __init__ is passed an Nonetype for arg defn.

    EX:

    """
    def __init__(self, input, message="Error type of arg defn cannot be None, GIVEN="):
        super().__init__(f"{message}{type(input)}")