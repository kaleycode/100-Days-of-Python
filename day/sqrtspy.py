from typing import Generator

def squared_nums(nums):
    result = []
    for i in nums:
        yield(i*i)
    return result

nums_list = squared_nums([1, 2, 3, 5, 9, 12])
for num in nums_list:
    print (num)