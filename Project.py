from FileProcessor import FileProcessor
import config.file
import json
import jsonpickle

class Project:

    def __init__(self, name):
        self.data = {
            "directory": None
        }
        self.name = name
        self.newly_created = True
        self.FileProcessor = FileProcessor(config.file.config)
        self.FileProcessor.base_path = self.FileProcessor.path("Projects")

    def save(self):
        if self.newly_created:
            self.FileProcessor.create_folder(self.name)
            self.FileProcessor.base_path = self.FileProcessor.path(self.name)
            self.newly_created = False
        else:
            if(self.gemini.chat is not None):
                self.data['chat_history'] = jsonpickle.encode(self.gemini.chat.history)
            else:
                self.data['chat_history'] = None
    
        self.FileProcessor.write_to_file("config.json",  json.dumps(self.data))
    
    def set_gemini(self, gemini):
        self.gemini = gemini

    def getChatHistory(self):
        if "chat_history" in self.data:
            if not self.data["chat_history"] is None:
                return jsonpickle.decode(self.data["chat_history"])
        
        return None
    
    def getRawChatHistory(self):
        if "chat_history" in self.data:
            return self.data["chat_history"]

        return None

    def setDirectory(self, directory):
        self.data['directory'] = directory
        self.directoryFileProcessor = FileProcessor(config.file.config)
        self.directoryFileProcessor.base_path = directory

    def getDirectory(self):
        return self.data['directory']

    @staticmethod
    def load_from_file(file):
        project = Project(file)
        project.FileProcessor.base_path = project.FileProcessor.path(file)
        project.data = json.loads(''.join(project.FileProcessor.read_file("config.json")))
        project.newly_created = False
        project.setDirectory(project.data['directory'])
        return project