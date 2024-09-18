from commands.Clear import ClearCommand
from commands.Help import HelpCommand
from commands.Quit import QuitCommand
from commands.Run import RunCommand

class Commands:
    def __init__(self, application):
        self.application = application
        self.commands = []
        self.load_commands()

    def add_command(self, command):
        self.commands.append(command)

    def load_commands(self):
        self.add_command(RunCommand(self))
        self.add_command(HelpCommand(self))
        self.add_command(QuitCommand(self))
        self.add_command(ClearCommand(self))

    def find_command(self, signature):
        for command in self.commands:
            if command.signature == signature:
                return command
        return None
    
    def list_commands(self):
        cmd_list = []
        for command in self.commands:
            cmd_list.append([command.signature, command.description])

        return cmd_list