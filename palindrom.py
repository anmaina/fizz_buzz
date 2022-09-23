def isPalindrome(x: int) -> bool:
    if list(str(x)) == list(reversed(str(x))):
        return True

print(
isPalindrome(121),
isPalindrome(123),
isPalindrome(1),
isPalindrome(-121))