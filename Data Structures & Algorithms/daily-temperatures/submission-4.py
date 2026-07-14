class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # look at the top of the stack
            # if its smaller, you just the next warmest day
            # use its index to compute the diff vs current temp day (num days untl found warmer day)
            # pop from stack
            # keep going until you found a higher temp, then add to stack
            while s and s[-1][1] < t:
                print(s)
                print(res)
                index, temp = s.pop()
                res[index] = i - index
            s.append((i, t)) # add to stack

        return res