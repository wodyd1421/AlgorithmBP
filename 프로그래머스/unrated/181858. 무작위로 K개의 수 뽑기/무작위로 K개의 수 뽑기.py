def solution(arr, k):
    x = []
    for n in arr:
        if n not in x:
            x.append(n)
        if len(x) == k:
            return x
    if len(x) < k:
        x += [-1]*(k-len(x))
    return x
        