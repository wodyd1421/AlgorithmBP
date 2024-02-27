n = int(input())
arr = [0] + [1] * n
for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]
ans = 2 * (2*arr[n]+arr[n-1])
print(ans)