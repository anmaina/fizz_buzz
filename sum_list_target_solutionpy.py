from typing import List


# def twoSum(nums: List[int], target: int) -> List[int]:
#         answer = []
#         for number in range(len(nums)):
#             for second_number in range(len(nums)):
#                 if number != second_number:
#                     if nums[number] + nums[second_number] == target:
#                         answer.append(number)
#                         answer.append(second_number)
#                         yield answer
  



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         answer = []
#         a = 0
#         while a != (len(nums)-1):
#             b = 0
#             while b != (len(nums)-1):
#                 b += 1
#                 if nums[a] + nums[b] == target and b != a:
#                     answer.append(b)
#                     answer.append(a)
#                     return answer
#             a+=1

# def twoSum(nums: List[int], target: int) -> List[int]:
#         answer = []
#         sorted_list = list(sorted(enumerate(nums), key = lambda x: x[1]))
#         print(sorted_list)
#         for ind, element in sorted_list:
#             if target == abs(target):
#                 if element <= target:
#                     new_target_for_search = target - element
#                     print(new_target_for_search)
#                     if new_target_for_search in nums:
#                         second_element_index = nums.index(new_target_for_search, ind+1)
#                         answer.append(ind)
#                         answer.append(second_element_index)
#                         return answer
#             else:
#                 new_target_for_search = target - element
#                 print(new_target_for_search)
#                 if new_target_for_search in nums:
#                     second_element_index = nums.index(new_target_for_search, 0, ind-1)
#                     answer.append(ind)
#                     answer.append(second_element_index)
#                     return answer

def twoSum(nums: List[int], target: int) -> List[int]:
        answer = []
        sorted_list = list(enumerate(nums))
        print(sorted_list)


print(twoSum(nums=[5,75,25], target=100))
