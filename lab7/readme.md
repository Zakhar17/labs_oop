# Vehicle Inspection System

The Vehicle Inspection System allows users to save and restore the state of inspections using the Memento pattern and perform different operations on vehicles using the Visitor pattern.

## Requirements

1. Implement a Vehicle class with properties such as make, model, year, and mileage.
2. Implement a VehicleInspection class that can save and restore its state using the Memento pattern.
3. Implement the Memento class that holds the state of a VehicleInspection object.
4. Implement a Visitor class hierarchy for different operations on vehicles.
5. Create a clear and organized project directory structure with separate folders for the Memento, Visitor, and Vehicle classes.


## Usage

1. Instantiate a Vehicle with make, model, year, and mileage.
2. Instantiate a VehicleInspection object.
3. Add vehicles to the VehicleInspection object using the add_vehicle method.
4. Save the state of the VehicleInspection object using the save_state method.
5. Perform operations on vehicles using the Visitor pattern by implementing VehicleVisitor classes and calling the accept method on Vehicle objects with a visitor instance.
6. Restore the state of the VehicleInspection object using the restore_state method and a Memento object.

Refer to the `main.py` file for a usage example.
