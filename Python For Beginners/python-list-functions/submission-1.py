from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    list_sum = 0
    for num in nums:
        list_sum += num
    return list_sum

def get_min(nums: List[int]) -> int:
    list_min = nums[0]
    for num in nums:
        if num < list_min:
            list_min = num
    return list_min

def get_max(nums: List[int]) -> int:
    list_max = nums[0]
    for num in nums:
        if num > list_max:
            list_max = num
    return list_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
