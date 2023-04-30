from smart_home_automation.interpreter.command_interpreter import CommandInterpreter
from smart_home_automation.mediator.device_mediator import DeviceMediator
from smart_home_automation.devices.light import Light
from smart_home_automation.devices.air_conditioner import AirConditioner
from smart_home_automation.devices.security_system import SecuritySystem

def main():
    mediator = DeviceMediator()

    light = Light()
    air_conditioner = AirConditioner()
    security_system = SecuritySystem()

    mediator.add_device("light", light)
    mediator.add_device("air_conditioner", air_conditioner)
    mediator.add_device("security_system", security_system)

    interpreter = CommandInterpreter(mediator)

    commands = ["light on", "air_conditioner on", "security_system arm", "light off", "air_conditioner off", "security_system disarm"]

    for command in commands:
        interpreter.interpret(command)

if __name__ == "__main__":
    main()
