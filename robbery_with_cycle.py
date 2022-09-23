# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this 
# place are arranged in a circle. That means the first house is the neighbor
#  of the last one. Meanwhile, adjacent houses have a security system connected,
#  and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.
from typing import List

def rob(self, nums: List[int]) -> int:
    nums_without_0el = nums[1:]
    nums_without_last = nums[:-1]
    if len(nums)==1:
        return nums[0]
    def check_better_scheme(num_list):
        next1, next2 = 0,0
        for i in range(len(num_list)-1, -1, -1):
            tmp = max(num_list[i] + next2, next1)
            next2 = next1
            next1 = tmp
        return tmp
    
    return max(check_better_scheme(nums_without_0el), check_better_scheme(nums_without_last))