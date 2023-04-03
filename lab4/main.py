from ecommerce_order_processing import SimpleOrderProcessor, MacroCommand

class ProcessOrderCommand:
    def __init__(self, processor, order):
        self.processor = processor
        self.order = order

    def execute(self):
        self.processor.process_order(self.order)

def main():
    order_processor = SimpleOrderProcessor()
    order1 = "Order1"
    order2 = "Order2"

    process_order1_command = ProcessOrderCommand(order_processor, order1)
    process_order2_command = ProcessOrderCommand(order_processor, order2)

    macro_command = MacroCommand([process_order1_command, process_order2_command])
    macro_command.execute()

if __name__ == "__main__":
    main()
