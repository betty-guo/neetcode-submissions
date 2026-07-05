# all lowercase
# length needs to match to be anagram
# strings length can be 0
# no empty strings (length at least 1)

class Solution: 
    
    # time complexity O(m*nlogn), where n is length of the longest string, m is number of strings. This is because sorting take nlogn
    # space complexity O(m*n) where m is the number of strings, n is the length. This is for the additional dictionary for storage
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramLists = defaultdict(list)
        for s in strs:
            sorted_s = str(sorted(s))
            anagramLists[sorted_s].append(s)
        return list(anagramLists.values())

        # other approaches, use number counting (no sorting, O(m * n) time complexity)