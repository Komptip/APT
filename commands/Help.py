from commands.Command import Command

class HelpCommand (Command):
    def __init__(self, commands):
        super().__init__(commands)
        self.signature = "help"
        self.description = "Displays all available commands"
    
    def execute(self):
        for command in self.commands.list_commands():
            print(f"{command[0]}: {command[1]}")