from collections import defaultdict

def findWinners(matches):
    won = defaultdict(int)
    lost = defaultdict(int)

    for w, l in matches:
        won[w] += 1
        lost[l] += 1

    never_lost = []
    lost_once = []

    for i in won:
        if not i in lost:
            never_lost.append(i)
    
    for j in lost:
        if lost[j] == 1:
            lost_once.append(j)
    
    return [sorted(never_lost), sorted(lost_once)]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

