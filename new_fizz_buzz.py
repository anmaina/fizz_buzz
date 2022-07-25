from typing import List, Tuple, Any

MAPPING = [
    (3, 'fizz'),
    (5, 'buzz'),
    (7, 'bar')
]


def fizz_buzz(number:int, mapping:List[Tuple[int, str]])->str:
    result = ""
    for digit_element, output_word in mapping:
        if number % digit_element == 0:
            result += output_word
    if result != "":
        return result
    else:
        return str(number)

def list_creation(start:int, stop:int, mapping_function:function)->Any:
    for number in range(start, stop+1): 
        to_append = mapping_function(number)
        yield to_append

def print_list():
    mapping_function = lambda x: "<li>" + fizz_buzz(x, MAPPING) + "</li>"
    print("<ul>")
    for n in list_creation(1, 100, mapping_function):
        print(n)
    print("</ul>")


if __name__ == '__main__':
    print_list()