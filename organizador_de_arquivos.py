import shutil
import pathlib
import os


class FileManager:

    def __init__(self):
        self.source_directory = pathlib.Path(pathlib.Path.home(), "Downloads")
        self.number_of_files_moved = 0
        self.number_of_directories_created = 0
        self.types_of_files = []

    def run(self):
        self.initialize()
        self.get_type_of_files()
        self.create_directories()
        self.move_files()
        self.close()

    def initialize(self):
        print("Inicializando gerenciador de arquivos...")
        print()
        print(f"Diretório fonte   : {self.source_directory}")

    def close(self):
        print()
        print(f"Diretórios criados: {self.number_of_directories_created}")
        print(f"Arquivos movidos  : {self.number_of_files_moved}")
        print()
        print("Encerrando gerenciador de arquivos...")

    def get_type_of_files(self):
        for directory in self.source_directory.glob("*.*"):
            file = str(directory).split("//")[-1]
            type_of_file = file.split(".")[-1]
            if type_of_file not in self.types_of_files:
                self.types_of_files.append(type_of_file)

    def create_directories(self):
        self.number_of_directories_created = 0
        for type_of_file in self.types_of_files:
            path = pathlib.Path(self.source_directory, f"{type_of_file}")
            if not os.path.exists(path):
                os.mkdir(path)
                self.number_of_directories_created += 1

    def move_files(self):
        self.number_of_files_moved = 0
        for type_of_file in self.types_of_files:
            destination_directory = pathlib.Path(self.source_directory, f"{type_of_file}")
            for file_directory in self.source_directory.glob(f"*.{type_of_file}"):
                shutil.move(file_directory, destination_directory)
                self.number_of_files_moved += 1


file_manager = FileManager()
file_manager.run()
