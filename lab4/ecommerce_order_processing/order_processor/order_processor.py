from abc import ABC, abstractmethod

class OrderProcessor(ABC):
    def process_order(self, order):
        self.validate_order(order)
        self.calculate_total(order)
        self.create_invoice(order)
        self.send_invoice(order)

    @abstractmethod
    def validate_order(self, order):
        pass

    @abstractmethod
    def calculate_total(self, order):
        pass

    @abstractmethod
    def create_invoice(self, order):
        pass

    @abstractmethod
    def send_invoice(self, order):
        pass

class SimpleOrderProcessor(OrderProcessor):
    def validate_order(self, order):
        print(f"Validating order {order}")

    def calculate_total(self, order):
        print(f"Calculating total for order {order}")

    def create_invoice(self, order):
        print(f"Creating invoice for order {order}")

    def send_invoice(self, order):
        print(f"Sending invoice for order {order}")
