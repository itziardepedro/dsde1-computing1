'''
test_question5.py

Unit tests for functions in question 5.
'''


import unittest
import unittest.mock
import io

import question5 as q

class TestStructures(unittest.TestCase):
    def set_up(self):
        pass


    def test_merge_list1(self):
        '''
        Test 
        '''
        result = q.merge_list([1,2,3,4,5], [6,7,8,9,10])
        self.assertEqual(result, [1,2,3,4,5,6,7,8,9,10])

    def test_merge_list2(self):
        '''
        Test 
        '''
        result = q.merge_list([1,2,3,4], [6,7,8,9,10])
        self.assertEqual(result, [])

    def test_merge_listi3(self):
        '''
        Test 
        '''
        result = q.merge_list([1,2,3,4,5], [7,8,9,10])
        self.assertEqual(result, [])

    def test_unique_values(self):
        '''
        Test
        '''
        result = q.unique_values([1,2,1,2,4,3,5,3,1,2,3])
        self.assertEqual(set(result), set([1,2,3,4,5]))


    def test_start_to_lower(self):
        '''
        Test
        '''
        result = q.start_to_lower('HeLLO World', 5)
        self.assertEqual(result, 'hello World')

    def test_first_double_char1(self):
        '''
        Test
        '''
        result = q.first_double_char('abcdefcab')
        self.assertEqual(result, 'c')

    def test_first_double_char2(self):
        '''
        Test
        '''
        result = q.first_double_char('asdfgzxcrrdsad')
        self.assertEqual(result, 'r')
    
    def test_sum_of_dict(self):
        '''
        Test
        '''
        result = q.sum_of_dict({'a': 1, 'b': 10, 'c': 100})
        self.assertEqual(result, 111)
        
    def test_multiply_dict(self):
        '''
        Test
        '''
        result = q.multiply_dict({'a': 1, 'b': 10, 'c': 100})
        self.assertEqual(result, {'a': 3, 'b': 30, 'c': 300})

    def test_max_min1(self):
        '''
        Test
        '''
        result = q.max_min([1,2,-1,4,5,20,7])
        self.assertEqual(result, 20)

    def test_max_min2(self):
        '''
        Test
        '''
        result = q.max_min([1,2,-1,4,5,20,7], "min")
        self.assertEqual(result, -1)

    def test_max_min3(self):
        '''
        Test
        '''
        result = q.max_min([1,2,-1,4,5,20,7], "extra")
        self.assertEqual(result, None)

       

    

if __name__ == '__main__':
    unittest.main()
