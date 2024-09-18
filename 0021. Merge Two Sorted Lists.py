def mergeTwoSortedLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = curr = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    while list1:
        curr.next = list1
        list1 = list1.next
        curr = curr.next
    
    while list2:
        curr.next = list2
        list2 = list2.next
        curr = curr.next
    
    return head.next
