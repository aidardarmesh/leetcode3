def validPath(n, edges, s, d):
    from collections import defaultdict

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, d, seen):
        ans = False
        seen.add(node)
        
        if node == d:
            return True

        for n in graph[node]:
            if not n in seen:
                ans |= dfs(n, d, seen)
        
        return ans

    return dfs(s, d, set())

