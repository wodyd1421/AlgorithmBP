n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
def dfs(g, v, visited):
    global ct
    visited[v] = True
    ct += 1
    for i in g[v]:
        if not visited[i]:
            dfs(g, i, visited)
visited = [False] * (n+1)
ct = -1
dfs(g, 1, visited)
print(ct)