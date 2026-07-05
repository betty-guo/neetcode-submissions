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
# i != j

# Output: [0,1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # O(n) space and time, extra hash map for storing all values but only do one pass
        valMap = {} # map to store target - value: index, for reverse lookup. Then don't need to iterate through O(N^2) time e.g. brute force
        for i, num in enumerate(nums):
            diff = target - num # calculate the matching side you need
            if diff in valMap:
                return [valMap[diff], i]
            valMap[num] = i # this way never fetch i == j
            