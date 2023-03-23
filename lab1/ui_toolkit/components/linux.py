from .base import Button, Label, Textbox

class LinuxButton(Button):
    def __init__(self):
        print("LinuxButton created")

    def render(self):
        print("Rendering LinuxButton")

class LinuxLabel(Label):
    def __init__(self):
        print("LinuxLabel created")

    def render(self):
        print("Rendering LinuxLabel")

class LinuxTextbox(Textbox):
    def __init__(self):
        print("LinuxTextbox created")

    def render(self):
        print("Rendering LinuxTextbox")
