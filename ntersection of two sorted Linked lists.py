class Solution:
    def findIntersection(self,head1,head2):
        newHead = None
        curNode = None
        
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                head1 = head1.next
            elif head2.data < head1.data:
                head2 = head2.next
            else:
                if newHead is None:
                    newHead = Node(head1.data)
                    curNode = newHead
                else:
                    curNode.next = Node(head1.data)
                    curNode = curNode.next
                head1 = head1.next
                head2 = head2.next
        
        return newHead
