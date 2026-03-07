from .Card import Card
from .CardLs import CardLs
from .StudyLs import StudyLs
from .Console import Console

class StudySess:

    def __init__(self, cards:list) -> StudySess:
        """
        Engine Class that runs a StudyLs and allows intercation with it and user through a console.
        """
        self.studyls = StudyLs(CardLs(cards))
        self.console = Console()

    def shuffle(self) -> None:
        """
        Abstraced shuffle of mutable CardLs in StudyLs
        """
        self.studyls.shuffle()

    def next_card(self) -> Card:
        """
        Abstracted next() of mutable Cardls in StudyLs.
        """
        next(self.studyls)

    def start_over(self) -> None:
        """
        Abstracted start_over() of mutable Cardls in StudyLs
        """
        self.studyls.start_over()

    def flash_loop(self) -> None:
        """
        Loop for flashcards, begins by simple_prompt (yes/no) for shuffle then begns loop for prompting each card.defn then waiitng for either "" or "f". continues till set completes or exit(). after which user is simple prompted if they want to continu => call loop again else exits.
        """
        self.console.simple_prompt("Shuffle Set?", [self.studyls.shuffle, self.console.pass_comm()])
        while(True):
            try:
                card = next(self.studyls)
                self.console.prompt(str(card.get_term()), ["", "f"], [self.console.give_out(card.get_defn), self.console.give_out(card.get_defn)])
            except StopIteration:
                self.console.simple_prompt("Set Completed. Continue?", [self.console.pass_comm(), self.console.console_exit()])
                break
        self.flash_loop()
        
