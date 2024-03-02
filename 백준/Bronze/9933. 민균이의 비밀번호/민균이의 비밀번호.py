n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
for x in arr:
    if x[::-1] in arr:
        lth = len(x)
        print(lth, x[lth//2])
        break