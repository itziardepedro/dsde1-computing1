'''
test_question1.py

Unit tests for question 1 of the practice assessment.
'''

import unittest
import question1 as fc

class TestFlowchart(unittest.TestCase):
    def test_zero(self):
        '''
        Test zero
        '''
        result = fc.flowchart(0)
        self.assertEqual(result, 'zero')

    def test_positive_odd(self):
        '''
        Test positive odd
        '''
        result = fc.flowchart(15)
        self.assertEqual(result, 'positive-odd')


    def test_positive_even(self):
        '''
        Test positive even
        '''
        result = fc.flowchart(60)
        self.assertEqual(result, 'positive-even')

    def test_negative_odd(self):
        '''
        Test negative odd
        '''
        result = fc.flowchart(-75)
        self.assertEqual(result, 'negative-odd')
    
    def test_negative_even(self):
        '''
        Test two valid number inputs
        '''
        result = fc.flowchart(110)
        self.assertEqual(result, 'positive-even')


if __name__ == '__main__':
    unittest.main()