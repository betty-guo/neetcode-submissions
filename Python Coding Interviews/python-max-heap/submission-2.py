import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    # negative = [-n for n in nums] # reverse first, O(n)
    # heapq.heapify(negative) # heapify O(n). this means negative[0] will have the smallest number, which is negative of the biggest number
    max_heap = []
    # O(nlogn)
    for n in nums: 
        heapq.heappush(max_heap, -n)
    
    
    output = []

    while max_heap:
        output.append(-heapq.heappop(max_heap))

    return output





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
