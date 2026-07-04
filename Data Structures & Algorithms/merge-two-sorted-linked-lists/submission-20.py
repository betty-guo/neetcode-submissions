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
# lists are diff length e.g. run out of nodes in one, but other still has nodes

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive case, pick the smaller node and then merge the rest of the two sublists

        # base case, no more merging to do if either one or both are null
        if not list1:
            return list2
        elif not list2:
            return list1

        head = ListNode() # dummy node, head.next is the start of the new merged list

        if list1.val <= list2.val:
            head.next = list1
            head.next.next = self.mergeTwoLists(list1.next, list2)
        else:
            head.next = list2
            head.next.next = self.mergeTwoLists(list1, list2.next) # merge remaining sub lists, and append to current node
        
        return head.next # return start of merged list


        
