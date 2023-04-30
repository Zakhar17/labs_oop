from vehicle_inspection_system.vehicle.vehicle import Vehicle
from vehicle_inspection_system.memento.vehicle_inspection import VehicleInspection
from vehicle_inspection_system.visitor.vehicle_visitor import PrintVehicleInfoVisitor

def main():
    vehicle1 = Vehicle("Audi", "S8", 2015, 50000)
    vehicle2 = Vehicle("Audi", "RS6", 2017, 30000)

    inspection = VehicleInspection()
    inspection.add_vehicle(vehicle1)
    inspection.add_vehicle(vehicle2)

    saved_state = inspection.save_state()

    inspection.remove_vehicle(vehicle2)

    print("Before restoring state:")
    for vehicle in inspection._inspected_vehicles:
        vehicle.accept(PrintVehicleInfoVisitor())

    inspection.restore_state(saved_state)

    print("After restoring state:")
    for vehicle in inspection._inspected_vehicles:
        vehicle.accept(PrintVehicleInfoVisitor())

if __name__ == "__main__":
    main()
