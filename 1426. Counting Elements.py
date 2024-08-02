def countElements(arr):
    s = set(arr)
    cnt = 0

    for num in arr:
        if num + 1 in s:
            cnt += 1
    
    return cnt

arr = [1,2,3]
print(countElements(arr))

arr = [1,2,2,3]
print(countElements(arr))

arr = [1,1,3,3,5,5,7,7]
print(countElements(arr))

