def closestValue(root, target):
    ans = []
    closest_val = float('inf')

    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)
    
    dfs(root)
    
    for i in range(len(ans)):
        if abs(closest_val - target) > abs(ans[i] - target):
            closest_val = ans[i]
    
    return closest_val

