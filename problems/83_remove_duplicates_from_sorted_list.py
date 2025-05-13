class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current != None:
            if previous and previous.val == current.val:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next

        return head