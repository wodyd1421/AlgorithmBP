n, m = map(int, input().split())
arr = list(map(int, input().split()))
cur = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            prev = arr[i] + arr[j] + arr[k]
            if cur < prev <= m:
                cur = prev
print(cur)