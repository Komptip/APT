from commands.Command import Command

class QuitCommand(Command):
    def __init__(self, commands):
        super().__init__(commands)
        self.signature = "quit"
        self.description = "Quits the application"

    def execute(self):
        self.application.exit = True
        
        if self.application.project:
            self.application.project.save()