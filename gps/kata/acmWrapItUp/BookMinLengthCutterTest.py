from gps.kata.acmWrapItUp.BookWrapper import BookWrapper
from gps.kata.acmWrapItUp.BookDimension import BookDimension
import unittest


class BookMinLengthCutterTest(unittest.TestCase):
    bookWrapper= BookWrapper()

    def test_noBooks(self):
        books = []
        bookDimension = self.bookWrapper.getMinLengthToCut(books)

    def test_oneBook(self):
        book1 = BookDimension()
        book1.height = 408
        book1.width=608
        books = [book1]
        bookDimension = self.bookWrapper.getMinLengthToCut(books)
        self.assertEqual(408, bookDimension)

    def test_twoBook(self):
        book1 = BookDimension()
        book1.height = 700
        book1.width = 1080
        book2 = BookDimension()
        book2.height = 690
        book2.width = 1080
        books = [book1, book2]
        bookDimension = self.bookWrapper.getMinLengthToCut(books)
        self.assertEqual(1080, bookDimension)

if __name__ == '__main__':
    unittest.main()
