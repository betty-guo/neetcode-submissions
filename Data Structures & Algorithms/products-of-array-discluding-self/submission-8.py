class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # can we use prefix sum somehow? e.g. array where arr[i] = product of every element up to and including i
        # we can use prefix sum and suffix sum e.g. two arrays, product up to element i (not including), suffix is product of all elements i+1 to end
        # so productExceptSelf = prefix[i] * suffix[i]
        # works around division, so don't need to handle 0s

        n = len(nums)
        # prefix/ suffic not including i would have no numbers, leave as 1 so doesn't affect result
        prefix_product = [1] * n
        suffix_product = [1] * n

        for i in range(1, n):
            prefix_product[i] = nums[i - 1] * prefix_product[i-1]
        
        for i in range(n - 2, -1, -1): # go backwards
            suffix_product[i] = nums[i + 1] * suffix_product[i + 1] # we want the product to be product of everything not including the current i

        return [ i * j for i, j in zip(prefix_product, suffix_product)]