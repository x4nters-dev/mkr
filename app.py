from enums.run_mode import RunMode
from features.explorer import Explorer
from features.runner import Runner
from os import path


class App:
    def __init__(self, args: list[str]):
        self.script_path = args[0] if len(args) > 0 else None

    def run(self):
        try:
            if self.script_path:
                self.__on_run(self.script_path)
            else:
                Explorer(self.__on_run).run()
        except KeyboardInterrupt:
            pass

    def __on_run(self, file_path: str, run_mode: RunMode):
        if not path.isfile(file_path):
            print(f"[!] Script not found: {file_path}")
            return

        Runner(file_path, run_mode).run()
