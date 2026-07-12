class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while len(s) > 0:
                ind, temp = s[-1]
                if t > temp:
                    res[ind] = i - ind
                    s.pop()
                else: 
                    break
            s.append((i, t))
        return res