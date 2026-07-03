import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    negative = [-n for n in nums]
    heapq.heapify(negative) # this means negative[0] will have the smallest number, which is negative of the biggest number
    output = []

    while negative:
        output.append(-heapq.heappop(negative))

    return output





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
