# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        len = 0
        while curr!=None:
            len +=1
            curr = curr.next
        p = (len-n) + 1
        if n==len:
            return head.next
        curr = head
        for i in range(len -n -1):
            curr = curr.next
        curr.next = curr.next.next
        return head