from tests.resources.base_test import BaseTestCase
from isaac_martin_sdk.resources.book import Book


class TestBook(BaseTestCase):
    def test_list(self):
        books = Book.list()
        self.assertEquals(3, len(books))
        self.assertTrue(isinstance(books[0], Book))

    def test_index(self):
        book = Book.index('5cf5805fb53e011a64671582')
        self.assertEquals('The Fellowship Of The Ring', book.name)

    def test_chapters(self):
        chapters = Book.chapters('5cf5805fb53e011a64671582')
        self.assertEquals(22, len(chapters))







