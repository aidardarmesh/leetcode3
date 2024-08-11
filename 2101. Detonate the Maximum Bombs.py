def maximumDetonation(bombs):
    from collections import defaultdict
    graph = defaultdict(list)
    n = len(bombs)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            xi, yi, ri = bombs[i]
            xj, yj, _  = bombs[j]

            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)
    
    def dfs(index, graph, seen):
        seen.add(index)
        for neighbor in graph[index]:
            if not neighbor in seen:
                dfs(neighbor, graph, seen)
        
        return len(seen)
    
    ans = 0
    for i in range(n):
        seen = set()
        ans = max(ans, dfs(i, graph, seen))
    
    return ans

# bombs = [[2,1,3],[6,1,4]]
# print(maximumDetonation(bombs))

# bombs = [[1,1,5],[10,10,5]]
# print(maximumDetonation(bombs))

# bombs = [[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]]
# print(maximumDetonation(bombs))

# bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# print(maximumDetonation(bombs))

bombs = [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
print(maximumDetonation(bombs))
