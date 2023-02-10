import unittest
from main import *

class Test(unittest.TestCase):

    def test_CouvMinDF(self):
        F = [['a', 'b'],['b', 'c'], ['d', 'e']]
        self.assertEqual(CouvMinDF(F), [['a', ['b']], ['b', ['c']], ['d', ['e']]])

        F2 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c']]
        self.assertEqual(CouvMinDF(F2), [['a', ['b']], ['b', ['c']], ['d', ['e']]])

        F3 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c'], ['a', 'd']]
        self.assertEqual(CouvMinDF(F3), [['a', ['b']], ['b', ['c']], ['d', ['e']], ['a', ['d']]])


    def test_DecompoDFen3FN(self):
        F = [['a', 'b'],['b', 'c'], ['d', 'e']]
        self.assertEqual(DecompoDFen3FN(F, ['a', 'b', 'c', 'd', 'e']), [['a', ['b']], ['b', ['c']], ['d', ['e']]])

        F2 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c']]
        self.assertEqual(DecompoDFen3FN(F2, ['a', 'b', 'c', 'd', 'e']), [['a', ['b']], ['b', ['c']], ['d', ['e']]])

        F3 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c'], ['a', 'd'], ['b', 'd']]
        self.assertEqual(DecompoDFen3FN(F3, ['a', 'b', 'c', 'd', 'e']), [['a', ['b']], ['d', ['e']], ['b', ['c', 'd']]])

        F4 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c'], ['a', 'd'], ['b', 'd'], ['a', 'e']]
        self.assertEqual(DecompoDFen3FN(F4, ['a', 'b', 'c', 'd', 'e']), [['a', ['b']], ['d', ['e']], ['b', ['c', 'd']]])

    def test_FermTransAttr(self):
        F = [['a', 'b'],['b', 'c'], ['d', 'e']]
        self.assertEqual(FermTransAttr(F, ['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

        F2 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c']]
        self.assertEqual(FermTransAttr(F2, ['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

        F3 = [['a', 'b'],['b', 'c'], ['d', 'e'], ['a', 'c'], ['a', 'd'], ['b', 'd']]
        self.assertEqual(FermTransAttr(F3, []), [])

if __name__ == '__main__':
    unittest.main()
