# input: nums List[int], of length n
# output: ans List[int], of length 2n
# ans[i] == nums[i], ans[i + n] == nums[i] for 0 <= i <n
# e.g. we stack nums on top of itself twice

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums # basic python, O(n)

        n = len(nums)
        ans = [0] * 2 * n # init array first with the correct size or else get array out of bounds
        for i in range(len(nums)): # time complexity, O(n) one pass, space complexity O(1)
            ans[i] = ans[i+n] = nums[i]
        return ans

