def all_paths_source_target(graph):
    start, dest = 0, len(graph)-1
    ans = []

    def dfs(curr_path):
        if curr_path[-1] == dest:
            ans.append(curr_path[:])
            return
        
        for i in graph[curr_path[-1]]:
            curr_path.append(i)
            dfs(curr_path)
            curr_path.pop()
    
    dfs([start])

    return ans


assert all_paths_source_target([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
assert all_paths_source_target([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]