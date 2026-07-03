# input: arr List[int], this array is unsorted
# output: List[int] where every element in that array is replaced
# with greatest element among the elements to its right
# last element is -1
# length of output should be the same
# should end in descending order (e.g. every item on the left needs to be >= neighbors on the right)

# example
# Input: arr = [2,4,5,3,1,2]
# Output: [5,5,3,2,2,-1]

# edge cases:
# arr length is 1: return array [-1]
# all array elements are >= 1
# all array elements are the same
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force
        # scan through every sublist
        # space: O(1)
        # time: O(n^2)
        for i in range(len(arr) - 1):
            max_num = 0
            for j in arr[i + 1:]: # only look to the right
                max_num = max(max_num, j)
            arr[i] = max_num
        arr[len(arr) - 1] = -1
        return arr


        