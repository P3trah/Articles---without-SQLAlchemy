class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        if len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._name = name
        self._category = category
        all_magazines.append(self)
        
    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category
    
     
    def articles(self):
        return [article for article in all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))
     
    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        authors_count = Counter(article.author for article in self.articles())
        return [author for author, count in authors_count.items() if count > 2] or None
    @classmethod
    def top_publisher(cls):
        if all_articles:
            magazine_counts = Counter(article.magazine for article in all_articles)
            top_magazine = max(magazine_counts, key=magazine_counts.get)
            return top_magazine
        else:
            return None