n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(n):
    ans += A[i]*(i+1)
print(ans)