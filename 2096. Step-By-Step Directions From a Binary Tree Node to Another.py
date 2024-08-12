def getDirections(root, s, d):
    if not root:
        return ''

    from collections import defaultdict, deque

    treeDict = defaultdict(TreeNode)
    parentDict = defaultdict(TreeNode)

    def dfs(node, parent):
        if not node:
            return
        
        treeDict[node.val] = node
        parentDict[node.val] = parent
        dfs(node.left, node)
        dfs(node.right, node)
    
    dfs(root, None)
    seen = set([startValue])
    queue = deque([(startValue, '')])

    while queue:
        n, pathString = queue.popleft()
        
        if n == destValue:
            return pathString
        
        node = treeDict[n]
        
        if node.left:
            if not node.left.val in seen:
                queue.append((node.left.val, pathString + 'L'))
                seen.add(node.left.val)

        if node.right:
            if not node.right.val in seen:
                queue.append((node.right.val, pathString + 'R'))
                seen.add(node.right.val)
        
        parent = parentDict[n]
        if parent != None:
            if not parent.val in seen:
                queue.append((parent.val, pathString + 'U'))
                seen.add(parent.val)
        
    return ''