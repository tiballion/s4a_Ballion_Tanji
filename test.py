import unittest
from main import *



class TestFermTransAttr(unittest.TestCase):
    def test_ferm_trans_attr(self):
        # Test 1: Basic functionality
        F = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'D'})]
        A = {'A'}
        expected_output = {'A', 'B', 'C', 'D'}
        self.assertEqual(ferm_trans_attr(F, A), expected_output)

        # Test 2: Empty set
        F = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'D'})]
        A = set()
        expected_output = set()
        self.assertEqual(ferm_trans_attr(F, A), expected_output)

        # Test 3: No dependencies in F
        F = []
        A = {'A'}
        expected_output = {'A'}
        self.assertEqual(ferm_trans_attr(F, A), expected_output)

        # Test 4: A is already a closure
        F = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'D'})]
        A = {'A', 'B', 'C', 'D'}
        expected_output = {'A', 'B', 'C', 'D'}
        self.assertEqual(ferm_trans_attr(F, A), expected_output)


class TestCouvMinDF(unittest.TestCase):
       def test_CouvMinDF(self):
        # Todo
        pass
        

class TestDecompoDFen3Fn(unittest.TestCase):
       def test_DecompoDFen3Fn(self):
         # Test Case 1
            F = [({'a', 'b'}, {'d'}), ({'b', 'c'}, {'d'}), ({'c', 'd'}, {'a'})]
            A = {'a', 'b', 'c', 'd'}
            assert decompo_dfe_3fn(F, A) == [({'d', 'c'}, ['a']), ({'b', 'c'}, ['d']), ({'a', 'b'}, ['d'])]
            



if __name__ == '__main__':
    unittest.main()