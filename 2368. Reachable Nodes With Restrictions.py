def reachableNodes(n, edges, restricted):
    from collections import defaultdict

    graph = defaultdict(list)
    seen = set(restricted)
    start = 0

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, graph, seen):
        seen.add(node)

        ans = 1
        for n in graph[node]:
            if not n in seen:
                ans += dfs(n, graph, seen)
        
        return ans
    
    return dfs(start)
