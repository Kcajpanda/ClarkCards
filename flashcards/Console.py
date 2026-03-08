class Console:
    # TODO add way to store history so its not just a priNT and input replacement
    
    def __init__(self):
        """
        Simple abstraction class for interacting with console to avoid input and print commands.
        """
        self.hist = list()

    def take_in(self)  -> str:
        """
        Serves a a wrapper for input() and logs input from input().
        """
        input = input()
        self.log(f"I:{input}")
        return input
    
    def give_out(self, out:str, endchar="\n") -> str:
        """
        Serves as a wrapper for print() and logs the requested arg out. with optional arg end for print().
        """
        self.log(f"O:{out}{endchar}")
        print(out, end=endchar)

    def log(self, line:str) -> None: #TODO check what input() returns as for type hint
        """
        Appends line to self.hist.
        """
        self.hist.append(line)

    def out_log(self, line=0):
        """
        prints the most recent lines from logs
        """
        line = len(self.hist) - 1
        print(self.hist[line])

    def interpret(self, input:str, commands:list, responses:list) -> Any:
        """
        Takes a given string input and finds a matching valid command from commands and returns the response of the same index.
        
        every valid arg commands and arg responses always have "exit" and "self.console_exit()" appended to the end so exit is always possible.
        """
        if isinstance(commands, list):
            if isinstance(responses, list):
                if len(commands) == len(responses):
                    commands.append("exit")
                    responses.append(self.console_exit())
                    for index, com in enumerate(commands):
                        if com == input:
                            return responses[index]
                    raise InvalidCommand(input)
                else:
                    raise InvalidArgsLen(len(commands), len(responses))
            else:
                raise InvalidResponsesListType(type(responses))
        raise InvalidCommandsListType(type(commands))
    
    def pass_comm(self) -> None:
        """
        Acts and  None action for as one of of the args in interpret() arg responses
        """
        return None
       
    def ask(self, prompt:str, end="\n") -> str:
        """
        Prints arg prompt and returns the next line taken in, with optional arg end for self.give_out() for printing.
        """
        self.give_out(prompt, end)
        return self.take_in()
    
    def prompt(self, prompt:str, commands:list, responses:list, end="\n") -> Any:
        """
        Sends a prompt and interperts the input based on the given valid commands and responses. With optional arg end for self.interpret for printing.
        """
        input = self.ask(prompt, end)
        return self.interpret(input, commands, responses)
    
    def simple_prompt(self, prompt:str, responses:list) -> Any:
        """
        Sends a prompt and interperts the input based on the simples commands 'y' and 'n' and responses
        """
        input = self.ask(prompt)
        return self.interpret(input, ["y", "n"], responses)
    
    def console_exit(self) -> None:
        """
        Console class abstraction of system exit(). Prints a nice goodbye first :).
        """
        print("Goodbye")
        exit()

    # Class Methods
    def __str__(self):
        """
        __str__ for console, prints all logs with start with numbered lines.
        """
        string = ""
        for index, line in enumerate(self.hist):
            string += f"{index}. {line}"
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