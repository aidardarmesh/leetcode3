def deleteDuplicates(head):
    LESS_THAN_MIN = -101
    sent = ListNode(-101)
    sent.next = head

    while sent and sent.next:
        while sent and sent.next and sent.val == sent.next.val:
            sent.next = sent.next.next
        
        sent = sent.next
        
    return head

None

-101 1

-101 1

-101 1 2

-101 1 1 1


