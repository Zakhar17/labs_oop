from .base import UIFactory
from ..components.macos import MacOSButton, MacOSLabel, MacOSTextbox

class MacOSUIFactory(UIFactory):
    def create_button(self) -> MacOSButton:
        return MacOSButton()

    def create_label(self) -> MacOSLabel:
        return MacOSLabel()

    def create_textbox(self) -> MacOSTextbox:
        return MacOSTextbox()
