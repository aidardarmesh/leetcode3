class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

def merge_k_lists(lists):
    import heapq

    sent = curr = ListNode()
    heap = [HeapNode(list_head) for list_head in lists if list_head]
    heapq.heapify(heap)

    while heap:
        heap_node = heapq.heappop(heap)
        node = heap_node.node

        if node.next:
            heapq.heappush(heap, HeapNode(node.next))

        curr.next = node
        curr = curr.next
    
    return sent.next