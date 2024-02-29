t = int(input())
arr = [[i for i in range(15)]] + [[0]*15 for _ in range(14)]
for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]
for _ in range(t):
    k, n = int(input()), int(input())
    print(arr[k][n])