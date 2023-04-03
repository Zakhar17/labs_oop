from abc import ABC, abstractmethod

class ImageObserver(ABC):
    @abstractmethod
    def update(self, image):
        pass

class PrintImageObserver(ImageObserver):
    def update(self, image):
        print(f"Image updated: {image}")
