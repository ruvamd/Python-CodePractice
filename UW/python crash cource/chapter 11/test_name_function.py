import unittest
from name_function import full_name

class names_test_cases(unittest.TestCase): #test for name_function.py
    def full_name_test(self):
        formatted_full_name=full_name('vadim','rusu')
        self.assertEqual(formatted_full_name,'vadim rusu')
if __name__=='__main__':
    unittest.main()


