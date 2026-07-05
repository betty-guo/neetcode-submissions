# input s and t
# output true if strings are anagrams (e.g. same letters) otherwise return false

# example
# Input: s = "racecar", t = "carrace"

# Output: true


# example 2
# Input: s = "jar", t = "jam"

# Output: false

# edge cases
# both s and t are not null, at least length of 1
# s and t are lowercase (capitalization doesn't matter)
# it's not an anagram if not all of the letters are used

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # O(n + m) since iterate through both strings, space complexity is O(1) since at most 26 characters
        s_count = Counter(s)
        t_count = Counter(t)

        if s_count == t_count:
            return True
        return False
        