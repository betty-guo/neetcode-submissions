class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: array of nums (nums can be negative, can be zero. ints only)
        #       nums array can be empty
        #       array is not sorted (consecutive)
        #.      can have duplicate nums
        # output: LENGTH of longest consecutive sequence e.g. 12345 that can be formed
        # requirements: algo runs in O(n) time

        # even more naive, store all the nums into a set and for every num try and extend the longest sequence from that num
        # brute force: sort the array (nlogn) and then iterate while counting the max longest consecutive, returning the length
        if not nums:
            return 0

        nums_sorted = sorted(set(nums)) #O(nlogn) and remove duplicates (needed or else halts chain)

        max_length = 0
        length = 1

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == (nums_sorted[i-1] + 1): # while they are consecutive (skip duplicates due to set)
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
        

        return max(max_length, length) # need to do one more check, since if the consective ends on the last element we don't set max_length
            