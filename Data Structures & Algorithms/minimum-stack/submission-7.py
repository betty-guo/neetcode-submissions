class MinStack: # all O(1) time complexity, O(n) space complexity for the two stacks

    def __init__(self):
        self.stack = []
        self.minStack = [] # stack that tracks the current min in the entire stack
        # only get added to the stack if it's the current minimum
        # can also track the current minimum at every step of add/ remove instead, then don't need to compare

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val: # this passes because if its not init, will never reach second eval
            self.minStack.append(val)# add first min or new min
                

    def pop(self) -> None:
        val = self.stack.pop()
        # remove from the min stack if it's the current min
        if self.minStack and self.minStack[-1] == val:
            self.minStack.pop() # remove from the min stack tracker

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

# make sure to synchronize the two stacks! e.g. if pushing to minStack only when new value is smaller
# need to make sure pop from minStack when the popped value == current minimum or else ends up misaligned