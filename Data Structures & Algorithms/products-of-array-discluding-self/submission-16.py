class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # can we use prefix sum somehow? e.g. array where arr[i] = product of every element up to and including i
        # # we can use prefix sum and suffix sum e.g. two arrays, product up to element i (not including), suffix is product of all elements i+1 to end
        # # so productExceptSelf = prefix[i] * suffix[i]
        # # works around division, so don't need to handle 0s
        # O(n) time, since pass through nums twice, O(1) space since only compute output


        # optimize by not storing prefix and suffix, compute the result as we iterate (two passes, forward and backward)
        n = len(nums)
        # initialize as 1, no impact on multiplication. Important that we don't init to 0 in product questions!
        # optimal is to do in two passes, but don't need to store prefix/ suffix, just compute result as we do the passes
        output = [1] * n
        prefix_product_up_to_i = suffix_product_up_to_i = 1
        for i in range(1, n):
            prefix_product_up_to_i *= nums[i - 1]
            output[i] *= prefix_product_up_to_i
        
        for i in range(n - 2, -1, -1): # go backwards
            suffix_product_up_to_i *= nums[i + 1] # we want the product to be product of everything not including the current i
            output[i] *= suffix_product_up_to_i

        return output

# in product/ division questions, make sure to handle divison by 0, and ensure that your indices match (e.g. off by 1 issues in construction)
# step through with test cases to test the logic components for construction