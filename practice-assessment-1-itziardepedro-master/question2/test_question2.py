'''
test_question2.py

Unit tests for question 2 to help demonstrate algorithm.
'''

import unittest
import question2 as fc

class TestFlowchart(unittest.TestCase):
    def test_threes(self):
        '''
        Test divisible by 3
        '''
        result = fc.flowchart([6, 9, 3, 12])
        self.assertEqual(result, [3, 3, 3, 3])

    def test_twos(self):
        '''
        Test divisible by 2
        '''
        result = fc.flowchart([4, 8, 10, 2])
        self.assertEqual(result, [2, 2, 2, 2])


    def test_neither(self):
        '''
        Test not divisible by 3 or 2
        '''
        result = fc.flowchart([5, 7, 1])
        self.assertEqual(result, [0, 0, 0])

    def test_medium_odd(self):
        '''
        Test a mix
        '''
        result = fc.flowchart([5, 9, 4, 1, 14])
        self.assertEqual(result, [0, 3, 2, 0, 2])
    

if __name__ == '__main__':
    unittest.main()