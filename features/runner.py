from utils.map_to_script import map_to_script


class Runner:
    def __init__(self,
                 file_path: str):
        self.file_path = file_path
        self.script = map_to_script(file_path)
        self.params: dict[str, str] = {}

    def run(self):
        if self.script:
            success = self.script.run()
            print('[ ] OK' if success else '[!] FAILED')