# You are given a binary array nums, return the maximum number of consecutive 1's in the array.
# input: List[int] nums
# output: int max_num_consecutive_ones

# Example
# input: nums = [1,1,0,1,1,1]
# output: 3

# assume nums can't be null
# assume nums can be empty
# assume nums can contain no 1s

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_num_consecutive_ones = 0
        ones_counter = 0

        for num in nums:
            if num == 1: # already counting 1s
                ones_counter += 1
                max_num_consecutive_ones = max(max_num_consecutive_ones, ones_counter) # need to increment if we end on a 1
            elif ones_counter > 0: # not a 1
                max_num_consecutive_ones = max(max_num_consecutive_ones, ones_counter)
                ones_counter = 0 # reset to 0

        return max_num_consecutive_ones
        

