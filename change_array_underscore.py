from typing import List


def removeElement(nums: List[int], val: int) -> int:
    val_count_in_nums = nums.count(val)
    i = 0
    nums = [nums.pop(i) for i in nums if i == val]
    return nums

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))