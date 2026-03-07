from .Card import Card
from .CardLs import CardLs
from .StudyLs import StudyLs
from .Console import Console

class StudySess:

    def __init__(self, cards):
        self.studyls = StudyLs(CardLs(cards))
        self.console = Console()

    def shuffle(self):
        self.studyls.shuffle()

    def next_card(self):
        next(self.studyls)

    def start_over(self):
        self.studyls.start_over()

    def flash_loop(self):
        self.console.simple_prompt("Shuffle Set?", [self.studyls.shuffle, self.console.pass_comm()])
        while(True):
            try:
                card = next(self.studyls)
                self.console.prompt(str(card.get_term()), ["", "f"], [self.console.give_out(card.get_defn), self.console.give_out(card.get_defn)])
            except StopIteration:
                self.console.simple_prompt("Set Completed. Continue?", [self.console.pass_comm(), self.console.console_exit()])
                break
        self.flash_loop()
        
