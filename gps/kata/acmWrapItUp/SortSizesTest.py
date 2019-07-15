__author__ = 'gabe'

import unittest


class SortSizesTest(unittest.TestCase):
    def est_sortAndMessureOne(self):
        minLenght = self.sortMeasure([[1080,700]]);
        self.assertEqual(minLenght, 700)

    def test_IterateCombinations(self):
        iteraFlags = list()
        books = [[1080, 700]]
        for b in books:
            iteraFlags.append(0)
        print(iteraFlags)
        minLenght = self.iterateBooks(books, iteraFlags, -1)
        self.assertEqual(minLenght, 700)

    def test_IterateCombinationsACMExample(self):
        iteraFlags = list()
        books = [[1080, 700], [1080, 680]]
        for b in books:
            iteraFlags.append(0)
        print(iteraFlags)
        minLenght = self.iterateBooks(books, iteraFlags, -1)
        self.assertEqual(minLenght, 1080)

    def test_IterateCombinations_3(self):
        iteraFlags = list()
        books = [[800, 900], [600, 300], [450, 680]]
        for b in books:
            iteraFlags.append(0)
        print(iteraFlags)
        minLenght = self.iterateBooks(books, iteraFlags, -1)
        self.assertEqual(minLenght, 800)
    #
    # @unittest.skip("solve later medium level case ")
    # def test_height2Width1Nothickness(self):
    #     minLenght = self.bookWrapper.wrapItUp([[2,1,0]])
    #     self.assertEqual(minLenght,82)
    #
    # @unittest.skip("solve later medium level case ")
    # def test_twoDimensionSizeOne(self):
    #     minLenght = self.bookWrapper.wrapItUp([1,1,1]*22)
    #     self.assertEqual(minLenght,83)
    #
    # def heightBestThanWith(self):
    #     pass

    def sortMeasure(self, books):
        size = len(books)
        for counter in iter(range(0,size)):
            width = books[counter][0];
            heigth = books[counter][1];
            if(size > counter + 1):
                width = width + books[counter+1][0];
                heigth = heigth + books[counter][1];
            else:
                width = books[counter][1];
                heigth = books[counter][0];
        if width > heigth:
            return heigth
        else:
            return width;

    def iterateBooks(self, books, flags, minHeight):
        traversed = True
        width = 0
        height = 0
        size = len(flags)
        acc = 1
        for counter in iter(range(size-1, -2, -1)):
            if(counter == -1):
                if(width <= 1800 and (height < minHeight or minHeight == -1)): minHeight = height
                if(acc == 1): return minHeight
                else:
                    return self.iterateBooks(books, flags, minHeight)
            flag = flags[counter]
            width+=books[counter][flag]
            if(width > 1800): continue
            currentHeight = books[counter][abs(flag - 1)]
            if(currentHeight > height): height = currentHeight
            if(flag == 1):
                if(acc == 1):
                    flags[counter] = 0
                    acc = 1
            else:
                if(acc == 1):
                    flags[counter] = 1
                    acc = 0
        return minHeight



print(__name__)
if __name__ == '__main__':
    unittest.main()

