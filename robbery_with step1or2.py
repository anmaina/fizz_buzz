from typing import List
def rob(nums: List[int]) -> int:
    next1, next2 = 0,0
    added_num = []
    for i in range(len(nums)-1, -1, -1):
        tmp = max(nums[i][1] + next2, next1)
        if max(nums[i][1] + next2, next1) == nums[i][1] + next2:
            added_num.append(nums[i][0])
        next2 = next1
        next1 = tmp
        print(added_num)
    return tmp

print(rob([2,4,1,4,2,5])) # 13
# def rob(nums:List[int])->int:
#     if not nums:
#                 yield 0

#     elif len(nums) == 1:
#         yield nums[0]

#     else:
#         for value_from_other_houses in self._rob(nums[2:]):
#             combination_total = nums[0] + value_from_other_houses
#             # print("first option: %i" %(combination_total))
#             yield combination_total

#         for value_from_other_houses in self._rob(nums[3:]):
#             combination_total = nums[1] + value_from_other_houses
#             # print("second option: %i" %(combination_total))
#             yield combination_total

# def rob(self, nums: List) -> int:
#     return max(self._rob(nums))
#print(max(rob([1,2,3,4,5,6,7])))
# print(max(rob([1,1,1]))) #2
# print(max(rob([0]))) #0
#print(max(rob([1,3,1]))) #3

# print(max(rob([2,1,1,2]))) #4
