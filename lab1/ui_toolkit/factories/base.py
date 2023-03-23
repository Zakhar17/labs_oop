from abc import ABC, abstractmethod
from ..components.base import Button, Label, Textbox

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_label(self) -> Label:
        pass

    @abstractmethod
    def create_textbox(self) -> Textbox:
        pass
