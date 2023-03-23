from .base import UIFactory
from ..components.windows import WindowsButton, WindowsLabel, WindowsTextbox

class WindowsUIFactory(UIFactory):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def create_label(self) -> WindowsLabel:
        return WindowsLabel()

    def create_textbox(self) -> WindowsTextbox:
        return WindowsTextbox()
