def minDepth(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    if not root.left:
        return self.minDepth(root.right) + 1
    
    if not root.right:
        return self.minDepth(root.left) + 1
    
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
