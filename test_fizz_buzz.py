import unittest
import new_fizz_buzz as func

class TestStringMethods(unittest.TestCase):

    def test_1check_if_function_returns_fizz_with_number_9(self):
        assert func.fizz_buzz(9) == 'fizz'

    def test_2check_if_function_returns_buzz_with_number_10(self):
        assert func.fizz_buzz(10) == 'buzz'

    def test_3check_if_function_returns_fizzbuzz_with_number_15(self):
        assert func.fizz_buzz(15) == 'fizzbuzz'
    
    def test_4check_if_function_returns_self_with_number_13(self):
        assert func.fizz_buzz(13) == 13
        

    def test_check_if_list_generator_first_value_is_1(self):
        list_to_count = list(func.list_creation(1,100))
        len_of_list = len(list_to_count) 
        assert len_of_list == 100
        assert list_to_count[0] == 1
        assert list_to_count[-1] == 'buzz'

if __name__ == '__main__':
    unittest.main()