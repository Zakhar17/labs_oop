from abc import ABC, abstractmethod

class UIComponent(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Button(UIComponent):
    pass

class Label(UIComponent):
    pass

class Textbox(UIComponent):
    pass
