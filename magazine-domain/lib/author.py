class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid author name")
        self._name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        from lib.article import Article
        return [a for a in Article.all_articles if a.author == self]

    def magazines(self):
        mags = []
        for art in self.articles():
            if art.magazine not in mags:
                mags.append(art.magazine)
        return mags

    def add_article(self, magazine, title):
        from lib.article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        categories = []
        for m in mags:
            if m.category not in categories:
                categories.append(m.category)
        return categories
