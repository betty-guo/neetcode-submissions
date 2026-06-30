from typing import List

def contains_duplicate(words: List[str]) -> bool:
    length_list = len(words)
    length_set = len(set(words))
    return length_set < length_list # if this is true, then there is a duplicate
        

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
