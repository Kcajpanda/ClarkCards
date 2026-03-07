class Console:
    # TODO add way to store history so its not just a priNT and input replacement
    
    def __init__(self):
        """Simple abstraction class for interacting with console to avoid input and print commands"""
        self.hist = list()

    def take_in(self):
        """Serves a a wrapper for input() and logs input from input()"""
        input = input()
        self.log(input)
        return input
    
    def give_out(self, out, endchar="\n"):
        """Serves as a wrapper for print() and logs the requested arg out"""
        self.log(f"{out}{endchar}")
        print(out, end=endchar)

    def log(self, line):
        """Appends line to self.hist"""
        self.hist.append(line)

    def interpret(self, input, commands, responses):
        """takes a given string input and finds a matching valid command from commands and returns the response of the same index.
        
        every valid arg commands and arg responses always have "exit" and "self.console_exit()" appended to the end so exit is always possible"""
        if isinstance(commands, list):
            if isinstance(responses, list):
                if len(commands) == len(responses):
                    commands.append("exit")
                    responses.append(self.console_exit())
                    for index, com in enumerate(commands):
                        if com == input:
                            return responses[index]
                    raise self.InvlaidCommand(input)
                else:
                    raise self.InvlaidArgsLen(len(commands), len(responses))
            else:
                raise self.InvlaidResponsesListType(type(responses))
                # why the self. ?
        raise self.InvlaidCommandsListType(type(commands))
    
    def pass_comm(self):
        """acts and  None action for as one of of the args in interpret() arg responses"""
        return None
       
    def ask(self, prompt, end="\n"):
        """Prints arg prompt and returns the next line taken in"""
        self.give_out(prompt, end)
        return self.take_in()
    
    def prompt(self, prompt, commands, responses, end="\n"):
        """Sends a prompt and interperts the input based on the given valid commands and responses"""
        input = self.ask(prompt, end)
        return self.interpret(input, commands, responses)
    
    def simple_prompt(self, prompt, responses):
        """Sends a prompt and interperts the input based on the simples commands 'y' and 'n' and responses"""
        input = self.ask(prompt)
        return self.interpret(input, ["y", "n"], responses)
    
    def console_exit(self):
        print("Goodbye")
        exit()

    
# Exceptions
    class InvlaidCommand (Exception):
        """Exception for when the loop in interpret() finishes without finsing a match in commands for input"""
        def __init__(self, input, message="Input does match list of valid commands"):
            super().__init__(f"{message}: {input}")
    
    class InvlaidArgsLen (Exception):
        """Exception for when the arg commands and arg responses for interpret() are unequal"""
        def __init__(self, input1, input2, message="length of arg commands and arg responses do not match"):
            super().__init__(f"{message} len(commands): {input1}, len(responses): {input2}")

    class InvlaidCommandsListType (Exception):
        """Exception for when interpret() arg commands is not of type 'list'"""
        def __init__(self, input, message="Args commands is not of valid type 'list', GIVEN="):
            super().__init__(f"{message}{input}")
    
    class InvlaidResponsesListType (Exception):
        """Exception for when interpret() arg responses is not of type 'list'"""
        def __init__(self, input, message="Arg responses is not of valid type 'list', GIVEN="):
            super().__init__(f"{message}{input}")