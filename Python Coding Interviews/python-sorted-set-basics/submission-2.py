from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    # add nums1 to sortedset
    for num in nums1:
        sorted_set.add(num)
    # remove nums2 from sorted_set. If some elements of num2 don't exist in set (edge case), don't throw error
    for num in nums2:
        sorted_set.discard(num)
    # return first three elements of the sorted set. can assume there is at least three elements after operations
    # return [sorted_set.pop(0) for _ in range(3)]
    return list(sorted_set)[:3]


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
