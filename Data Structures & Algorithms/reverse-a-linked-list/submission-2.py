# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input: head ListNode
# output: newHead ListNode

# Example:
# Input: head = [0,1,2,3]

# Output: [3,2,1,0]

# edge cases:
# head can be null
# input can be output (e.g. the listNode is size one)
# the linked list may be circular (e.g. will come back to head at one point)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     # brute force O(n) since only iterate once, no new data struct so O(1)
     # iterate through linked list and build a new linked list by keeping track of the 
     # nodes behind and forward, and setting curr.next = previous, and then jumping to the original curr.next

        if head:
            start_node = head
            previous_node = None
            next_node = None
            curr = head
            while curr: # in case it is circular, curr == start_node at the end
                next_node = curr.next # keep path to next node
                curr.next = previous_node # set current pointer to one behind
                previous_node = curr # set the new previous to the one you are currently at
                curr = next_node # advance
                if curr == start_node:
                    curr.next = previous_node
                    return curr
            return previous_node # when the loop ends, curr is at None so we return previous_node
        else:
            return None # Optional is either a ListNode or None