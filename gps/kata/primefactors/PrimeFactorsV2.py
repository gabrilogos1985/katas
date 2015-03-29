import math

__author__ = 'Sony'


class PrimerFactorsV2(object):
    @classmethod
    def generate(cls, param):
        primeList = []
        for factor in range(2, int(math.sqrt(param)) + 1):
            while param % factor == 0:
                param /= factor
                primeList.append(factor)
        if param > 1:
            primeList.append(param)

        return primeList