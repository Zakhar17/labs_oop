from playlist_management_system import Playlist, PlayingState, PausedState, StoppedState
from playlist_management_system import PlayCommandHandler, PauseCommandHandler, StopCommandHandler


def main():
    songs = ["Song1", "Song2", "Song3"]
    playlist = Playlist(songs)

    print("Songs in the playlist:")
    for song in playlist:
        print(song)

    state = StoppedState()
    command_handler = PlayCommandHandler(PauseCommandHandler(StopCommandHandler()))

    commands = ["play", "pause", "play", "stop", "pause", "play", "stop"]

    for command in commands:
        state = command_handler.handle_command(command, state)


if __name__ == "__main__":
    main()
