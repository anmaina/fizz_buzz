string = 'anna'
def is_palindrome(string: str) -> bool:
    # write code here
    if string==string[::-1]:
        print('True')
        return True
    else:
        print('F')
        False
    pass