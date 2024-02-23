import sys
input = sys.stdin.readline
n = int(input())
arr = []
prev = -1
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    ct = -1
    for j in range(n):
        if (arr[i][0] == arr[j][0]) or (arr[i][1] == arr[j][1]) or (arr[i][2] == arr[j][2]) or (arr[i][3] == arr[j][3]) or (arr[i][4] == arr[j][4]):
            ct += 1
    if prev < ct:
        prev = ct
        m = i + 1
print(m)