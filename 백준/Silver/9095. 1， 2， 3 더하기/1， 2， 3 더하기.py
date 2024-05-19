t = int(input())
arr = [[1], [2], [3]]
e = 0
for i in range(9):
    s, e = e, len(arr)
    for j in range(s, e):
        arr.append(arr[j]+[1])
        arr.append(arr[j]+[2])
        arr.append(arr[j]+[3])
for _ in range(t):
    n = int(input())
    ct = 0
    for s in arr:
        if sum(s) == n:
            ct += 1
    print(ct)