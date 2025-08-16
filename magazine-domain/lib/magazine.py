class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Invalid magazine name")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Invalid category")
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    def articles(self):
        from lib.article import Article
        return [a for a in Article.all_articles if a.magazine == self]

    def contributors(self):
        authors = []
        for art in self.articles():
            if art.author not in authors:
                authors.append(art.author)
        return authors

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        arts = self.articles()
        freq_authors = {}
        for a in arts:
            freq_authors[a.author] = freq_authors.get(a.author, 0) + 1
        result = [author for author, count in freq_authors.items() if count > 2]
        if not result:
            return None
        return result

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        top_mag = max(cls.all_magazines, key=lambda m: len(m.articles()))
        return top_mag
