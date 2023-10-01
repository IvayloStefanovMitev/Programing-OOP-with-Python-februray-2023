from typing import List

from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str) -> str:
        try:
            curr_album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if curr_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(curr_album)

        return f"Album {album_name} has been removed."

    def details(self) -> str:

        result = [f"Band {self.name}"]

        [result.append(a.details()) for a in self.albums]

        return "\n".join(result)
#
