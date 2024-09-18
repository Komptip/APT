from Gemini import Gemini
from FileProcessor import FileProcessor
from Project import Project

import config.gemini
import config.file

from Commands import Commands

class App:
	def __init__(self):
		self.exit = False

		self.gemini = Gemini(config.gemini.config)
		self.fileProcessor = FileProcessor(config.file.config)
		
		self.directory = None
		self.directory_content = None

		self.init_commands()

	def init_commands(self):
		self.commands = Commands(self)

	def createProjectCmd(self):
		name = input("Enter project name: ")
		self.project = Project(name)
		self.gemini.set_project(self.project)
		self.project.set_gemini(self.gemini)
		self.project.save()
		print("Project created")

	def loadProjectCmd(self):
		name = input("Enter project name: ")

		if not self.fileProcessor.file_exists("Projects/" + name + "/config.json"):
			return print("Project not found")
			

		self.project = Project.load_from_file(name)
		self.gemini.set_project(self.project)
		self.project.set_gemini(self.gemini)
		print("Project loaded")

	def saveProjectCmd(self):
		self.project.save()
		print("Project saved")

	def setDirectoryCmd(self):
		directory = input("Enter directory: ")

		if not self.fileProcessor.directory_exists(directory):
			return print("Directory not found")

		self.project.setDirectory(directory)
		print("Directory set")
		
	def showDirectoryCmd(self):
		if self.project.getDirectory():
			print(self.project.getDirectory())
		else:
			print("No directory set")

	def printChatHistoryToFileCmd(self):
		print(self.project.getChatHistory())

	def run(self):
		while not self.exit:
			signature = input("Enter command: ")

			command = self.commands.find_command(signature)

			if command:
				command.execute()
			else:
				print("Command not found")

if(__name__ == "__main__"):
	app = App()
	app.run()