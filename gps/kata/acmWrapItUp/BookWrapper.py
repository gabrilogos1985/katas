__author__ = 'gabe'


class BookWrapper(object):
    def wrapItUp(self, booksDimensions):
        minLenght = 0
        for book in booksDimensions:
            minLenght +=book[0]
        return minLenght