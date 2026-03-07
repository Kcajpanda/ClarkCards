class Card:
    def __init__(self, term, defn):
        """Creates a card object with two inputs storing them as term and defn
        
        meant to serve a object abstracting a flashcard: front and back, or term and defn"""
        if not term is None:
            if not defn is None:
                self.term, self.defn = term, defn
            else:
                exit(f"Error invalid datatype for Card defn creation GIVEN={type(defn)}, cannot be Nonetype")
        else:
            exit(f"Error invalid datatype for Card term creation GIVEN={type(term)}, cannot be Nonetype")
    
    # Getter and Setter
    def get_term(self):
        """returns a cards term"""
        return self.term
    
    def get_defn(self):
        """returns a cards defn"""
        return self.defn
    
    #Class Methods
    def __str__(self):
        """__str__ for Card class, prints term then defn seperated by _:_ ending with a linebreak"""
        return f"{self.term} : {self.defn}"
    
    def __eq__(self, obj):
        """__eq__ for Card, checks if its a type(Card) and then makes sure its term and fen are the same as the obj."""
        if isinstance(obj, self):
            if self.term == obj.term:
                if self.defn == obj.defn:
                    return True
        return False