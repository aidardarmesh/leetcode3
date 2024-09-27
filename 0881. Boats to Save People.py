def find_num_rescue_boats(people, limit):
    if not people:
        return 0

    people.sort()
    left, right = 0, len(people)-1
    ans = 0

    while left <= right:
        ans += 1
        if people[left] + people[right] > limit:
            right -= 1
        else:
            left += 1
            right -= 1
    
    return ans
