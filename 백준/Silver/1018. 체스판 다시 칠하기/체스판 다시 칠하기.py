n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
minct = 32
for i in range(n-7):
    for j in range(m-7):
        even = arr[i][j]
        ct = 0
        for k in range(8):
            for l in range(8):
                if ((k+l) % 2 == 0 and arr[i+k][j+l] != even) or ((k+l) % 2 == 1 and arr[i+k][j+l] == even):
                    ct += 1
        minct = min(minct,min(ct,64-ct))
print(minct)