class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input: tokens won't be empty, will be valid RPN and num in [-200, 200]
        #   need to be careful if num == 0 because division by 0
        # output: result of the evaluation of the expression

        # use a stack to apply the operations

        # edge cases

        RPN = []

        for token in tokens:
            if token == "+":
                op2 = RPN.pop()
                op1 = RPN.pop()
                RPN.append(op1 + op2)
            elif token == "-":
                op2 = RPN.pop()
                op1 = RPN.pop()
                RPN.append(op1 - op2)
            elif token == "*":
                op2 = RPN.pop()
                op1 = RPN.pop()
                RPN.append(op1 * op2)
            elif token == "/":
                op2 = RPN.pop()
                op1 = RPN.pop()
                RPN.append(int(op1 / op2)) # floor, truncate to 0, must cast or else double
            else: # is an integer
                RPN.append(int(token))
        return RPN.pop() # should only have one value left