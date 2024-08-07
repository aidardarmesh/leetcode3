def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = self.insertIntoBST(root.left, val)
    elif val > root.val:
        root.right = self.insertIntoBST(root.right, val)
    
    return root
