# note, if end > len(input_string) need to return empty string or else out of index
# also assume end >= start
def get_substring(input_string: str, start: int, end: int) -> str:
    # this works because the end index is non inclusive and the length of the str is also non inclusive (zero indexed strings)
    if end > len(input_string):
        return ""
    return input_string[start: end]



# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
