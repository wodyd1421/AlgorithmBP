arr = [[0]*101 for _ in range(101)]
n = int(input())
ct = 0
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            if arr[j][k] == 0:
                ct += 1
            arr[j][k] = 1
print(ct)