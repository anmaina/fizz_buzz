from typing import List

def plusOne(digits: List[int]) -> List[int]:
        new_digits = int("".join([str(i) for i in digits])) + 1
        return [int(j) for j in str(new_digits)]


print(plusOne([1,2,3]))
print(plusOne([9]))
print(plusOne([9,9,9,9]))