from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for num in arr2:
        arr1.append(num)
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    # if n > len(arr):
    #     return []
    # for i in range(n): #range generates a sequence from 0 to n-1, total 0 elements
    #     arr.pop()
    # return arr
    while n > 0 and arr: # while n isn't gone and array isn't empty
        arr.pop()
        n -= 1
    return arr

def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if index < 0 or index >= len(arr): #out of bounds, can't be len(arr) either since array is 0 indexed
        arr.append(element)
    else:
        arr.insert(index, element) # insert syntax is (index, element)
    return arr



# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
