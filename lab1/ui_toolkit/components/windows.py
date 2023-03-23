from .base import Button, Label, Textbox

class WindowsButton(Button):
    def __init__(self):
        print("WindowsButton created")

    def render(self):
        print("Rendering WindowsButton")

class WindowsLabel(Label):
    def __init__(self):
        print("WindowsLabel created")

    def render(self):
        print("Rendering WindowsLabel")

class WindowsTextbox(Textbox):
    def __init__(self):
        print("WindowsTextbox created")

    def render(self):
        print("Rendering WindowsTextbox")
