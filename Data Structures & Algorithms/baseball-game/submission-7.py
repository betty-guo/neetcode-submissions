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
        # this is the best data structure since each operation depends on the most recent scores, need access to recent elements
        # but also need to keep all valid scores
        # space: O(n) for the stack where n is the number of operations (upper bound)
        # time: O(n) since iterate through number of operations

        # optimization - keep running total instead of summing at the end (removes one extra pass)
        stack = [] # this should only store ints so we can add etc
        total = 0
        if not operations:
            return 0
        
        for op in operations:
            if op == "+":
                sum_two = stack[-1] + stack[-2]
                stack.append(sum_two)
                total += sum_two
            elif op == "D":
                doubled = stack[-1] * 2
                stack.append(doubled)
                total += doubled
            elif op == "C":
                removed = stack.pop() # remove the last score
                total -= removed
            else: # is an int as a string, needs to be cast! !!!!! common pitfall
                stack.append(int(op)) # assumes valid operations, so don't need to check if can be converted
                total += int(op)
        
        return total
        