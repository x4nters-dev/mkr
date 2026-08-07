from models.step import Step


class Script:
    def __init__(self,
                 name: str,
                 description: str,
                 params: list[str],
                 steps: list[Step]):
        self.name = name
        self.description = description
        self.params = params
        self.params_values: dict[str, str] = {}
        self.steps = steps

    def run(self):
        for param in self.params:
            self.params_values[param] = input(f"[ ] {param} > ")

        has_steps = len(self.steps) > 0
        if not has_steps: return True

        return self.__run__step(0)

    def __run__step(self, index: int) -> bool:
        if index == len(self.steps):
            return True

        step = self.steps[index]

        try:
            if step.run(self.params_values) and self.__run__step(index + 1):
                return True
            else:
                step.undo(self.params_values)
                return False

        except:
            step.undo(self.params_values)
            return False