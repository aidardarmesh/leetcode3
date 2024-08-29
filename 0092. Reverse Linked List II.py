def reverse_between(head, left, right):
    prev, curr = None, head

    for _ in range(left-1):
        prev = curr
        curr = curr.next

    tail, con = curr, prev

    for _ in range(right-left+1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    if con:
        con.next = prev
    else:
        head = prev

    tail.next = curr

    return head


1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 

# next_node = curr.next
# curr.next = prev
# prev = curr
# curr = next_node

