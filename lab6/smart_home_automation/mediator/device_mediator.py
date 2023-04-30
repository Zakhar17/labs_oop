class DeviceMediator:
    def __init__(self):
        self.devices = {}

    def add_device(self, device_name, device):
        self.devices[device_name] = device

    def perform_action(self, device_name, action):
        if device_name in self.devices:
            device = self.devices[device_name]
            if hasattr(device, action):
                getattr(device, action)()
            else:
                print(f"Action '{action}' not supported by {device_name}.")
        else:
            print(f"Device '{device_name}' not found.")
