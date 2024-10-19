def inoder_successor(root, p):
    nodes = []
    val_node_mapper = {}

    def dfs(node):
        if not node:
            return
        
        val_node_mapper[node.val] = node
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)

    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        nodes.append(node.val)
        inorder(node.right)
    
    inorder(root)
    
    i = nodes.index(p.val)
    
    if i == len(nodes)-1:
        return None
    
    return val_node_mapper[nodes[i+1]]

