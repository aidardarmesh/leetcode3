def maxAncestorDiff(root):
    if not root:
        return 0
    
    def helper(node, curr_max, curr_min):
        if not node:
            return curr_max - curr_min
        
        curr_max = max(curr_max, node.val)
        curr_min = min(curr_min, node.val)
        left = helper(node.left, curr_max, curr_min)
        right = helper(node.right, curr_max, curr_min)

        return max(left, right)
    
    return helper(root, root.val, root.val)

