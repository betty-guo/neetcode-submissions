# input: int[] heights, heights[i] represents heights of the ith bar
# output: MAX amount of water a container can store

# area = height * width (indexes between the two bars * min height of the two bars)
# we are tracking the MAX area, so keep
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            # calculate area and take max
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]: # if this is the shorter bar, then since width is shortening, you keep the tallest bar
                l += 1
            else:
                r -= 1

        return maxArea
        