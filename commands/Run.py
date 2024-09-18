from commands.Command import Command

class RunCommand(Command):

    def __init__(self, application):
        super().__init__(application)
        self.signature = "run"
        self.description = "Runs the Gemini model with the input text"
    
    def execute(self):
        text = input(": ")
        print(self.application.gemini.run(text).text)