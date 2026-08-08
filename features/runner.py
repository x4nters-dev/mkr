from enums.run_mode import RunMode
from utils.map_to_script import map_to_script


class Runner:
    def __init__(self,
                 file_path: str,
                 run_mode: RunMode):
        self.file_path = file_path
        self.run_mode = run_mode
        self.script = map_to_script(file_path)
        self.params: dict[str, str] = {}

    def run(self):
        if self.script:
            success = self.script.run(self.run_mode)
            print('[ ] OK' if success else '[!] FAILED')