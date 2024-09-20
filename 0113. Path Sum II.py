def path_sum(root, target_sum):
    if not root:
        return []
    
    def dfs(node, target_sum, path, paths):
        if not node:
            return

        if target_sum == node.val:
            if not node.left and not node.right:
                paths.append(path + [node.val])
        
        dfs(node.left, target_sum - node.val, path + [node.val], paths)
        dfs(node.right, target_sum - node.val, path + [node.val], paths)
    
    res = []
    dfs(root, target_sum, [], res)

    return res
