from gps.kata.acmWrapItUp.BookDimension import BookDimension

__author__ = 'gabe'


class BookWrapper(object):

    def wrapItUp(self, booksDimensions):
        minLenght = self.FULL_WRAP_AROUND_MILIS
        #for book in booksDimensions:
            #minLenght +=book[1]
        return minLenght + booksDimensions[0][0]

    def calculateBookDimension(self, height, width, thickness):
        dimension = BookDimension()
        dimension.height = height+8;
        dimension.width = width*2+8+thickness
        return dimension

    def getMinLengthToCut(self, books):
        minLength = 0
        for book in books:
            minLength = book.height
            if book.width<book.height:
                minLength = book.width
            for otherBook in books:
                if book != otherBook:
                    if book.width == otherBook.width or book.width == otherBook.height:
                        minLength = book.width
                        leftAnotherBookSide = otherBook.width
                        if minLength != otherBook.height:
                            leftAnotherBookSide =  otherBook.height
                        othersideLenght = book.height + leftAnotherBookSide
                        if othersideLenght < minLength:
                            minLength = othersideLenght
                        elif minLength * 2 >1720:
                            if leftAnotherBookSide < book.height:
                                minLength = leftAnotherBookSide
                    elif book.height == otherBook.height or book.height == otherBook.width:
                        minLength = book.height
                        leftAnotherBookSide = otherBook.width
                        if minLength!=otherBook.height:
                            leftAnotherBookSide = otherBook.height
                        othersideLenght = book.width + leftAnotherBookSide
                        if othersideLenght < minLength:
                            minLength = othersideLenght
                        elif leftAnotherBookSide < book.height:
                                minLength = leftAnotherBookSide

        return minLength