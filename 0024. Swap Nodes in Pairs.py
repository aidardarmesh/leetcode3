def swapPairs(head):
    if not head or not head.next:
        return head

    prev, curr = None, head

    new_head = curr.next # 5
    while curr and curr.next:
        if prev:
            prev.next = curr.next # 4
        prev = curr # 3

        next_node = curr.next.next # 2
        curr.next.next = curr # 1

        curr.next = next_node # 3
        curr = next_node # 6
    
    return new_head

[]
[]

1
1

1 -> 2
p
# 1 should point to node that is after the next one
# node next to 1 should point to itself
# current pointer might move twice because pair has been swapped
2 -> 1

1 -> 2 -> 3
# 1 should point to 3
# 2 should point to 1
# curr pointer should move to 3
# 3 should keep pointing to None
# while loop works only until curr node is not None and has next not None

1 -> 2 -> 3 -> 4 ->
# 1 perform swap 1 <-> 2 3 -> 4 ->
# 2 save 3 as next_node
# 3 save curr pointer to prev
# 4 connect prev pointer to new pair
# 5 use dummy pointer to keep reference to new head
# 6 handle use cases with odd number of nodes
