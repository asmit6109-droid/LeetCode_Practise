class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        for i in range(n):
            fast = fast.next

        if fast == None:
            head = head.next
            return head

        while fast.next!= None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head 