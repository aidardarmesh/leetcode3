def maxAncestorDiff(root):
    if not root:
        return 0
    
    self.result = 0

    def helper(node, curr_max, curr_min):
        if not node:
            return
        
        self.result = max(self.result, abs(node.val - curr_max), abs(node.val - curr_min))
        curr_max = max(curr_max, node.val)
        curr_min = min(curr_min, node.val)
        helper(node.left, curr_max, curr_min)
        helper(node.right, curr_max, curr_min)

    helper(root, root.val, root.val)
    return self.result
