import os
import time
from tqdm import tqdm
import os
from config.file import config
from tqdm import tqdm


class FileProcessor:
    def __init__(self, config):
        self.config = config
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def set_base_path(self, base_path):
        self.base_path = base_path

    def read_directory(self, directory):
        texterisedContent = ''

        for root, dirs, files in tqdm(os.walk(directory)):
            [dirs.remove(d) for d in list(dirs) if d in config['exclude']]
            
            for filename in files:
            
                if filename.endswith(config['required_extesions']) and not filename.endswith(config['disabled_extensions']):

                    if filename not in config['ignore']:
                    
                        file_path = os.path.join(root, filename)

                        content = self.read_file(file_path)

                        texterisedContent += f"\n##### GEMINI FILE START {file_path} #####\n"
                        texterisedContent += content
                        texterisedContent += f'\n##### GEMINI FILE END #####\n'

                        print(file_path, len(content))

        return texterisedContent
    
    def path(self, file):
        if not os.path.isabs(file):
            return os.path.join(self.base_path, file)
        return file
    
    def create_folder(self, folder):
        folder = self.path(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    def list_files(self, directory):
        directory = self.path(directory)
        fileList = []
        for root, dirs, files in tqdm(os.walk(directory)):
            [dirs.remove(d) for d in list(dirs) if d in config['exclude']]
            
            for filename in files:
            
                if filename.endswith(config['required_extesions']) and not filename.endswith(config['disabled_extensions']):

                    if filename not in config['ignore']:
                    
                        file_path = os.path.join(root, filename)

                        fileList.append(file_path)

        return fileList
    
    def read_file(self, file_path):
        file_path = self.path(file_path)
        with open(file_path, 'r', encoding="utf8") as file:
            return file.read()

    def write_to_file(self, output_file, texterisedContent):
        output_file = self.path(output_file)

        if not os.path.exists(os.path.dirname(output_file)):
            os.makedirs(os.path.dirname(output_file))

        with open(output_file, 'w', encoding="utf8") as file:
            file.write(texterisedContent)
        
    def insert_after_line(self, file, line, content):
        file = self.path(file)
        content = content + '\n'
        with open(file, 'r', encoding="utf8") as f:
            lines = f.readlines()
        lines.insert(line, content)
        with open(file, 'w', encoding="utf8") as f:
            f.writelines(lines)

    def replace_line(self, file, line, content):
        file = self.path(file)
        content = content + '\n'
        with open(file, 'r', encoding="utf8") as f:
            lines = f.readlines()
        lines[line] = content
        with open(file, 'w', encoding="utf8") as f:
            f.writelines(lines)

    def file_exists(self, file):
        file = self.path(file)
        return os.path.exists(file)
    
    def directory_exists(self, directory):
        directory = self.path(directory)
        return os.path.exists(directory)