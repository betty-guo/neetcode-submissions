# the answer is always unique

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_topK = Counter(nums) # O(n) since iterate through every num

        # bucket sort
        # each array stores other list, where array index is the frequency, sublist is the numbers with that frequence
        # the max frequency is the length of nums (e.g. everything in nums is the same)
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in count_topK.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1): # iterate through the whole thing backwards by frequency, stop at 1
            for num in buckets[i]:
                res.append(num)
                if len(res) == k: # we have topK
                    return res
        
        # the answer should always exist, and k is less than distinct nums

        

        