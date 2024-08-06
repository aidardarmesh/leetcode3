def zigzagLevelOrder(root):
    if not root:
        return []

    from collections import deque

    queue = deque([root])
    order = 1
    ans = []

    while queue:
        curr_level_len = len(queue)
        level = []

        for _ in range(curr_level_len):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        ans.append(level[::order])
        order *= -1
    
    return ans
