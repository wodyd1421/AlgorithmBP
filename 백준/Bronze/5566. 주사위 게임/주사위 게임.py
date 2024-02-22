n, m = map(int, input().split())
gamemap = []
loc = 0
for i in range(n):
    gamemap.append(int(input()))
for j in range(m):
    loc += int(input())
    if loc >= n-1:
        print(j+1)
        break
    loc += gamemap[loc]
    if loc >= n-1:
        print(j+1)
        break