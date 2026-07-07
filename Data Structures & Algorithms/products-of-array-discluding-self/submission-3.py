class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force, iterate through the whole nums multiple times and create the new product array
        # time: O(n^2)
        
        # optimized: get product of entire array, then create array by dividing total sum by nums[i]
        # time is O(n) (O(n twice))
        # num can be 0, how to handle if 1 0 or multiple 0s
        # num can be negative
        # there will be at least two nums in num

        total_product = 1 # this does not include 0s
        # if 1 0, then output[] is all 0 except for if nums[i] == 0
        # if 2+ 0, then output[] is all 0
        num_zero = 0 
        for num in nums:
            if num == 0:
                num_zero += 1
            else: # keep total_product without 0
                total_product *= num
        
        output = [0] * len(nums)
        if num_zero == 0: 
            for i, num in enumerate(nums): # no 0s
                output[i] = int(total_product/num) # need to cast since division is always float
        elif num_zero == 1:
            index_zero = nums.index(0)
            output[index_zero] = total_product
            # everything else is 0
        # if more than 1 zero, every result is 0
            
        return output