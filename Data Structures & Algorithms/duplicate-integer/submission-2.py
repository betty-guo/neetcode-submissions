class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) space complexity (new set)
        # O(n) time complexity, iterate through the whole list at worst
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False