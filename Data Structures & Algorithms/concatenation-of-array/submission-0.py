# input: nums List[int], of length n
# output: ans List[int], of length 2n
# ans[i] == nums[i], ans[i + n] == nums[i] for 0 <= i <n
# e.g. we stack nums on top of itself twice

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

