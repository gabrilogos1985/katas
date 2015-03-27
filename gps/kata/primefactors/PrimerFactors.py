__author__ = 'Sony'


class PrimerFactors(object):
    @classmethod
    def generate(cls, param):
        primes = []
        remainder = param
        for primeNumber in [2, 3, 5]:
            while remainder % primeNumber == 0:
                remainder /= primeNumber
                primes.append(primeNumber)

        return primes