# input: numbers, sorted in non decreasing order (e.g. 0 1 1 2 3), increasing but some can be the same
# output: return the indices of two numbers such that they add up to the number target
# the indices are 1-indexed e.g. index 0 is output as 1
# there is always a valid solution
# can't use additional data structures
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1 # need to increase sum
            elif numbers[l] + numbers[r] > target:
                r -=1 # need to decrease sum
            else:
                return [l+1, r+1]
        return [l+1, r+1]
