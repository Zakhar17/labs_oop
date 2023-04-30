from .memento import Memento

class VehicleInspection:
    def __init__(self):
        self._inspected_vehicles = []

    def add_vehicle(self, vehicle):
        self._inspected_vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self._inspected_vehicles.remove(vehicle)

    def save_state(self):
        return Memento(self._inspected_vehicles.copy())

    def restore_state(self, memento):
        self._inspected_vehicles = memento.get_saved_state()
