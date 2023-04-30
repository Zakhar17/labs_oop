from abc import ABC, abstractmethod

class VehicleVisitor(ABC):
    @abstractmethod
    def visit(self, vehicle):
        pass

class PrintVehicleInfoVisitor(VehicleVisitor):
    def visit(self, vehicle):
        print(f"{vehicle.year} {vehicle.make} {vehicle.model}, Mileage: {vehicle.mileage}")
