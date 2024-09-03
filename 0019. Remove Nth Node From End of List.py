def remove_nth_element(head, n):
    if not head:
        return head
    
    sent = ListNode(-1, head)
    curr = head

    for _ in range(n):
        head = head.next
    
    while head:
        head = head.next
        curr = curr.next
    
    curr.next = curr.next.next

    return sent.next
