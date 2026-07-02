from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]: # these List[int] are imported from typing library
    rotated_list = deque(arr)
    for i in range(k):
        rotated_list.appendleft(rotated_list.pop())
    return rotated_list

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
