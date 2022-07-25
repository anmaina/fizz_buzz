from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums)-1
    new_nums = sorted(list(enumerate(nums)), key = lambda x: x[1])
    
    while new_nums[left][1] + new_nums[right][1]!=target:
        if new_nums[left][1] + new_nums[right][1] > target:
            right -=1
        else:
            left +=1
    return [new_nums[left][0], new_nums[right][0]]

print(twoSum([-1,-2,-3,-4,-5], -8))