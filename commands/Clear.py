from commands.Command import Command
import os

class ClearCommand(Command):
    def __init__(self, application):
        super().__init__(application)
        self.signature = "clear"
        self.description = "Clears the console"

    def execute(self):
        os.system('cls')