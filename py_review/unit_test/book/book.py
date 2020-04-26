class Book():
    def __init__(self):
        self.books = {}

    def add(self, name, author, price=None):
        self.books[name] = [author, price]

    def search(self, name=None, author=None):
        if name:
            return self.books[name]

        for name, items in self.books.items():
            if author == items[0]:
                return self.books[name]
