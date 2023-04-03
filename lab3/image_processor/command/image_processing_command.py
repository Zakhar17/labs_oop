from abc import ABC, abstractmethod

class ImageProcessingCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class ApplyProcessingCommand(ImageProcessingCommand):
    def __init__(self, image_processor, processing_strategy):
        self.image_processor = image_processor
        self.processing_strategy = processing_strategy
        self.previous_image = None

    def execute(self):
        self.previous_image = self.image_processor.image
        self.image_processor.apply_processing(self.processing_strategy)

    def undo(self):
        self.image_processor.image = self.previous_image
        self.image_processor._notify_observers()
