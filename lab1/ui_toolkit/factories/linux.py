from .base import UIFactory
from ..components.linux import LinuxButton, LinuxLabel, LinuxTextbox

class LinuxUIFactory(UIFactory):
    def create_button(self) -> LinuxButton:
        return LinuxButton()

    def create_label(self) -> LinuxLabel:
        return LinuxLabel()

    def create_textbox(self) -> LinuxTextbox:
        return LinuxTextbox()
