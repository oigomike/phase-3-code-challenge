from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from lib.author import Author
    from lib.magazine import Magazine

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Invalid title")
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    def set_author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    def set_magazine(self, new_mag):
        self._magazine = new_mag
