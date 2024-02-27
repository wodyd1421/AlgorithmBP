d = int(input())
n, m, k = map(int, input().split())
a, b, c = d - n%d, d - m%d, k%d
if c >= a + b:
    ans = k - a - b
elif c >= min(a, b):
    ans = k - min(a, b)
elif c >= a + b - d:
    ans = k - a - b
else:
    ans = k
print(ans)