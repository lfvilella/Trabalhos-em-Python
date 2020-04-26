import unittest
from book import Book


class BookTest(unittest.TestCase):

    def setUp(self):
        self.book = Book()

    def test_search_book_by_name(self):
        self.book.add('Book1', 'Author1')
        name = self.book.search(name='Book1')
        self.assertEqual('Author1', name[0])

    def test_search_book_by_author(self):
        self.book.add('Book1', 'Author1')
        name = self.book.search(author='Author1')
        self.assertEqual('Author1', name[0])
