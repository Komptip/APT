import pathlib
import textwrap

import google.generativeai as genai


class Gemini:

    def __init__(self, config):
        genai.configure(api_key='YOUR_API_KEY')
        self.config = config
        self.chat = None
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest', system_instruction=self.config['instructions'], tools=[self.get_project_file_list, self.read_file, self.write_file, self.insert_after_line, self.replace_full_line])

    def get_project_file_list(self, filesOnly: bool) -> str:
        print("Getting project file list called ", filesOnly)
        project_files = self.project.directoryFileProcessor.list_files(self.project.getDirectory())
        self.project.save()
        return project_files
    
    def read_file(self, file: str) -> str:
        print("Reading file called with file: ", file)
        content = self.project.directoryFileProcessor.read_file(file)
        self.project.save()
        return content
    
    def write_file(self, file: str, content: str) -> None:
        print("Writing file called with file: ", file)
        self.project.directoryFileProcessor.write_to_file(file, content.encode('utf-8').decode('unicode_escape'))
        self.project.save()

    def insert_after_line(self, file: str, line: float, content: str) -> None:
        line = int(line)
        print("Inserting content after line: ", line, " in file: ", file)
        self.project.directoryFileProcessor.insert_after_line(file, line, content.encode('utf-8').decode('unicode_escape'))
        self.project.save()

    def replace_full_line(self, file: str, line: float, content: str) -> None:
        line = int(line)
        print("Replacing line: ", line, " in file: ", file)
        self.project.directoryFileProcessor.replace_line(file, line, content.encode('utf-8').decode('unicode_escape'))
        self.project.save()
    
    def set_project(self, project):
        self.project = project
        self.chat = None

    def run(self, prompt):
        if not self.project:
            return "No project loaded"
        
        if not self.chat:
            history = self.project.getChatHistory()
            if not history:
                history = [
                    {'role': 'user', 'parts': [self.config['instructions']]},
                    {'role': 'model', 'parts': ['OK I understand. I will do my best!']}
                ]

            self.chat = self.model.start_chat(history=history, enable_automatic_function_calling=True)

        return self.chat.send_message(prompt)