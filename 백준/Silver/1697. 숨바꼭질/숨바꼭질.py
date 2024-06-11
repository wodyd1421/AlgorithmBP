n, k = map(int, input().split())

from collections import deque

def bfs(start, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        v, t = queue.popleft()
        if v == k:
            print(t)
        for i in [v - 1, v + 1, 2 * v]:
            if 0 <= i <= 10 ** 5 and not visited[i]:
                queue.append((i, t + 1))
                visited[i] = True

visited = [False] * (10 ** 5 + 1)

bfs(n, visited)