class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: array of nums (nums can be negative, can be zero. ints only)
        #       nums array can be empty
        #       array is not sorted (consecutive)
        #.      can have duplicate nums
        # output: LENGTH of longest consecutive sequence e.g. 12345 that can be formed
        # requirements: algo runs in O(n) time

        # to make this run in O(n) time instead of creating a sequence for every number in nums, only do it if its the beginning of a sequence e.g. we didn't already include it in a sequence
        # this is because other than beginning of a new sequence, we can't make a longer sequence anyways

        num_set = set(nums) # deduplicated and for easier O(1) lookup with hashing, vs array is O(n) lookup
        max_length = 0

        for num in nums:
            if (num - 1) not in num_set: # we are at the beginning of a sequence
                length = 1
                while (num + length) in num_set: # these are O(1) in a set and O(n) in an array, which is why convert to set
                    length += 1
                max_length = max(max_length, length)
        
        return max_length

        # space is O(n) for the additional set
        # time is O(n), one pass through the array and go through every item at most once (since only iterate through each sequence once)
            