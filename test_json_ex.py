import unittest
# import function from tested file
from json_ex import check_char_count

class TestJsonEx(unittest.TestCase):
   
    def test_check_char_count(self):
	# assertEqual tests that output of function is equal to seccond input 
        self.assertEqual(check_char_count('AA'), 'AA count passes')
        self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
 
       # assertRaise tests that error appears (TypeError, ValueError)
	self.assertRaises(TypeError, check_char_count, 1)
        self.assertRaises(TypeError, check_char_count, True)
        self.assertRaises(TypeError, check_char_count, ['AA', 'BB'])

if __name__ == '__main__':
    unittest.main()
