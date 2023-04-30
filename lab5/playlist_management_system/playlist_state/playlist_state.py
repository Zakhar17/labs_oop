from abc import ABC, abstractmethod

class PlaylistState(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class PlayingState(PlaylistState):
    def play(self):
        print("Playlist is already playing.")

    def pause(self):
        print("Pausing playlist.")
        return PausedState()

    def stop(self):
        print("Stopping playlist.")
        return StoppedState()

class PausedState(PlaylistState):
    def play(self):
        print("Resuming playlist.")
        return PlayingState()

    def pause(self):
        print("Playlist is already paused.")

    def stop(self):
        print("Stopping playlist.")
        return StoppedState()

class StoppedState(PlaylistState):
    def play(self):
        print("Starting playlist.")
        return PlayingState()

    def pause(self):
        print("Cannot pause a stopped playlist.")

    def stop(self):
        print("Playlist is already stopped.")
