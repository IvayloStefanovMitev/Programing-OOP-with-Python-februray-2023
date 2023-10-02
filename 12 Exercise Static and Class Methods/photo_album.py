from math import ceil


class PhotoAlbum:
    PHOTOS_FOR_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[]for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_FOR_PAGE))

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_FOR_PAGE:
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self) -> str:

        result = ['-' * 11]

        for photo in self.photos:
            result.append(('[] ' * len(photo)).rstrip())
            result.append('-' * 11)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
