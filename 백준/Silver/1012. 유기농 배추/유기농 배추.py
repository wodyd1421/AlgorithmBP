import sys
input = sys.stdin.readline
def BFS(x, y):
    queue = [(x, y)]
    graph[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  graph = [[0] * n for _ in range(m)]
  for _ in range(k):
      x, y = map(int, input().split())
      graph[x][y] = 1
  count = 0
  for i in range(m):
      for j in range(n):
          if graph[i][j] == 1:
              BFS(i, j)
              count += 1
  print(count)