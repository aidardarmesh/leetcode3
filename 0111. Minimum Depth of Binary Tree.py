def minDepth(root):
    def find(node):
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 1
        
        if not node.left:
            return find(node.right) + 1
        
        if not node.right:
            return find(node.left) + 1
        
        return min(find(node.left), find(node.right)) + 1
    
    return find(root)
