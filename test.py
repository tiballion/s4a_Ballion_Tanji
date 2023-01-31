import unittest
from main import *



class TestFermTransAttr(unittest.TestCase):
    def test_ferm_trans_attr(self):
        # Test 1: Basic functionality
        F = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'D'})]
        A = {'A'}
        expected_output = {'A', 'B', 'C', 'D'}
        self.assertEqual(FermTransAttr(F, A), expected_output)

        # Test 2: Empty set
        F = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'D'})]
        A = set()
        expected_output = set()
        self.assertEqual(FermTransAttr(F, A), expected_output)

        # Test 3: No dependencies in F
        F = []
        A = {'A'}
        expected_output = {'A'}
        self.assertEqual(FermTransAttr(F, A), expected_output)

        # Test 4: A is already a closure
        F = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'D'})]
        A = {'A', 'B', 'C', 'D'}
        expected_output = {'A', 'B', 'C', 'D'}
        self.assertEqual(FermTransAttr(F, A), expected_output)


class TestCouvMinDF(unittest.TestCase):
       def test_CouvMinDF(self):
            #TODO: Write tests for CouvMinDF
            pass



if __name__ == '__main__':
    unittest.main()