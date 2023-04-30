# Smart Home Automation System

The Smart Home Automation System interprets simple commands using the Interpreter pattern and manages the communication between different devices using the Mediator pattern.

## Requirements

1. Implement an Interpreter class that can parse and execute simple commands for controlling smart home devices.
2. Implement a Mediator class that manages the communication between different smart home devices.
3. Implement classes for different smart home devices, such as lights, air conditioners, and security systems.
4. Create a clear and organized project directory structure with separate folders for the Interpreter, Mediator, and Device classes.

## Usage

1. Instantiate a DeviceMediator.
2. Create instances of different devices (Light, AirConditioner, and SecuritySystem) and add them to the mediator using the add_device method.
3. Instantiate a CommandInterpreter with the mediator.
4. Interpret commands for devices using the interpret method of the CommandInterpreter.
