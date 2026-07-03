# input: List[str] operations, where operations is one of int, '+', 'D', 'C'
# assume no invalid operations

# output: the SUM of all the scores on the record after applying all the operations

# example
# Input: ops = ["1","2","+","C","5","D"]

# Output: 18 # 1, 2, 5, 10 = 18

# assume input has no invalid operations
# assume that if ops is empty, return 0
# assume no invalid operations e.g. calling C on an empty record, D on an empty record, + when no two scores on the record
# assume all intermediate calcs (scores) fit within an int

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # brute force, store running sum. Update whenever current sum changes
        # store last two scores. But this doesn't hold if we delete the last score and then need to add two
        # intuitively, we use a stack to keep track of the running valid scores

        stack = []
        if not operations:
            return 0
        
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop() # remove the last score
            else: # is an int as a string, needs to be cast!
                stack.append(int(op)) # assumes valid operations, so don't need to check if can be converted
        
        return sum(stack)
        