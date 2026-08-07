import json

from models.script import Script
from models.step import Step


def map_to_script(path: str) -> Script | None:
    with open(path, 'r') as file:
        try:
            script = json.load(file)
            steps: list[Step] = []

            for step in script['steps']:
                steps.append(Step(key=step['key'],
                                  name=step['name'],
                                  params=step['params'] if step['params'] else [],
                                  script=step['script'] if step['script'] else [],
                                  rollback=step['rollback'] if step['rollback'] else []))

            result = Script(name=script['name'] if script['name'] else '',
                            description=script['description'] if script['description'] else '',
                            params=script['params'] if script['params'] else [],
                            steps=steps)

            return result
        except:
            return None