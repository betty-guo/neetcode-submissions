 # remove all occurences of val in nums in place
# e.g. modify the existing array
# return the number of elements in nums which are not equal to val

# input:
# int val -> value to remove if matching
# List[int] nums -> array to modify in place
# after shifting the array, the value of the array after the first k elements don't matter e.g. can set to -1

# cases:
# val is not in the array, no change. output is len(nums)
# val is entire array, output is 0
# assume array contains both positive and negative integers including 0

# example:
# Input: nums = [3,2,2,3], val = 3
# Output: k = 2, nums = [2,2,_,_]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # counter = 0
        # for num in nums:
        #     if num == val:
        #         nums.remove(num) # can't do this, modifying array while I'm iterating causes skips
        #     else:
        #         counter += 1
        # return counter

        # brute force # space complexity O(n) for temp, time complexity O(n)
        # to_keep = [n for n in nums if n != val]
        # for i in range(len(to_keep)):
        #     nums[i] = to_keep[i]
        # return len(to_keep)

        # two pointer
        # overwrite the unwanted elements in place
        # use pointer to track the index of the unwanted element, and overwrite with the next correct one

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # if it's a value we keep, we overwrite it where the pointer is for the end of our valid array
                nums[k] = nums[i] # this modifies nums in place, and the rest of the array after k is garbage
                # increment k
                k += 1
        return k