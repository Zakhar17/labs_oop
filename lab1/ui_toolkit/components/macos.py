from .base import Button, Label, Textbox

class MacOSButton(Button):
    def __init__(self):
        print("MacOSButton created")

    def render(self):
        print("Rendering MacOSButton")

class MacOSLabel(Label):
    def __init__(self):
        print("MacOSLabel created")

    def render(self):
        print("Rendering MacOSLabel")

class MacOSTextbox(Textbox):
    def __init__(self):
        print("MacOSTextbox created")

    def render(self):
        print("Rendering MacOSTextbox")
