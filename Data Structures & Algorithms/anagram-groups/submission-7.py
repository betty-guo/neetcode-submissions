# all lowercase
# length needs to match to be anagram
# strings length can be 0
# no empty strings (length at least 1)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramLists = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in anagramLists:
                anagramLists[sorted_s].append(s)
            else:
                anagramLists[sorted_s] = [s]
        
        return list(anagramLists.values())