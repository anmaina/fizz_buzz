from typing import List

#### to-do!!!

def binary_search(nums:List, num:int) -> int:
    start, stop = 0, len(nums)-1
    mid = (start + stop)//2
    print("Start is:", start, "stop is:", stop, "Middle is:", mid)
    result = nums[mid]
    

print(binary_search([1,2,3,4,5,6,7,8,8,8,8,8,9], 8))

def check_the_list(nums:List, num:int, start:int, stop:int) -> int:
    while start!=num and stop!=num:
        if result > num or nums[stop] == num:
            start += 1
        elif result < num or nums[start] == num:
            stop -=1
        else:
            print (start, stop)

