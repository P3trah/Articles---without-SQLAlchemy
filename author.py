all_authors = []
all_magazines = []
all_articles = []

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        all_authors.append(self)

    @property
    def name(self):
        return self._name

def articles(self):
        return [article for article in all_articles if article.author == self]

def magazines(self):
        return list(set(article.magazine for article in self.articles()))
def add_article(self, magazine, title):
        new_article = Article(author=self, magazine=magazine, title=title)
        all_articles.append(new_article)
        return new_article

def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles())) or None