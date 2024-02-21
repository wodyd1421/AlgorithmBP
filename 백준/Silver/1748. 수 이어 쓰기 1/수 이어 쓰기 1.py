n = int(input())
m = len(str(n)) # 자릿수
ans = 0
for x in range(1, m):
    ans += x * (10 ** x - 10 ** (x-1))
ans += m * (n - 10 ** (m-1) + 1)
print(ans)