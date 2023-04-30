import re

class CommandInterpreter:
    def __init__(self, mediator):
        self.mediator = mediator

    def interpret(self, command):
        device_name, action = self._parse_command(command)
        self.mediator.perform_action(device_name, action)

    def _parse_command(self, command):
        device_name, action = re.match(r"(\w+)\s+(\w+)", command).groups()
        return device_name, action
