from tests.resources.base_test import BaseTestCase
from resources.book import Book, Chapter


class TestBook(BaseTestCase):
    def test_list(self):
        books = Book.list()
        self.assertEquals(3, len(books))

    def test_index(self):
        book = Book.index('5cf5805fb53e011a64671582')
        self.assertEquals('The Fellowship Of The Ring', book.name)

    def test_chapters(self):
        chapters = Book.chapters('5cf5805fb53e011a64671582')
        self.assertEquals(22, len(chapters))

    def test_chapters_cannot_call_list_index(self):
        self.assertRaises(Exception, Chapter.list)
        self.assertRaises(Exception, Chapter.index)






