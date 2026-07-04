# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input: list1 (sorted linked list), list2 (sorted linked list)
# output: head (new sorted linked list)

# example:
# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

# edge cases:
# list1 or list2 are None, return the other or return None if both are None
# if they contain the same values e.g. all 1s, return the values in arbitrary order
# list with just one node, should not break the code
# NEGATIVE values, these comes earlier in the sorted LinkedList and should be handled correctly
# duplicate values across the two lists, can store in new linkedlist in any order

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force, O(n + m) since iterate through each once, O(1) since reusing same nodes
        # choose the smallest node from either list until both lists are empty

        # handles case where one or both are None
        if not list1:
            return list2
        elif not list2:
            return list1
        
        head = ListNode() # dummy empty node, head.next points to front
        currNode = head

        while list1 or list2: # if any of either list left
            # compare the values and choose to append to the list
            if not list1: # if list 1 is out then append list 2 to list
                currNode.next = list2
                break
            elif not list2: # if list2 is out then no comparison
                currNode.next = list1
                break
            elif list1.val <= list2.val:
                currNode.next = list1
                list1 = list1.next # move forward
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next # move forward
        
        return head.next


        
