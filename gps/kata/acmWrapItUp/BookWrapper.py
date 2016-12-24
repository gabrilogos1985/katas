__author__ = 'gabe'


class BookWrapper(object):
    FULL_WRAP_AROUND_MILIS=80

    def wrapItUp(self, booksDimensions):
        minLenght = self.FULL_WRAP_AROUND_MILIS
        #for book in booksDimensions:
            #minLenght +=book[1]
        return minLenght + booksDimensions[0][0]