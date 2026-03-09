class Console:
    # TODO add actuall if siwtchbascks (or dict) for command interpretation but learn decorators so can register and new commands to it

# Constructor 
    def __init__(self):
        """
        Simple abstraction class for interacting with console to avoid input and print commands.
        """
        self.hist = list()
        self.log_num = 0
        self.built_in_command_dict = {"exit": self.console_exit} #TODO add help function

# Input in/out/interpret
    def take_in(self)  -> str:
        """
        Serves a a wrapper for input() and logs input from input().
        """
        user_input = input()
        self.log(f"I:{user_input}")
        return user_input
    
    def give_out(self, out:str, endchar="\n") -> None:
        """
        Serves as a wrapper for print() and logs the requested arg out. with optional arg end for print().
        """
        self.log(f"O:{out}{endchar}")
        print(out, end=endchar)
    
    def interpret(self, user_input:str, in_commands:dict) -> Any:
        """
        Takes a given input and matches it to a user provided dict of commands which is then addded to a new dict that includes basic commands, attempts to mtach user_input to a valid command and raises error if not found.
        """
        in_commands = in_commands | self.built_in_command_dict
        try:
            return in_commands[user_input]()
        except KeyError:
            raise InvalidCommand(user_input)
    
    def pass_comm(self) -> None:
        """
        Acts and  None action for as one of of the args in interpret() arg responses
        """
        return None
       
    def ask(self, prompt:str, endchar="\n") -> str:
        """
        Prints arg prompt and returns the next line taken in, with optional arg end for self.give_out() for printing.
        """
        self.give_out(prompt, endchar)
        return self.take_in()
    
    def prompt(self, prompt:str, in_commands:dict, endchar="\n") -> Any:
        """
        Sends a prompt and interperts the input based on the given valid commands and responses. With optional arg end for self.interpret for printing.
        """
        user_input = self.ask(prompt, endchar)
        return self.interpret(user_input, in_commands)
    
    def simple_prompt(self, prompt:str, responses:list, endchar="\n") -> Any:
        """
        Sends a prompt and interperts the input based on the simples commands 'y' and 'n' and responses
        """
        user_input = self.ask(prompt)
        in_commands = zip(["y", "n"], responses)
        return self.interpret(user_input, in_commands, endchar)
    
    def console_exit(self) -> None:
        """
        Console class wrapper of system exit(). Prints a nice goodbye first :).
        """
        print("Goodbye")
        exit()

# Logging methods with self.hist
    def log(self, line:str) -> None: #TODO check what input() returns as for type hint
        """
        Appends line to self.hist. including its number in the logs
        """
        self.hist.append(f"{self.log_num}. {line}")
        self.log_num += 1 #TODO ensure log numbers can't get out of sync

    def print_log(self, log, endchar="\n"):
        """
        Used by Console as a print() wrapper for self.hist.
        """
        print(log, end=endchar)

    def out_log(self, index=-1, endchar="\n") -> None:
        """
        Prints log of given index, defaults to the most recent lines from logs using the print function print_log()
        """
        self.print_log(self.hist[index], endchar)

    def out_logs(self, start=None, end=None, endchar="\n") -> None:
        """
        Prints each log line from given start and end index (inclusive). Defaults to printing full history using the print function print_log()
        """
        # Uses pythonic slicing. [:]=all, [:end]=from begin to end (exclusive), [start:]= from start (inclusive) to end of list. thanks for the reminder chat
        logs = self.hist[start:(None if end is None else end + 1)]

        for log in logs:
            self.print_log(log, endchar)

    def search_logs(self, search:str, limit=True, start=None, end=None, endchar="\n") -> None:
        """
        Searches all of self.hist for given arg search and prints first instance. Can print all instances if limit=False. Also can search in given range if provided and can chnage the print end char if provided as well.
        """
        # Uses pythonic slicing. [:]=all, [:end]=from begin to end (exclusive), [start:]= from start (inclusive) to end of list. thanks for the reminder chat
        logs = self.hist[start:(None if end is None else end + 1)]

        for log in logs:
            if search in log:
                if limit:
                    # only prints first if limited
                    self.print_log(log, endchar)
                    return
                self.print_log(log, endchar)
    
    def tail(self, n=10):
        """
        Unix Style printign of last 10 logs of self.hist
        """
        for log in self.hist[-n:]:
            self.print_log(log)

    # Class Methods
    def __str__(self):
        """
        __str__ for console, prints all logs with start with numbered lines.
        """
        string = ""
        for line in self.hist:
            string += line
        return string

    
# Exceptions
class InvalidCommand (Exception):
    """
    Exception for when the loop in interpret() finishes without finsing a match in commands for input
    """
    def __init__(self, input, message="Input does match list of valid commands"):
        super().__init__(f"{message}: {input}")

class InvalidArgsLen (Exception):
    """
    Exception for when the arg commands and arg responses for interpret() are unequal
    """
    def __init__(self, input1, input2, message="length of arg commands and arg responses do not match"):
        super().__init__(f"{message} len(commands): {input1}, len(responses): {input2}")

class InvalidCommandsListType (Exception):
    """
    Exception for when interpret() arg commands is not of type 'list'
    """
    def __init__(self, input, message="Args commands is not of valid type 'list', GIVEN="):
        super().__init__(f"{message}{input}")

class InvalidResponsesListType (Exception):
    """
    Exception for when interpret() arg responses is not of type 'list'
    """
    def __init__(self, input, message="Arg responses is not of valid type 'list', GIVEN="):
        super().__init__(f"{message}{input}")