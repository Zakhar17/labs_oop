from abc import ABC, abstractmethod

class CommandHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_command(self, command, playlist_state):
        pass

class PlayCommandHandler(CommandHandler):
    def handle_command(self, command, playlist_state):
        if command == "play":
            new_state = playlist_state.play()
            return new_state if new_state else playlist_state
        if self.next_handler:
            return self.next_handler.handle_command(command, playlist_state)
        raise ValueError(f"Command '{command}' not recognized.")

class PauseCommandHandler(CommandHandler):
    def handle_command(self, command, playlist_state):
        if command == "pause":
            new_state = playlist_state.pause()
            return new_state if new_state else playlist_state
        if self.next_handler:
            return self.next_handler.handle_command(command, playlist_state)
        raise ValueError(f"Command '{command}' not recognized.")

class StopCommandHandler(CommandHandler):
    def handle_command(self, command, playlist_state):
        if command == "stop":
            new_state = playlist_state.stop()
            return new_state if new_state else playlist_state
        if self.next_handler:
            return self.next_handler.handle_command(command, playlist_state)
        raise ValueError(f"Command '{command}' not recognized.")
