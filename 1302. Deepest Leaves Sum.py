def deepestLeavesSum(root):
    from collections import deque

    queue = deque([root])

    while queue:
        curr_level_len = len(queue)
        ans = 0

        for _ in range(curr_level_len):
            node = queue.popleft()
            ans += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return ans
