import unittest
import nums_from_robbery_with_delete_elements as func

class TestStringMethods(unittest.TestCase):

    def test_func_return_correct_num_if_all_num_equal_1(self):
        assert func.deleteAndEarn([1,1,1,1,1]) == 5

    def test_2func_return_correct_num_if_all_numbers_differ(self):
        assert func.deleteAndEarn([7,2,4,1]) == 13
    
    def test_3func_return_correct_num_if_there_are_not_only_equal_number_and(self):
        assert func.deleteAndEarn([1,3,3,3,1]) == 11

if __name__=='__main__':
    unittest.main()