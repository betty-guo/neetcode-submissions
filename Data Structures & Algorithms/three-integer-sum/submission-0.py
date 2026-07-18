# input: integer array nums, not necessarily sorted
# output: ALL triplets where sum is 0
# output indices must be distinct, output triplets should be distinct, can return in any order
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        res = []
        for i, a in enumerate(nums): # give index, value
            if a > 0:
                break
            elif i > 0 and a == nums[i-1]: # we already saw this number!
                continue # skip duplicates
            else:
                a = nums[i] # fix the number (a)
                l, r = i + 1, len(nums) - 1 # set the pointers
                while l < r: # iterate and find all combos that would add to -a
                    threesum = nums[l] + nums[r] + a
                    if threesum == 0: # if we find a hit
                        res.append([a, nums[l], nums[r]]) # add it to the result
                        l += 1
                        # skip duplicates on left pointer to prevent duplicate triplets
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                    elif threesum < 0:
                        l += 1
                    else:
                        r -= 1
                
        return res

        