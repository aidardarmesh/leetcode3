def canReach(arr, start):
    from collections import deque
    queue = deque([start])
    seen = set([start])
    n = len(arr)

    while queue:
        i = queue.popleft()

        if arr[i] == 0:
            return True
        
        for ii in [i + arr[i], i - arr[i]]:
            if 0 <= ii < n and not ii in seen:
                seen.add(ii)
                queue.append(ii)

    return False
