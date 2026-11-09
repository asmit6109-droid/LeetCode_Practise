class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = head
        prev = None 
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
            head = prev
        return head       