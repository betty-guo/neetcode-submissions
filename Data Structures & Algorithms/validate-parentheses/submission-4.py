class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack, if its an opening bracket add it to the stack
        # if its a closing one, pop from the stack it should match, otherwise return false
        # if get to the end and stack is empty, return true.
        # otherwise return false, there is some unmatched opening brackets still

        matching_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            # is a closing bracket
            elif not stack : # stack is empty, no opening brackets
                return False
            elif stack[-1] != matching_brackets[c]: # peek at top
                return False
            else:
                stack.pop()

        return len(stack) == 0
