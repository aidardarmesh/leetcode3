def delete_middle(head):
    prev, middle, fast = None, head, head

    while fast and fast.next:
        prev = middle
        middle = middle.next
        fast = fast.next.next
    
    if not prev:
        return prev

    prev.next = middle.next

    return head

1 -> None

1 -> None

1 -> 3 -> None

