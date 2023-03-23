from ui_toolkit import WindowsUIFactory, MacOSUIFactory, LinuxUIFactory

class UIAbstractFactory:
    def __init__(self, platform: str):
        if platform == "Windows":
            self.factory = WindowsUIFactory()
        elif platform == "macOS":
            self.factory = MacOSUIFactory()
        elif platform == "Linux":
            self.factory = LinuxUIFactory()
        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def create_button(self):
        return self.factory.create_button()

    def create_label(self):
        return self.factory.create_label()

    def create_textbox(self):
        return self.factory.create_textbox()

# Example usage
def main(platform):
    abstract_factory = UIAbstractFactory(platform)

    button = abstract_factory.create_button()
    label = abstract_factory.create_label()
    textbox = abstract_factory.create_textbox()

    button.render()
    label.render()
    textbox.render()

if __name__ == "__main__":
    main("macOS")
