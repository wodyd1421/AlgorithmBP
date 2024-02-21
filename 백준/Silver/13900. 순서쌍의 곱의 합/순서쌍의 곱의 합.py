n = int(input())
arr = list(map(int, input().split()))
ans = 0
add = sum(arr)
for x in arr:
    add -= x
    ans += x * add
print(ans)