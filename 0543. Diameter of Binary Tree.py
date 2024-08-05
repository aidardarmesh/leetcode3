def diameterOfBinaryTree(root):
    self.max_diam = 0

    def max_depth(node):
        if not node:
            return 0
        
        left = max_depth(node.left)
        right = max_depth(node.right)

        self.max_diam = max(self.max_diam, left + right)

        return max(left, right) + 1
    
    max_depth(root)

    return self.max_diam

