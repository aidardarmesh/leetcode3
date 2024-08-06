def countComponents(n, edges):
    from collections import defaultdict

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    ans = 0
    seen = set()

    def dfs(node, graph, seen):
        for n in graph[node]:
            if not n in seen:
                seen.add(n)
                dfs(n, graph, seen)
    
    for i in range(n):
        if not i in seen:
            ans += 1
            dfs(i, graph, seen)
    
    return ans

