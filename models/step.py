from os import system


class Step:
    def __init__(self,
                 key: str,
                 name: str,
                 params: list[str],
                 script: list[str],
                 rollback: list[str]):
        self.key = key
        self.name = name
        self.params = params
        self.params_values: dict[str, str] = {}
        self.script = script
        self.rollback = rollback

    def run(self, script_params: dict[str, str]) -> bool:
        print(f"[ ] Running... {self.name}")
        return self.__execute(self.script, script_params)

    def undo(self, script_params: dict[str, str]) -> bool:
        print(f"[!] Rolling back... {self.name}")
        return self.__execute(self.rollback, script_params)

    def __execute(self, commands: list[str], script_params: dict[str, str]) -> bool:
        for param in self.params:
            if param not in self.params_values:
                self.params_values[param] = input(f"[ ] {param} > ")

        for command in commands:
            filtered_command = command

            for param in script_params:
                filtered_command = filtered_command.replace("{{" + param + "}}", script_params[param])

            for param in self.params_values:
                filtered_command = filtered_command.replace("{{" + param + "}}", self.params_values[param])

            result = system(filtered_command)
            if result > 0:
                return False

        return True