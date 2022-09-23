from tokenize import String
import unittest

import binary_search as func

class TestStringMethods(unittest.Testcase):
    def check_if_function_searches_the_right_start_index(self):
        assert func.binary_search([1,3,7,9,2,5,3], 7) == 2
    