#Problem No. 206- Reversed linked list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=None
        c=head
        while c:
            next_node=c.next
            c.next=p
            p=c
            c=next_node
        return p