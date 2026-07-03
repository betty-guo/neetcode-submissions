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

        # two pointer _ 1. space complexity; O(1) no new arrays. time complexity: O(n), one pass
        # overwrite the unwanted elements in place
        # use pointer to track the index of the unwanted element, and overwrite with the next correct one

        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         # if it's a value we keep, we overwrite it where the pointer is for the end of our valid array
        #         nums[k] = nums[i] # this modifies nums in place, and the rest of the array after k is garbage
        #         # increment k
        #         k += 1
        # return k

        # two pointer _ 2
        # improves on the previous approach by not shifting every element down
        # realize that output can be unsorted (e.g. can shift elements out of order, e.g. from the end of the array)
        # space complexity is O(1), time complexity is O(n) one pass

        # when do we exit? e.g. when k > end_of_array?
        k = 0
        end_of_array = len(nums) -1
        while k <= end_of_array: # move k
            if nums[k] == val: # if we find a value to overwrite
                while end_of_array >= k and nums[end_of_array] == val : # need to check that this value is smth we want to keep, move while keeping in mind k
                    end_of_array -= 1
                if k > end_of_array:
                    break # shouldn't increment if in a bad state e.g. all remaining values are invalid
                nums[k] = nums[end_of_array] # once I find a valid number, overwrite
                end_of_array -= 1 # move end of array since we already used that value
            else:
                k += 1 # continue iterating through array only if value is valid          
        return k # this is the length of the array once all the swapping is done e.g. we found all the valid values
