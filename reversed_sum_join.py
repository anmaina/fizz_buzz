from typing import Optional, List

def addTwoNumbers(l1: Optional[List], l2: Optional[List]) -> Optional[List]:
    result = str(int(joinfunction(l1)) + int(joinfunction(l2)))
    reversed_result = list(reversed([int(i) for i in result]))
    return reversed_result


def joinfunction(l):
    new_num = ''.join(reversed(list(str(i) for i in l)))
    return new_num

print(addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))
print(addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))