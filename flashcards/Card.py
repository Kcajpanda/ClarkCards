# plan.
# 1. build structure of card, set, and terminal interaction, score keeper?
# 2. build way to take in csv and make cards
# 3. make way to study cards flashcard style
# 4. make way to to do "learn style" stuff
# 5. build AI integration to gen other learn answers

import random

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

class Set:
     #TODO add __init_ for manually adding cards from console in

    def __init__(self, cards):
        """inits with list of cards becoming self.cards"""
        if isinstance(card, list):
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
    
    def find(self, search, func):
        """searches self.cards for a given string.
        
        func input is used to change search from searching a cards term or defn.
        
        Ex: .find("T1", Card.get_term)
        Ex: .find("D1", Card.get_defn)"""
        for index, card in enumerate(self.cards):
            if func(card) == search:
                return index
    
    def shuffle(self):
        """Returns a shuffled version of self.cards not altering orignal.
        
        It chooses to random indices and swaps them and repeats random swap operations for at least as many times as half the length of the list and up to 3 times the list's length"""
        temp_ls, length, end_index = self.cards.copy(), len(self.cards), len(self.cards)-1
        num_times = length + random.randint(length//2,length*3)

        for i in range(num_times):
            rand_num1, rand_num2 = random.randint(0,end_index), random.randint(0,end_index)
            temp = temp_ls[rand_num1]

            temp_ls[rand_num1] = temp_ls[rand_num2]
            temp_ls[rand_num2] = temp
        
        return temp_ls
    
    def __str__(self):
        """Prints each card on its own line"""
        string = ""
        for card in self.cards:
            string += str(card) + "\n"
        return string
            
class Console:
    # TODO add way to store history so its not just a priNT and input replacement
    
    def __init__(self):
        """Simple abstraction class for interacting with console to avoid input and print commands"""
        self.hist = list()

    def take_in(self):
        """Serves a a wrapper for input()"""
        return input()
    
    def take_out(self, out):
        """Serves as a wrapper for print()"""
        print(out)

    def interpret(self, command):
        if command == "exit":
            print("Goodbye!")
            exit()
        elif command == "1":
            pass

# Main
card = Card("T1", "D1")

Cards = [card, Card("T2","D2"), Card("T3","D3"), Card("T4","D4"), Card("T5","D5"), Card("T6","D6"), Card("T7","D7")]
FlashCards = Set(Cards)

print(card)
print()
print(FlashCards)

print(FlashCards.find("T1", Card.get_term))
print()

FlashCards.shuffle()
print(FlashCards)