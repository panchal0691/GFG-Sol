class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def pairWiseSwap(self, head):
        if head is None or head.next is None:
            return head

        first = head
        second = head.next

        head = second

        while first is not None and second is not None:
            temp = second.next
            second.next = first

            if temp is None or temp.next is None:
                first.next = temp
            else:
                first.next = temp.next

            first = temp
            if temp is not None:
                second = first.next
            else:
                second = None

        return head
