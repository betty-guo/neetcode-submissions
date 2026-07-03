from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    output_dict = defaultdict(int)
    
    for c in s:
        output_dict[c] += 1

    return output_dict


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    # input: list of list of ints
    # output: dictionary where key is first element, values are rest of elements

    output_dict = defaultdict(list)

    for l in nums:
        output_dict[l[0]] = output_dict[l[0]] + l[1:] # add rest of the list to the existing value
    
    return output_dict


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
