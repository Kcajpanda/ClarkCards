class Card:
    def __init__(self, term, defn):
        """Creates a card object with two inputs storing them as term and defn
        
        meant to serve a object abstracting a flashcard: front and back, or term and defn"""
        self.term, self.defn = term, defn
    
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


            
# class Console:
#     # TODO add way to store history so its not just a priNT and input replacement
    
#     def __init__(self):
#         """Simple abstraction class for interacting with console to avoid input and print commands"""
#         self.hist = list()

#     def take_in(self):
#         """Serves a a wrapper for input()"""
#         return input()
    
#     def take_out(self, out):
#         """Serves as a wrapper for print()"""
#         print(out)

#     def interpret(self, command):
#         if command == "exit":
#             print("Goodbye!")
#             exit()
#         elif command == "1":
#             pass