def can_visit_all_rooms(rooms: list[int]):
    if not rooms:
        return False

    from collections import deque

    visited = set([0])
    q = deque([0])

    while q:
        key = q.popleft()

        for k in rooms[key]:
            if not k in visited:
                q.append(k)
                visited.add(k)

    return len(visited) == len(rooms)

print(can_visit_all_rooms([[1],[2],[3],[]]))
print(can_visit_all_rooms([[1,3],[3,0,1],[2],[0]]))

