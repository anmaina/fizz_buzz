'''You are given an integer array nums. You want to maximize the number of points you get by performing the following 
operation any number of times:
Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 
and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.'''

from typing import List

def deleteAndEarn(nums: List[int]) -> int:
    # do sum_identical_list from list
    # use code from robbery i
    sorted_list = sorted(nums, reverse=True)
    print(sorted_list)
    new_list = dict()
    sum_of_equal_num = sorted_list[0]
    for i in range(1, len(sorted_list)):
        if sorted_list[i] == sorted_list[i-1]: 
            if i != len(sorted_list)-1:
                sum_of_equal_num += sorted_list[i]
            else:
                sum_of_equal_num += sorted_list[i]
                # new_list[sum_of_equal_num] = sorted_list[i]
                new_list[sorted_list[i]] = sum_of_equal_num
                # print(new_list)
        else:
            new_list[sorted_list[i-1]] = sum_of_equal_num
            # new_list[sum_of_equal_num] = sorted_list[i-1]
            sum_of_equal_num = sorted_list[i]
    print(new_list)
    sum = 0
    for key, value in new_list.items():
        max_num = max(new_list, key= lambda x: new_list[x])
        print(max_num)
        # print(new_list[key])
        # if new_list[key] == max_num:
        #     del new_list[key-1]
        #     del new_list[key+1]
        #     sum += new_list[key]
        #     del new_list[key]
    return sum
# def deleteAndEarn(nums: List[int]) -> int:
#     sorted_nums = sorted(nums, reverse=True)
#     # print("Sorted_list: ", sorted_nums)
#     index_of_next_el = next_item_find(sorted_nums)
#     nums_without_0el = sorted_nums[index_of_next_el:]
#     # print("Index of Next element is:", index_of_next_el, "List without max el is:", nums_without_0el)
#     if len(nums)==1:
#         return nums[0]
#     else:
#         print("check with max element: ", check_better_scheme(sorted_nums))
#         print("check with max element: ", check_better_scheme(nums_without_0el))
#         return max(check_better_scheme(sorted_nums), check_better_scheme(nums_without_0el))

# def check_better_scheme(nums:List[int])-> int:
#     new_list = []
#     for j in range(len(nums)):
#         # take first element
#         first_el = nums[j]
#         # print("Fist element:", first_el)
#         # - 1  element + 1
#         minus1_element = first_el-1
#         plus1_element = first_el+1
#         # print("First element - 1 is: ", minus1_element, "First element +1 is: ", plus1_element)
#         #  check if those el in nums and delete all occurance of those element
#         for i in range(len(nums)):
#             if nums[i] == minus1_element or nums[i]==plus1_element:
#                 nums[i] = 0
                
#         new_list.append(nums[j])
#         # print("!!!!List is: ", nums, "!!!!New_list is: ", new_list)
#         # add element to list
#         # check next element from list
#         # return sum of new list elements   
#     return sum(new_list)

# def next_item_find(nums:List[int])-> int:
#     for i in range(1, len(nums)-1):
#         if nums[i] < nums[0]:
#             return i



# print(deleteAndEarn([1,1,1,1,1])) # 5
# print(deleteAndEarn([1,3,3,3,1])) # 11
print(deleteAndEarn([7,2,4,1])) #13
print(deleteAndEarn([1,1,1,2,4,5,5,5,6])) #18



    
