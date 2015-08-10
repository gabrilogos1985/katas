from gps.kata.acmWrapItUp.BookWrapper import BookWrapper

__author__ = 'gabe'

import unittest


class TestSequenceFunctions(unittest.TestCase):
    def test_oneDimension(self):
        bookWrapper= BookWrapper()
        minLenght = bookWrapper.wrapItUp([[1,1,1],[1,1,1]])
        self.assertEqual(minLenght,2)
        minLenght = bookWrapper.wrapItUp([[1,1,1],[1,1,1],[1,1,0]])
        self.assertEqual(minLenght,3)

    def heightBestThanWith(self):
        pass


if __name__ == '__main__':
    unittest.main()

