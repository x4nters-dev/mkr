from os import listdir, path
from typing import Callable


class Explorer:
    def __init__(self,
                 on_run: Callable[[str], None]):
        self.path = path.abspath('data')
        self.on_run = on_run

    def run(self):
        while True:
            output = input(f"{self.path} $> ").split(' ')
            command = output[0]
            args = output[1:]

            match command:
                case 'ls':
                    self.__handle_ls(' '.join(args) if len(args) else None)
                case '..':
                    self.__handle_cd('..')
                case 'cd':
                    self.__handle_cd(' '.join(args))
                case 'run':
                    self.__handle_run(f"{self.path}/{' '.join(args)}")
                case 'help':
                    self.__handle_help()
                case 'exit':
                    exit()
                case 'quit':
                    exit()

    def __handle_ls(self, segment: str | None):
        location = f"{self.path}/{segment if segment else ''}"
        content = listdir(location)
        folders: list[str] = []
        scripts: list[str] = []

        for item in content:
            item_location = f"{location}{item}"
            if path.isdir(item_location):
                folders.append(item)
            elif path.isfile(item_location) and item.endswith('.json'):
                scripts.append(item.replace('.json', ''))

        print(f"[ ] Folders: {', '.join(folders)}")
        print(f"[ ] Scripts: {', '.join(scripts)}")

    def __handle_cd(self, segment: str):
        match segment:
            case '':
                pass
            case '.':
                pass
            case '..':
                current_path = '/'.join(self.path.split('/')[:-1])
                self.path = current_path if current_path else '/'
            case _:
                current_path = f"{self.path}/{segment}"
                is_dir = path.isdir(current_path)
                if is_dir:
                    self.path = current_path

    def __handle_run(self, script_file: str):
        if len(script_file) == 0: return

        current_path = script_file if script_file.endswith('.json') else script_file + '.json'
        if not path.isfile(current_path):
            return

        self.on_run(current_path)

    def __handle_help(self):
        print("[ ] .. - go to parent directory")
        print("[ ] cd <str> - update path")
        print("[ ] ls - list current dir")
        print("[ ] run <str> - run selected script file (*.json)")
        print("[ ] exit,quit - exit app")