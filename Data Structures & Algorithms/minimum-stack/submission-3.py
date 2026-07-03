class MinStack:

    def __init__(self):
        self.minStack = []
        self.minStackTracker = [] # stack that tracks the current min in the entire stack
        # only get added to the stack if it's the current minimum

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.minStackTracker or self.minStackTracker[-1] >= val: # this passes because if its not init, will never reach second eval
            self.minStackTracker.append(val)# add first min or new min
                

    def pop(self) -> None:
        val = self.minStack.pop()
        # remove from the min stack if it's the current min
        if self.minStackTracker and self.minStackTracker[-1] == val:
            self.minStackTracker.pop() # remove from the min stack tracker

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        if self.minStackTracker:
            return self.minStackTracker[-1]
