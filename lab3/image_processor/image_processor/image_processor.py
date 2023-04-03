class ImageProcessor:
    def __init__(self, image):
        self.image = image
        self.observers = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def _notify_observers(self):
        for observer in self.observers:
            observer.update(self.image)

    def apply_processing(self, processing_strategy):
        self.image = processing_strategy.process(self.image)
        self._notify_observers()
