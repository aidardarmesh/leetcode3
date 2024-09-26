def meet_eating_speed(piles, h):
    def find_total_hours(piles, k):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / k)
        return total_hours
    
    left, right = 1, max(piles)
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        total_hours = find_total_hours(piles, mid)

        if total_hours <= h:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans

