class Solution:
    def isValid(self, s: str) -> bool:
        #brute force, keep removing valid parantheses. If you can't and string isn't empty then return False
        # use a stack, if its an opening bracket add it to the stack
        # if its a closing one, pop from the stack it should match, otherwise return false
        # if get to the end and stack is empty, return true.
        # otherwise return false, there is some unmatched opening brackets still
        # space, O(n) for stack
        # time, O(n) for one pass of string

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
            elif stack and stack[-1] == matching_brackets[c]: # stack is not empty, and opening bracket matches
                stack.pop()
            else:
                return False # it means stack was empty or non matching parantheses

        return len(stack) == 0
