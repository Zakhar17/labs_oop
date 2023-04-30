class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __iter__(self):
        return PlaylistIterator(self)


class PlaylistIterator:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def __next__(self):
        if self.index < len(self.playlist.songs):
            result = self.playlist.songs[self.index]
            self.index += 1
            return result
        raise StopIteration
