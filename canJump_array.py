'''You are given an integer array nums. You are initially positioned at the array's first index,
 and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.'''
from typing import List

def canJump(nums: List[int]) -> bool:
    # num of first list item 
    step = nums[0]
    # jump for getting next item value
    if step == 0:
        return False
    else:
        # print(step)
        while step <= len(nums):
            # print("step is: ", step, "nums first index is:", nums[first_index], "num from list", nums[step])
            if step < len(nums):
                first_index = nums[step]
                # print(nums, "index = ", first_index)
                step += first_index
            if step == len(nums)-1:
                return True
            if step >= len(nums) or nums[step] == 0:
                return False 
            # print("step is: ", step, "nums first index is =", nums[first_index])

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))