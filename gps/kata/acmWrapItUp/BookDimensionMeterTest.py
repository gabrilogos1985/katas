from gps.kata.acmWrapItUp.BookWrapper import BookWrapper
import unittest


class BookDimensionTest(unittest.TestCase):
    bookWrapper= BookWrapper()

    def test_noThickness(self):
        height = 620
        width = 500
        thickness = 0
        bookDimension = self.bookWrapper.calculateBookDimension(height, width, thickness);
        self.assertEqual(bookDimension.height, 628)
        self.assertEqual(bookDimension.width, 1008)

    def test_oneNoThickness(self):
        height = 1
        width = 1
        thickness = 0
        bookDimension = self.bookWrapper.calculateBookDimension(height, width, thickness);
        self.assertEqual(bookDimension.height, 9)
        self.assertEqual(bookDimension.width, 10)

    def test_withThickness(self):
        height = 1024
        width = 750
        thickness = 3
        bookDimension = self.bookWrapper.calculateBookDimension(height, width, thickness);
        self.assertEqual(bookDimension.height, 1032)
        self.assertEqual(bookDimension.width, 1511)

if __name__ == '__main__':
    unittest.main()
