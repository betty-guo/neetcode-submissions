class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # look at the top of the stack
            # if its smaller, you just found a temp higher
            # use its index to compute the diff vs current temp day
            # pop from stack
            while s and s[-1][1] < t:
                print(s)
                print(res)
                index, temp = s.pop()
                res[index] = i - index
            s.append((i, t))

        return res