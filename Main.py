from Gemini import Gemini
from FileProcessor import FileProcessor
from Project import Project
import os

import config.gemini
import config.file

class Main:
	def __init__(self):
		self.exit = False

		self.gemini = Gemini(config.gemini.config)
		self.fileProcessor = FileProcessor(config.file.config)
		
		self.directory = None
		self.directory_content = None

		self.commands = {
			"q": {
				"execute": self.exitCmd,
				"description": "Exits the program"
			},
			"help": {
				"execute": self.helpCmd,
				"description": "Displays all available commands"
			},
			"cls": {
				"execute": self.clearCmd,
				"description": "Clears the console"
			},

			"run": {
				"execute": self.runCmd,
				"description": "Runs the Gemini model with the input text"
			},

			"project:new": {
				"execute": self.createProjectCmd,
				"description": "Creates a new project"
			},

			"project:load": {
				"execute": self.loadProjectCmd,
				"description": "Loads an existing project"
			},

			"project:save": {
				"execute": self.saveProjectCmd,
				"description": "Saves the current project"
			},

			"project:dir:set": {
				"execute": self.setDirectoryCmd,
				"description": "Sets the directory for the project"
			},

			"project:dir": {
				"execute": self.showDirectoryCmd,
				"description": "Shows the current directory"
			},

			"project:chat:history:print": {
				"execute": self.printChatHistoryToFileCmd,
				"description": "Prints the chat history to a file"
			}
		}

	def exitCmd(self):
		self.exit = True

		if self.project:
			self.project.save()

	def helpCmd(self):
		print("Available commands:")
		for command in self.commands:
			print(command + " - " + self.commands[command]["description"])


	def runCmd(self):
		text = input(": ")
		print(self.gemini.run(text).text)

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

	def clearCmd(self):
		os.system('cls')

	def run(self):
		while not self.exit:
			command = input("Enter command: ")

			if command in self.commands:
				self.commands[command]["execute"]()
			else:
				print("Command not found - type help to see all available commands")

		print("Execution finished")

interface = Main()
interface.run()