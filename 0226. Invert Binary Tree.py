def invert_tree(root):
    def invert(node):
        if not node:
            return node
        
        left = invert(node.left)
        right = invert(node.right)
        node.left = right
        node.right = left
        return node
    
    return invert(root)

