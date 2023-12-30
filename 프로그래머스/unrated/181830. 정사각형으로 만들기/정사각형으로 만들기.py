def solution(arr):
    a=len(arr[0])
    if len(arr) >= a:
        for i in range(len(arr)):
            arr[i] += [0]*(len(arr)-a)
    else:
        arr += [[0]*a]*(a-len(arr))
    return arr