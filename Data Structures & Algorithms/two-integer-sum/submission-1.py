# input: 
# array of integers nums
# integer target

# output
# indices i and j such that nums[i]+nums[j] == target
# i != j
# return smaller index first

# Example
# Input: 
# nums = [3,4,5,6], target = 7

# Constraints:
# no null (nums.length >= 2)
# integers can be negative
# only one valid answer

# Output: [0,1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: for each nums in list, iterate through the rest of the list until you find another that adds up to target
        # for i, num_i in enumerate(nums):
        #     for j in range(i+1, len(nums)):
        #         if num_i + nums[j] == target:
        #             return [i,j]
        
        # optimized: store the values in a map, and look up target - i in the map
        seen = {} # key is num, value is index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
