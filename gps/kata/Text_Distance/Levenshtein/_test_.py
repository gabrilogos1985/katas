__author__ = 'Gabo'

import unittest

## TASK
## 1. Refactor
## 2. More cases
## 3. Check if it is complete
## 4. Compare algorithm
def compareLevenshtein(word1, word2):
    w2Lenght = len(word2)
    w1Lenght = len(word1)
    if(w1Lenght == 0 or w2Lenght == 0):
        return abs(w1Lenght - w2Lenght)
    return (1 if word1[0] != word2[0] else 0) + \
           compareLevenshtein(word1[1:], word2[1:])


def levenshtein(word1, word2):
    return 0 if word1 == word2 \
        else compareLevenshtein(word1, word2)
    # word1Lenght = len(word1)
    # w2Lenght = len(word2)
    # if word1Lenght == 0 or w2Lenght == 0:
    #     return abs(word1Lenght - w2Lenght)




class TestLevenshteinDistance(unittest.TestCase):

    def test_emptyWords(self):
        word1 = ''
        word2 = ''
        self.assertEqual(levenshtein(word1, word2), 0)

    def test_equalsChar(self):
        word1 = 'a'
        word2 = 'a'
        self.assertEqual(levenshtein(word1, word2), 0)

    def test_emptyAndChar(self):
        word1 = ''
        word2 = 'a'
        self.assertEqual(levenshtein(word1, word2), 1)

    def test_CharEmpty(self):
        word1 = 'a'
        word2 = ''
        self.assertEqual(levenshtein(word1, word2), 1)

    def test_notEqualsChar(self):
        word1 = 'a'
        word2 = 'b'
        self.assertEqual(levenshtein(word1, word2), 1)

    def test_2CharWordContainsOneCharWord(self):
        word1 = 'ab'
        word2 = 'a'
        self.assertEqual(levenshtein(word1, word2), 1)

    def test_2CharWordOneCharWordLastCharEqual(self):
        word1 = 'ab'
        word2 = 'b'
        self.assertEqual(levenshtein(word1, word2), 1)

    def test_2CharWordvsEmpty(self):
        word1 = 'ab'
        word2 = ''
        self.assertEqual(levenshtein(word1, word2), 2)

    def test_2CharWordsAllEquals(self):
        word1 = 'ab'
        word2 = 'ba'
        self.assertEqual(levenshtein(word1, word2), 2)

    def test_flawn(self):
        self.assertEqual(levenshtein('lawn', 'flaw'), 2)

if __name__ == '__main__':
    unittest.main()