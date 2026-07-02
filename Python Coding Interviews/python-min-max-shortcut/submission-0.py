from typing import List


def disallow_negatives(num: int) -> int:
    return max(0, num) #if num is < 0, then return 0


def max_difference(nums: List[int]) -> int:
    max_diff = 0
    last_element = nums[0]
    for num in nums: # for the first iteration, this does nothing
        max_diff = max(max_diff, num - last_element)
        last_element = num
    return max_diff



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
