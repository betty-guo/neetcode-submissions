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
        # space: O(1) -> note, output array does not count towards space complexity
        # time: O(n^2)
        # for i in range(len(arr) - 1):
        #     max_num = 0
        #     for j in arr[i + 1:]: # only look to the right
        #         max_num = max(max_num, j)
        #     arr[i] = max_num
        # arr[len(arr) - 1] = -1
        # return arr

        # n = len(arr)
        # ans = [0] * n # initialize empty array

        # for i in range(n): # iterate through the whole thing
        #     rightMax = -1
        #     for j in range(i+1, n): # if i+1 = n e.g. we are at the last element, this does nothing
        #         rightMax = max(rightMax, arr[j])
        #     ans[i] = rightMax # sets to -1 if at the last index
        # return ans

        # more optimal, if we traverse backwards, only need to traverse the list once
        # space complexity: O(1) since output doesn't count, and didn't ask for in place
        # time complexity: O(n), singular pass
        max_num = arr[-1] # set the max to be the end of the array
        n = len(arr)
        ans = [0] * n
        ans[-1] = -1
        for i in range(n - 2, -1, -1): # iterate backwards through the list starting at the second last index, ending at the start
            ans[i] = max_num
            max_num = max(max_num, arr[i])
        return ans




        