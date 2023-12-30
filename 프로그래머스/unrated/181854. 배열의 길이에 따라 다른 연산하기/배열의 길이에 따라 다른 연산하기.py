def solution(arr, n):
    if len(arr) % 2:
        for x in range(len(arr)):
            if not x % 2:
                arr[x] += n
    else:
        for x in range(len(arr)):
            if x % 2:
                arr[x] += n
    return arr