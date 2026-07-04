class LinkedNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

# need to capture case if index < 0 too!!
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if not self.head: # nothing to iterate
            return -1
        if index < 0 or index > self.length - 1: # out of bounds
            return -1

        counter = index
        currNode = self.head
        while counter > 0:
            currNode = currNode.next
            counter -= 1
        
        return currNode.val

    def addAtHead(self, val: int) -> None:
        newNode = LinkedNode(val)
        if not self.head: # new empty list
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = LinkedNode(val)
        if not self.tail: # new empty list
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    # insert BEFORE index-th node of list
    # e.g. if insert at 0, insert before the current 0
    # e.g. if insert at 6 (7th position) and the current length is 6, add to end
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: # add at head
            self.addAtHead(val)
            return
        elif index == self.length: # add a tail
            self.addAtTail(val)
            return
        elif index > self.length or index < 0: # out of bounds
            return
        
        newNode = LinkedNode(val)

        counter = index
        currNode = self.head
        while counter > 0:
            currNode = currNode.next
            counter -= 1
        
        #insert the node right before currNode
        newNode.prev = currNode.prev
        newNode.next = currNode
        currNode.prev.next = newNode
        currNode.prev = newNode

        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1: # out of bounds, can't delete
            return
        
        currNode = self.head
        counter = index
        while counter > 0:
            currNode = currNode.next
            counter -= 1
        
        #delete currNode
        if currNode == self.head:
            self.head = currNode.next # if this is null then no more linked list
            if self.head:
                self.head.prev = None
        elif currNode == self.tail:
            self.tail = currNode.prev
            if self.tail:
                self.tail.next = None
        else:
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev

        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)