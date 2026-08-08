from enums.run_mode import RunMode
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

    def run(self, run_mode: RunMode):
        for param in self.params:
            self.params_values[param] = input(f"[ ] {param} > ")

        has_steps = len(self.steps) > 0
        if not has_steps: return True

        return self.__run__step(0, run_mode)

    def __run__step(self, index: int, run_mode: RunMode) -> bool:
        if index == len(self.steps):
            return True

        step = self.steps[index]

        match run_mode:
            case RunMode.AUTO:
                try:
                    if step.run(self.params_values) and self.__run__step(index + 1, run_mode):
                        return True
                    else:
                        step.undo(self.params_values)
                        return False
                except:
                    step.undo(self.params_values)
                    return False

            case RunMode.SCRIPTS_ONLY:
                try:
                    step.run(self.params_values)
                    self.__run__step(index + 1, run_mode)
                except:
                    pass
                finally:
                    return True

            case RunMode.ROLLBACKS_ONLY:
                try:
                    self.__run__step(index + 1, run_mode)
                    step.undo(self.params_values)
                except:
                    pass
                finally:
                    return True
